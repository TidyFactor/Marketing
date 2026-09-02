# Marketing Discovery & Brief Workflow

> **Outcome**: Generates an authoritative `.tidyfactor/marketing-brief.md` baseline capturing target market, brand voice, funnel stage, conversion model, and delivery scope.

---

## 📋 Step 0: Context Delta Resolution Engine

Before asking any questions, execute the mechanical resolution formula:

$$\text{Unknowns} = \text{Required Decisions} - (\text{Discovered Facts} \cup \text{Brain KIs})$$

### 1. Required Decisions Set (from `manifest.json["decision_gates"]`):
- `target_market`: Regional calibration (GCC, Egypt/Levant, Global B2B SaaS, Bilingual MENA).
- `brand_voice`: Voice archetype (Authoritative Challenger, Empathetic Guide, Elite Luxury, High-Energy Direct Response).
- `funnel_stage`: Conversion focus (Top / Middle / Bottom of funnel).
- `core_offer`: Headline value proposition and transaction vehicle.

### 2. Discovered Facts (Auto-Sensing + Local Staleness Tracking):
- Inspect `brand.json` and `BRAND-GUIDELINES.md` on disk.
- If `track_staleness: true` is configured, verify file hash/mtime against stored snapshot.
- Any decision successfully extracted from local disk is removed from $\text{Unknowns}$.

### 3. Fail-Open MCP Brain Acceleration:
- If unresolved unknowns remain AND `search_knowledge_base` is available:
  - Query `search_knowledge_base(query="marketing persona brand voice", scope="project")`.
  - If a valid marketing KI exists, populate the context and remove from $\text{Unknowns}$.
- **Fail-Open Invariant**: If Brain MCP is unavailable or offline, skip instantly with 0ms delay without warnings.

---

## 💬 Step 1: Interactive Disclosure & Micro-Discovery

If $\text{Unknowns} = \emptyset$:
- Display the synthesized 4-line baseline summary.
- Suggest next commands (`/strategy`, `/advertising`, `/email`, `/content`) immediately.

If $\text{Unknowns} \neq \emptyset$:
> **Anti-Bot Invariant**: Strictly forbid bot persona greetings (*"أهلاً بك بصفتي خبير التسويق..."*) or conversational filler. Present genuine Unknowns interactively with structured A/B/C/D options and highlighted recommendations:

### Question 1: Target Market & Regional Tone (`target_market`)
- **(A) Gulf / GCC (Saudi Arabia 🇸🇦, UAE 🇦🇪, Kuwait 🇰🇼, Qatar 🇶🇦)** — High prestige, trust-first, WhatsApp/Installments framing, modern polished Arabic.
- **(B) Egypt & Levant (Egypt 🇪🇬, Jordan 🇯🇴)** — Practical ROI, high energy, relatable wit, cash-on-delivery & InstaPay framing.
- **(C) Global / B2B SaaS** — Direct, metric-dense, self-serve focused, English-first.
- **(D) (Recommended) Bilingual / Unified MENA** — Pan-Arab modern standard with English tech pairing.

### Question 2: Brand Voice Archetype (`brand_voice`)
- **(A) (Recommended) Authoritative Challenger** — Direct, contrarian, proof-backed, no-nonsense.
- **(B) Empathetic Guide** — Supportive, story-driven, transformational, warm.
- **(C) Elite Luxury / High-End** — Minimalist, aspirational, refined confidence.
- **(D) High-Energy Direct Response** — Urgent, benefit-stacked, conversion-focused.

### Question 3: Funnel Focus & Core Offer (`funnel_stage` + `core_offer`)
- **(A) Top-of-Funnel Lead Magnet** — Free guide, checklist, audit, quiz.
- **(B) Middle-of-Funnel Trial / Demo** — Product-led trial, 1-on-1 strategy call.
- **(C) (Recommended) Bottom-of-Funnel Direct Sale / Promo** — E-commerce purchase, limited-time launch offer.

---

## 💾 Step 2: Persist Baseline & Single-Direction Brain Push

1. Format and write `.tidyfactor/marketing-brief.md`:
```markdown
# Marketing Brief Baseline

- **Product / Brand**: [Extracted or Confirmed Name]
- **Target Market**: [GCC / Egypt & Levant / Global / Unified MENA]
- **Brand Voice**: [Authoritative / Empathetic / Luxury / Direct Response]
- **Funnel Stage**: [Top / Middle / Bottom]
- **Core Offer**: [Lead Magnet / Trial / Direct Transaction]
- **Deliverable Scope**: [Sprint Copy / Multi-Channel Blueprint]
- **Last Updated**: [Current Date]
```

2. Format snapshot `.tidyfactor/marketing-brief.snapshot.json` for deterministic local staleness tracking.

3. **Anti-Dual-Write Outbound Push (`--sync-brain`)**:
   - The local file is ALWAYS the single source of truth.
   - When explicitly passed `--sync-brain`, format the deliverable as an Atomic KI and push to Brain MCP via `extract_knowledge_item`.
   - Never perform simultaneous dual writes.

---

## 🎯 Step 3: Self-Critique & Actionable Summary

Stamp the 7-axis critique:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```
Display a concise summary and suggest the next logical marketing command (`/strategy`, `/advertising`, `/email`, `/content`).

---

## ## Validation checklist

- [ ] Context Delta Resolution computed prior to prompting user.
- [ ] No questions asked for parameters already discovered on disk.
- [ ] `.tidyfactor/marketing-brief.md` created or verified on disk.
- [ ] Regional calibration (GCC, Egypt, Global) explicitly recorded.
- [ ] Brand voice archetype explicitly recorded.
- [ ] Confirmed baseline summary displayed to user with next command suggestions (`/strategy`, `/advertising`, `/email`, `/content`).
