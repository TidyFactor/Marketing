# Command: prospects

Runtime dispatcher for B2B Account Intelligence, Buying System Mapping, Target Prospect Discovery, and Sourced Account Verification.

---

## Capabilities Handled

1. **Buying System Mapping**: Decompose procurement leverage across 4 distinct roles (Deciders, Influencers, Gatekeepers, Channel Partners).
2. **Account Fit Scoring (0–5)**: Binary 5-point evaluation across Relevance, Budget/Authority, Public Reachability, Market Proximity, and Active Timing.
3. **Priority Tier Assignment**: Tier A (4–5), Tier B (3), and Tier C (≤ 2) segmentation with zero padded records.
4. **Sourced 18-Column Database Generation**: Standardized matrix output with verified Evidence URLs and verified-on timestamps.
5. **Regulatory & Privacy Governance**: Corporate-only targeting, prohibition of guessed/constructed contact patterns, and compliance with regional data protection statutes (Saudi PDPL, UAE Decree-Law 45/2021, EU GDPR) with mandatory opt-out.
6. **Dual Export Compilation**: Simultaneous generation of machine-importable data (`.csv` / `.xlsx`) and executive analytical documentation (`.md` / `.html`).

---

## What It Loads

- **Workflow**: `../workflows/prospect-pipeline.md`
- **Memory**: `../memory/frameworks.md` (Section 6) + `../memory/quality-bar.md` (B2B Data Integrity Invariants) + `../memory/arabic-writing.md` (when targeting Arab markets)

---

## What It Does NOT Load

- Do not load `../workflows/paid-acquisition.md` (ad spend and creative testing belong to `advertising.md`).
- Do not load `../workflows/email-lifecycle.md` (drip automations and newsletter flows belong to `email.md`).
- Do not perform mass unverified scraping or harvest private personal data behind authentication walls.

