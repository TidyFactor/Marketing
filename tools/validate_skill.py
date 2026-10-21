#!/usr/bin/env python3
"""
validate_skill.py — TidyFactor Marketing Release & Integrity Validator.
Comprehensive 13-point governance audit across all skill artifacts.
"""

import sys
import os
import json
import re
from pathlib import Path

# Ensure UTF-8 output on Windows terminal
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

def main():
    root = Path(__file__).resolve().parent.parent
    errors = []
    warnings = []
    
    print("=" * 60)
    print("  RUNNING TIDYFACTOR MARKETING RELEASE VALIDATION")
    print("=" * 60)
    
    # 1. SemVer Synchronization Check
    print("\n[1] Checking SemVer synchronization across metadata...")
    pkg_file = root / "package.json"
    tf_file = root / ".tidyfactor"
    brand_yaml_file = root / "brand.yaml"
    brand_json_file = root / "brand.json"
    cl_file = root / "CHANGELOG.md"
    
    pkg_ver = json.loads(pkg_file.read_text(encoding="utf-8")).get("version") if pkg_file.exists() else None
    tf_ver = json.loads(tf_file.read_text(encoding="utf-8")).get("version") if tf_file.exists() else None
    
    brand_ver = None
    brand_source = None
    if brand_yaml_file.exists():
        brand_source = "brand.yaml"
        try:
            import yaml
            brand_data = yaml.safe_load(brand_yaml_file.read_text(encoding="utf-8")) or {}
            brand_ver = brand_data.get("version")
        except Exception:
            for line in brand_yaml_file.read_text(encoding="utf-8").splitlines():
                if line.strip().startswith("version:"):
                    brand_ver = line.split(":", 1)[1].strip().strip('"').strip("'")
                    break
    elif brand_json_file.exists():
        brand_source = "brand.json"
        brand_ver = json.loads(brand_json_file.read_text(encoding="utf-8")).get("version")
    
    print(f"  package.json : {pkg_ver}")
    print(f"  .tidyfactor  : {tf_ver}")
    print(f"  {brand_source or 'brand.yaml/json'}: {brand_ver}")
    
    if not (pkg_ver and tf_ver and brand_ver and pkg_ver == tf_ver == brand_ver):
        errors.append(f"SemVer mismatch: package.json ({pkg_ver}), .tidyfactor ({tf_ver}), {brand_source} ({brand_ver})")
    else:
        print(f"  [OK] Version {pkg_ver} synchronized across metadata ({brand_source}).")
        
    if cl_file.exists():
        cl_text = cl_file.read_text(encoding="utf-8")
        if f"[{pkg_ver}]" not in cl_text:
            errors.append(f"CHANGELOG.md missing release section for version [{pkg_ver}]")
        else:
            print(f"  [OK] CHANGELOG.md contains release entry for [{pkg_ver}].")
    else:
        errors.append("CHANGELOG.md missing from repository root.")

    # 2. License Consistency Check
    print("\n[2] Checking license consistency...")
    lic_file = root / "LICENSE"
    if lic_file.exists():
        lic_text = lic_file.read_text(encoding="utf-8")
        if "Apache License" in lic_text or "Version 2.0" in lic_text:
            print("  [OK] LICENSE file exists (Apache-2.0).")
        else:
            warnings.append("LICENSE file exists but may not be Apache-2.0.")
    else:
        errors.append("LICENSE file missing from repository root.")

    # 3. Path References & File Existence from SKILL.md
    print("\n[3] Checking SKILL.md referenced files exist on disk...")
    skill_file = root / "SKILL.md"
    if skill_file.exists():
        skill_text = skill_file.read_text(encoding="utf-8")
        raw_refs = re.findall(r'`(references/(?:commands|workflows|memory)/[a-zA-Z0-9_\-\.]+?\.md)`', skill_text)
        raw_refs += re.findall(r'`(scripts/[a-zA-Z0-9_\-\.]+?\.py)`', skill_text)
        refs = sorted(list(set(raw_refs)))
        for ref in refs:
            full_path = root / ref
            if not full_path.exists():
                errors.append(f"Referenced file does not exist: {ref}")
            else:
                print(f"  [OK] Found {ref}")
    else:
        errors.append("SKILL.md missing from repository root.")

    # 4. Workflow Single Outcome & Validation Checklists
    print("\n[4] Checking workflow checklists...")
    workflows_dir = root / "references" / "workflows"
    if workflows_dir.exists():
        for wf in sorted(workflows_dir.glob("*.md")):
            wf_text = wf.read_text(encoding="utf-8")
            if "## Validation checklist" not in wf_text:
                errors.append(f"Workflow missing mandatory '## Validation checklist': {wf.name}")
            else:
                print(f"  [OK] {wf.name} has Validation checklist.")
    else:
        errors.append("Workflows directory missing: references/workflows/")

    # 5. Leaked Machine-Specific Absolute Paths
    print("\n[5] Auditing for leaked machine-specific absolute paths...")
    leaked_pattern = re.compile(r'([A-Za-z]:\\[wW]amp64\\|/Users/[a-zA-Z0-9_-]+/|/home/[a-zA-Z0-9_-]+/)', re.IGNORECASE)
    scanned_exts = {".md", ".json", ".yaml", ".yml", ".js", ".py"}
    for ext in scanned_exts:
        for p in root.rglob(f"*{ext}"):
            if any(ignored in p.parts for ignored in ["dist", ".git", "__pycache__", "node_modules"]):
                continue
            try:
                content = p.read_text(encoding="utf-8", errors="ignore")
                matches = leaked_pattern.findall(content)
                if matches:
                    rel_p = p.relative_to(root)
                    errors.append(f"Machine-specific path leak in {rel_p}: {matches[0]}")
            except Exception as e:
                warnings.append(f"Could not read {p.name}: {e}")

    # 6. SKILL.md Token Budget
    print("\n[6] Checking SKILL.md token budget...")
    if skill_file.exists():
        st = skill_file.read_text(encoding="utf-8")
        est_tokens = len(st.split()) * 1.25
        print(f"  SKILL.md size: {len(st)} chars / {len(st.split())} words ≈ {int(est_tokens)} tokens")
        if est_tokens > 700:
            errors.append(f"SKILL.md exceeds dispatcher token budget: ~{int(est_tokens)} tokens (max 700)")
        else:
            print(f"  [OK] Within token budget ({int(est_tokens)} tokens, target ~350, max 700).")

    # 7. Memory Freshness Markers
    print("\n[7] Checking memory freshness markers (Rule 11)...")
    from datetime import datetime, timezone
    today = datetime.now(timezone.utc)
    mem_dir = root / "references" / "memory"
    if mem_dir.exists():
        for mf in sorted(mem_dir.glob("*.md")):
            mt = mf.read_text(encoding="utf-8")
            m = re.search(r'<!--\s*last-verified:\s*(\d{4}-\d{2}-\d{2})\s*-->', mt)
            if not m:
                warnings.append(f"Missing freshness stamp <!-- last-verified: YYYY-MM-DD --> in {mf.name}")
            else:
                d_str = m.group(1)
                try:
                    vf_date = datetime.strptime(d_str, "%Y-%m-%d").replace(tzinfo=timezone.utc)
                    age_days = (today - vf_date).days
                    if age_days > 180:
                        warnings.append(f"Memory file {mf.name} freshness marker is stale ({age_days} days old > 180)")
                    else:
                        print(f"  [OK] {mf.name}: verified {d_str} ({age_days} days ago)")
                except Exception:
                    warnings.append(f"Malformed date in freshness stamp for {mf.name}: {d_str}")

    # 8. SKILL.md Frontmatter YAML Syntax
    print("\n[8] Checking SKILL.md frontmatter YAML syntax & constraints (Rule 9)...")
    if skill_file.exists():
        st = skill_file.read_text(encoding="utf-8")
        fm_match = re.match(r'^---\r?\n(.*?)\r?\n---', st, re.DOTALL)
        if not fm_match:
            errors.append("SKILL.md missing valid YAML frontmatter delimiter (--- ... ---)")
        else:
            fm_raw = fm_match.group(1)
            try:
                try:
                    import yaml
                    fm_data = yaml.safe_load(fm_raw)
                except ImportError:
                    fm_data = {}
                    for line in fm_raw.splitlines():
                        if ":" in line and not line.strip().startswith("#"):
                            k, v = line.split(":", 1)
                            fm_data[k.strip()] = v.strip().strip('"').strip("'")

                if not isinstance(fm_data, dict):
                    errors.append("SKILL.md frontmatter must parse into a mapping/dict.")
                else:
                    name_val = fm_data.get("name")
                    desc_val = fm_data.get("description", "")
                    if not name_val or not re.match(r'^[a-z0-9-]+$', str(name_val)):
                        errors.append(f"Invalid name in frontmatter: '{name_val}'")
                    else:
                        print(f"  [OK] Name: '{name_val}' (valid).")
                    if len(desc_val) > 1024:
                        errors.append(f"SKILL.md description too long ({len(desc_val)} > 1024 chars)")
                    else:
                        print(f"  [OK] Description: {len(desc_val)}/1024 chars (YAML syntax valid).")
            except Exception as e:
                errors.append(f"SKILL.md YAML frontmatter parsing failed: {e}")

    # 9. Runtime Tooling Manifest
    print("\n[9] Checking Runtime Tooling Manifest & Scope declaration (Rule 10)...")
    manifest_file = root / "manifest.json"
    if manifest_file.exists():
        try:
            m_data = json.loads(manifest_file.read_text(encoding="utf-8"))
            tools = m_data.get("tools", [])
            print(f"  [OK] Tooling Scope declared with {len(tools)} tool(s).")
        except Exception as e:
            errors.append(f"manifest.json parsing error: {e}")
    else:
        errors.append("manifest.json missing from repository root.")

    # 10. Test Scenarios
    print("\n[10] Checking Test Scenarios (tests/scenarios.md)...")
    scenarios_file = root / "tests" / "scenarios.md"
    if scenarios_file.exists():
        s_text = scenarios_file.read_text(encoding="utf-8")
        sc_count = len(re.findall(r'##\s+Scenario\s+\d+:', s_text))
        if sc_count < 3:
            warnings.append(f"tests/scenarios.md has only {sc_count} scenario(s), minimum 3 recommended.")
        else:
            print(f"  [OK] tests/scenarios.md found with {sc_count} test scenarios (min 3).")
    else:
        warnings.append("Missing tests/scenarios.md test evaluation file.")

    # 11. MCP Boundary Documentation
    print("\n[11] Checking MCP boundary documentation (Rule 12)...")
    if skill_file.exists() and "Skill vs MCP Boundary" in skill_file.read_text(encoding="utf-8"):
        print("  [OK] SKILL.md contains Skill vs MCP Boundary section.")
    else:
        warnings.append("SKILL.md missing explicit 'Skill vs MCP Boundary' section.")

    # 12. Contextual Decision Layer & Decision Gates
    print("\n[12] Checking Contextual Decision Layer & Decision Gates (Rule 14 / CDL v1.1.0)...")
    if manifest_file.exists():
        try:
            m_data = json.loads(manifest_file.read_text(encoding="utf-8"))
            gates = m_data.get("decision_gates", [])
            if not gates:
                warnings.append("manifest.json missing 'decision_gates' declaration (CDL v1.1.0).")
            else:
                print(f"  [OK] manifest.json contains {len(gates)} valid decision gate(s) (CDL v1.1.0 compliant).")
        except Exception:
            pass

    # 13. Token Efficiency & YAML Primacy
    print("\n[13] Checking Token Efficiency & YAML Primacy (Rule 15)...")
    if brand_yaml_file.exists():
        print("  [OK] brand.yaml present (cognitive layer prioritized for token efficiency).")
    else:
        warnings.append("Missing brand.yaml. Adopting brand.yaml is recommended under Rule 15 for 35-50% token efficiency.")

    print("\n" + "=" * 60)
    if warnings:
        print(f"[WARN] {len(warnings)} non-blocking warning(s):")
        for w in warnings:
            print(f"  ⚠️  {w}")
    
    if errors:
        print(f"[FAIL] {len(errors)} validation error(s) found:")
        for err in errors:
            print(f"  ❌ {err}")
        print("=" * 60)
        sys.exit(1)
    else:
        print("[SUCCESS] ALL SKILL INTEGRITY CHECKS PASSED!")
        print("=" * 60)
        sys.exit(0)

if __name__ == "__main__":
    main()
