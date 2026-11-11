# Workflow: prospect-pipeline

One outcome: A sourced, scored B2B target-account database delivered in synchronized dual formats (machine-importable `.csv` / `.xlsx` dataset plus an executive verification report in `.md` / `.html`), fully compliant with corporate data protection regulations.

---

## Execution Steps

### 0. CDL Marketing Brief Resolution
1. Check `.tidyfactor/marketing-brief.md`. If present, adopt established target market (M1), ICP parameters, and core product/service offering.
2. If absent and prompt parameters are underspecified, assume sensible operational defaults and document them under "Assumptions".
3. Ask at most ONE clarifying question, and strictly only if the core offering cannot be identified from context.

### 1. Ingest Scope & Buying Constraints
- **What is sold**: Specific product, service, or engineering capacity.
- **Target markets**: Priority jurisdictions (e.g., Saudi Arabia, UAE, Kuwait, Egypt, UK, US).
- **Target volume**: Default 40 verified accounts (or custom batch size).
- **Constraints**: Sector exclusions, budgetary boundaries, and procurement deadlines.

### 2. Map the 4 Roles in the Buying System
Before naming accounts, map the procurement dynamics for the target vertical:
- **Deciders (صاحب القرار)**: C-level executives, Managing Directors, or Business Owners who control capital allocation.
- **Influencers (المؤثر الفني)**: Engineering consultants, architects, technical leads, and specification writers who draft BOQs and RFP requirements.
- **Gatekeepers (حارس البوابة)**: Vendor management teams, procurement officers, and tender qualification committees.
- **Channel Partners / Resellers (شريك القناة والموزع)**: General contractors, EPCs, system integrators, and distributors who provide high-leverage repeat contract pipelines.

### 3. Sourced Discovery & Live Verification
- **Source Priority**:
  1. Government and association directories (official contractor registers, chamber of commerce registries, tender boards).
  2. Organization primary websites (About, Contact, Projects, Press).
  3. Reputable industry press and trade show exhibitor lists.
- **Verification Rule**: Never treat search engine snippets as proof. Inspect the destination domain.
- **Evidence Trail**: Every prospect record must link to at least one active, verified primary Evidence URL.
- **Date Discipline**: Date-sensitive facts (active tenders, project milestones, budget seasons) must carry an explicit `Verified-on` date (`YYYY-MM-DD`).

### 4. Privacy & Regulatory Compliance
- **Corporate Scope Only**: Target business entities, institutions, and professional titles. Never list private donors, private homeowners, or non-commercial individuals.
- **Zero Guessed Emails**: Never construct or pattern-generate personal email addresses (`first.last@domain.com`). Record only officially published public contact channels (business WhatsApp, official contact forms, published office phone/switchboard, or company LinkedIn page).
- **Regulatory Frameworks**:
  - Enforce compliance with the Saudi Personal Data Protection Law (PDPL), UAE Federal Decree-Law No. 45/2021, and EU GDPR.
  - Outreach messaging must include sender corporate identity, business relevance justification, and an immediate, zero-friction opt-out mechanism.

### 5. Calculate Fit Scores (0–5) & Priority Tiers
Evaluate each candidate account across 5 binary criteria (1 point each):
1. **Relevance (+1)**: Documented activity, mandate, or ongoing projects requiring what is sold.
2. **Authority / Budget (+1)**: Commercial footprint or active capitalization indicates purchasing ability.
3. **Reachability (+1)**: Verified public business contact channel exists and functions.
4. **Proximity (+1)**: Geographic presence or proven history with similar offerings/markets.
5. **Timing (+1)**: Published tender, active build phase, or seasonal budget window within 3–6 months.

**Tier Assignment**:
- **Tier A (Score 4–5)**: High-priority immediate outreach.
- **Tier B (Score 3)**: Secondary nurture target.
- **Tier C (Score ≤ 2)**: Retained strictly if necessary to fulfill list size.

### 6. Generate the Standard 18-Column Matrix
Populate the prospect database schema:
1. `ID` (e.g. `P-001`)
2. `Tier` (`A` / `B` / `C`)
3. `Fit score` (0–5)
4. `Organization`
5. `Segment`
6. `Role in buying system` (`Decider` / `Influencer` / `Gatekeeper` / `Channel partner`)
7. `Country`
8. `City`
9. `Why it fits` (One evidence-backed line)
10. `Evidence URL`
11. `Best first channel` (e.g. Official WhatsApp, Contact Form, Company LinkedIn)
12. `Public business contact` (Published official details only)
13. `Named contact + title` (Only if published professionally by entity; else blank)
14. `Outreach hook` (One line anchored in a verified project or milestone)
15. `Timing note`
16. `Status` (Default `New`)
17. `Verified on` (`YYYY-MM-DD`)
18. `Confidence` (`High` / `Medium` / `Low`)

### 7. Dual Format Delivery & Pre-Emit Quality Self-Critique
1. Export structured dataset to workspace storage: `data/prospects/prospect-list-<slug>-<YYYY-MM-DD>.csv` (or `.xlsx`).
2. Export executive report to `data/reports/prospect-brief-<slug>-<YYYY-MM-DD>.md` (and styled `.html`) containing:
   - Summary counts by Tier and Country.
   - Top 5 high-leverage prospects.
   - Entry routes and procurement portals table.
   - Channels and gathering hubs table.
   - Seasonal calendar and budgeting windows.
   - Transparent search query log and documented gaps.
3. Apply pre-emit critique stamp:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```

---

## Validation checklist

- [ ] Every listed row has a verified, live Evidence URL and Verified-on date (`YYYY-MM-DD`)
- [ ] No private individuals, donors, or personal home addresses included
- [ ] No guessed or pattern-generated emails; unobserved contact fields remain blank
- [ ] Complete deduplication executed across Organization + City
- [ ] Strict adherence to local privacy rules (PDPL / GDPR, mandatory opt-out)
- [ ] Verified count honestly reported against requested list size (zero padding)
- [ ] Dual format export persisted to workspace storage (`.csv`/`.xlsx` and `.md`/`.html`)
- [ ] Pre-emit quality critique stamp applied

