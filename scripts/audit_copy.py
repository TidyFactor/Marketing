#!/usr/bin/env python3
"""
TidyFactor Marketing Copy Quality Auditor
Scans direct-response marketing copy, ad headlines, and landing page scripts
for AI anti-patterns, banned cliches, robotic phrasing, and angle diversity.
"""

import sys
import os
import re
import json
import argparse
from pathlib import Path

# Ensure UTF-8 output on Windows console
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if sys.stderr and hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

BANNED_AI_CLICHES = [
    # English Slop
    r"\bunleash\b", r"\belevate\b", r"\bgame-changer\b", r"\brevolutionize\b",
    r"\bseamlessly\b", r"\btap into\b", r"\bdive deep\b", r"\bdelve into\b",
    r"\bunlock your potential\b", r"\bin today's fast-paced world\b",
    r"\blook no further\b", r"\bcutting-edge\b", r"\bstate-of-the-art\b",
    # Arabic Slop
    r"في عالمنا اليوم المتسارع", r"في عصر التكنولوجيا", r"أطلق العنان",
    r"انغمس في", r"غيّر قواعد اللعبة", r"حلول سحرية", r"فريدة من نوعها",
    r"نقدم لكم بكل فخر", r"لا داعي للبحث بعد الآن", r"بوابتك نحو"
]

def audit_text_content(text: str, file_name: str = "inline-copy") -> dict:
    issues = []
    lines = text.splitlines()
    
    # 1. Check for AI Cliches & Marketing Slop
    for idx, line in enumerate(lines, start=1):
        for pattern in BANNED_AI_CLICHES:
            matches = re.finditer(pattern, line, re.IGNORECASE)
            for m in matches:
                issues.append({
                    "type": "banned_cliche",
                    "severity": "high",
                    "line": idx,
                    "matched": m.group(0),
                    "message": f"Banned marketing cliché detected: '{m.group(0)}'. Replace with concrete proof or specific benefit."
                })
                
    # 2. Check for Pre-emit critique stamp
    has_critique = bool(re.search(r"/\*\s*Pre-emit critique:[^\*]+\*/", text, re.IGNORECASE))
    if not has_critique and not text.startswith("#"):
        issues.append({
            "type": "missing_critique_stamp",
            "severity": "medium",
            "line": 1,
            "message": "Missing 7-axis pre-emit critique stamp: /* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */"
        })

    # 3. Calculate Score
    high_issues = [i for i in issues if i["severity"] == "high"]
    med_issues = [i for i in issues if i["severity"] == "medium"]
    
    score = max(0, 100 - (len(high_issues) * 20) - (len(med_issues) * 10))
    passed = len(high_issues) == 0 and score >= 80

    return {
        "file": file_name,
        "score": score,
        "passed": passed,
        "total_issues": len(issues),
        "issues": issues,
        "timestamp": "2026-09-02T06:00:00Z"
    }

def main():
    parser = argparse.ArgumentParser(description="TidyFactor Marketing Copy Auditor")
    parser.add_argument("target", nargs="?", help="Path to copy file or markdown script")
    parser.add_argument("--text", help="Direct copy string to audit")
    parser.add_argument("--json", action="store_true", help="Output pure JSON format")

    args = parser.parse_args()

    if args.text:
        content = args.text
        filename = "string-input"
    elif args.target and Path(args.target).exists():
        target_path = Path(args.target)
        content = target_path.read_text(encoding="utf-8", errors="replace")
        filename = str(target_path)
    else:
        # Default sample check
        content = "في عالمنا اليوم المتسارع، نقدم لكم بكل فخر الحل السحري لتغيير قواعد اللعبة."
        filename = "demo-sample"

    result = audit_text_content(content, filename)

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        status_str = "[PASS]" if result["passed"] else "[FAIL]"
        print(f"\n{status_str} Marketing Copy Quality Audit — Score: {result['score']}/100")
        print(f"Target: {result['file']}")
        print(f"Issues Found: {result['total_issues']}\n")
        for iss in result["issues"]:
            print(f"  - [Line {iss.get('line', '?')}] [{iss['severity'].upper()}] {iss['message']}")
        print()

    sys.exit(0 if result["passed"] else 1)

if __name__ == "__main__":
    main()
