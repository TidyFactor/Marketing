# Command: audit

Audits marketing copy, ad headlines, landing pages, and email drafts for AI clichés, banned fluff, and compliance with the 7-axis pre-emit critique stamp (`P5 H5 E5 S5 R5 V5 D5`).

---

## What It Loads

- **Script**: `scripts/audit_copy.py`
- **Memory**: `references/memory/quality-bar.md`
- **Memory**: `references/memory/arabic-writing.md`

---

## Execution Pattern

### 1. Direct Target File Audit
```bash
python scripts/audit_copy.py path/to/marketing-copy.md --json
```

### 2. Inline Copy String Audit
```bash
python scripts/audit_copy.py --text "Unleash your business with our game-changing platform" --json
```

---

## Validation checklist

- [ ] Command routes deterministically to `scripts/audit_copy.py`.
- [ ] Returns structured JSON with line numbers, severity, and matched patterns.
- [ ] Validates 7-axis pre-emit critique stamp presence.
- [ ] Reports zero false positives on clean technical copy.
