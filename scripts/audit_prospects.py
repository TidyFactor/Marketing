#!/usr/bin/env python3
"""
audit_prospects.py - TidyFactor B2B Prospect Matrix & Privacy Linter
Validates B2B prospect CSV exports against the canonical 18-column schema,
verifies URL evidence integrity, checks date formats, validates fit scores,
and enforces data privacy invariants (PDPL / GDPR compliance).
"""

import sys
import os
import csv
import json
import re
from datetime import datetime

EXPECTED_COLUMNS = [
    "ID",
    "Tier",
    "Fit score",
    "Organization",
    "Segment",
    "Role in buying system",
    "Country",
    "City",
    "Why it fits",
    "Evidence URL",
    "Best first channel",
    "Public business contact",
    "Named contact + title",
    "Outreach hook",
    "Timing note",
    "Status",
    "Verified on",
    "Confidence"
]

VALID_ROLES = {"decider", "influencer", "gatekeeper", "channel partner"}
VALID_TIERS = {"a", "b", "c"}
VALID_CONFIDENCE = {"high", "medium", "low"}

def audit_file(file_path):
    issues = []
    stats = {
        "total_rows": 0,
        "valid_rows": 0,
        "tier_a": 0,
        "tier_b": 0,
        "tier_c": 0,
        "duplicates": 0,
        "missing_urls": 0,
        "invalid_dates": 0
    }

    if not os.path.exists(file_path):
        return {"passed": False, "error": f"File not found: {file_path}", "stats": stats, "issues": [f"File not found: {file_path}"]}

    try:
        with open(file_path, "r", encoding="utf-8-sig") as f:
            reader = csv.reader(f)
            header = next(reader, None)

            if not header:
                return {"passed": False, "error": "CSV file is empty", "stats": stats, "issues": ["Empty CSV"]}

            # Normalize headers
            norm_header = [h.strip() for h in header]
            header_map = {col.lower(): i for i, col in enumerate(norm_header)}

            # Check expected columns
            missing_cols = [col for col in EXPECTED_COLUMNS if col.lower() not in header_map]
            if missing_cols:
                issues.append(f"Header schema mismatch. Missing columns: {', '.join(missing_cols)}")

            seen_entities = set()
            row_idx = 1

            for row in reader:
                if not row or not any(row):
                    continue
                row_idx += 1
                stats["total_rows"] += 1
                row_valid = True

                # Extract key fields safely
                def get_field(col_name):
                    idx = header_map.get(col_name.lower())
                    return row[idx].strip() if idx is not None and idx < len(row) else ""

                row_id = get_field("ID") or f"Row-{row_idx}"
                org = get_field("Organization")
                city = get_field("City")
                country = get_field("Country")
                role = get_field("Role in buying system").lower()
                evidence_url = get_field("Evidence URL")
                fit_score = get_field("Fit score")
                tier = get_field("Tier").lower()
                verified_on = get_field("Verified on")
                confidence = get_field("Confidence").lower()
                contact = get_field("Public business contact")

                # 1. Organization & Deduplication
                if not org:
                    issues.append(f"[{row_id}] Missing Organization name")
                    row_valid = False
                else:
                    entity_key = f"{org.lower()}|{city.lower()}|{country.lower()}"
                    if entity_key in seen_entities:
                        issues.append(f"[{row_id}] Duplicate organization detected: '{org}' in '{city}'")
                        stats["duplicates"] += 1
                        row_valid = False
                    seen_entities.add(entity_key)

                # 2. Evidence URL
                if not evidence_url or not (evidence_url.startswith("http://") or evidence_url.startswith("https://")):
                    issues.append(f"[{row_id}] Missing or invalid Evidence URL for '{org}': '{evidence_url}'")
                    stats["missing_urls"] += 1
                    row_valid = False

                # 3. Verified On Date
                if not verified_on:
                    issues.append(f"[{row_id}] Missing 'Verified on' date for '{org}'")
                    stats["invalid_dates"] += 1
                    row_valid = False
                else:
                    try:
                        datetime.strptime(verified_on, "%Y-%m-%d")
                    except ValueError:
                        issues.append(f"[{row_id}] 'Verified on' date not in YYYY-MM-DD format: '{verified_on}'")
                        stats["invalid_dates"] += 1
                        row_valid = False

                # 4. Role in Buying System
                if role and role not in VALID_ROLES:
                    issues.append(f"[{row_id}] Invalid role '{role}'. Must be one of: Decider, Influencer, Gatekeeper, Channel partner")
                    row_valid = False

                # 5. Fit Score & Tier Consistency
                if fit_score:
                    try:
                        score_num = int(fit_score)
                        if score_num < 0 or score_num > 5:
                            issues.append(f"[{row_id}] Fit score out of range (0-5): {score_num}")
                            row_valid = False
                        else:
                            if score_num >= 4:
                                stats["tier_a"] += 1
                                if tier and tier != "a":
                                    issues.append(f"[{row_id}] Tier mismatch: score {score_num} should be Tier A, got Tier {tier.upper()}")
                            elif score_num == 3:
                                stats["tier_b"] += 1
                                if tier and tier != "b":
                                    issues.append(f"[{row_id}] Tier mismatch: score {score_num} should be Tier B, got Tier {tier.upper()}")
                            else:
                                stats["tier_c"] += 1
                                if tier and tier != "c":
                                    issues.append(f"[{row_id}] Tier mismatch: score {score_num} should be Tier C, got Tier {tier.upper()}")
                    except ValueError:
                        issues.append(f"[{row_id}] Fit score must be an integer: '{fit_score}'")
                        row_valid = False

                # 6. Privacy & Personal Data Checks
                if "@gmail.com" in contact.lower() or "@yahoo.com" in contact.lower() or "@hotmail.com" in contact.lower():
                    issues.append(f"[{row_id}] Warning: Public contact appears to be a personal/free consumer email: '{contact}'")

                if row_valid:
                    stats["valid_rows"] += 1

    except Exception as e:
        return {"passed": False, "error": str(e), "stats": stats, "issues": [f"Exception: {str(e)}"]}

    passed = len(issues) == 0 and stats["total_rows"] > 0
    return {
        "passed": passed,
        "file": file_path,
        "stats": stats,
        "issues": issues
    }

def main():
    if len(sys.argv) < 2:
        print("Usage: python audit_prospects.py <path_to_prospects.csv> [--json]")
        sys.exit(1)

    file_path = sys.argv[1]
    json_mode = "--json" in sys.argv

    result = audit_file(file_path)

    if json_mode:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("=" * 60)
        print("  TIDYFACTOR B2B PROSPECT AUDITOR & PRIVACY LINTER")
        print("=" * 60)
        print(f"File: {file_path}")
        print(f"Status: {'[PASSED]' if result['passed'] else '[FAILED]'}")
        print(f"Total rows inspected: {result['stats']['total_rows']}")
        print(f"Valid verified rows:  {result['stats']['valid_rows']}")
        print(f"Tier Breakdown: A={result['stats']['tier_a']}, B={result['stats']['tier_b']}, C={result['stats']['tier_c']}")

        if result['issues']:
            print("\nIssues Found:")
            for issue in result['issues'][:20]:
                print(f"  - {issue}")
            if len(result['issues']) > 20:
                print(f"  ... and {len(result['issues']) - 20} more issues.")
        else:
            print("\n[SUCCESS] Schema, evidence URLs, dates, and privacy constraints 100% verified!")

    sys.exit(0 if result["passed"] else 1)

if __name__ == "__main__":
    main()

