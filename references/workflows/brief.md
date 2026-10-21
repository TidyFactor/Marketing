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
- Inspect `brand.yaml`, `brand.json`, and `BRAND-GUIDELINES.md` on disk.
- If `track_staleness: true` is configured, verify file hash/mtime against stored snapshot.
- Any decision successfully extracted from local disk is removed from $\text{Unknowns}$.

### 3. Fail-Open MCP Brain Acceleration:
- If unresolved unknowns remain AND `search_knowledge_base` is available:
  - Query `search_knowledge_base(query="marketing persona brand voice", scope="project")`.
  - If a valid marketing KI exists, populate the context and remove from $\text{Unknowns}$.
- **Fail-Open Invariant**: If Brain MCP is unavailable or offline, skip instantly with 0ms delay without warnings.

---

## 💬 Step 1: Interactive Modal Protocol (CDL v2.0)

If $\text{Unknowns} = \emptyset$:
- Display the synthesized 4-line baseline summary.
- Suggest next commands (`/strategy`, `/advertising`, `/email`, `/content`) immediately.

If $\text{Unknowns} \neq \emptyset$:
- **Interactive Wizard Invariant**: Present genuine Unknowns exclusively via the native interactive question tool (`ask_question`). Never dump static text questionnaires or bullet lists in chat.
- **Zero Robotic Preamble**: Forbid greetings or conversational filler.

### Operational Mode Selection:

#### [MODE A] Smart 3-Round Protocol (🎯 الارتجال الذكي المقيد)
Presents structured choices one step at a time via `ask_question`:
1. **Round 1 (Target Market & Regional Nuance)**:
   - `(Recommended) Bilingual / Unified MENA` — Pan-Arab modern standard paired with English tech terminology.
   - `Gulf / GCC (Saudi Arabia 🇸🇦, UAE 🇦🇪, Kuwait 🇰🇼, Qatar 🇶🇦)` — Prestige, trust-first, WhatsApp/Installment framing.
   - `Egypt & Levant (Egypt 🇪🇬, Jordan 🇯🇴)` — Practical ROI, high energy, relatable wit, InstaPay framing.
   - `Global / B2B SaaS` — Direct, metric-dense, self-serve focused, English-first.
2. **Round 2 (Brand Voice Archetype)**:
   - `(Recommended) Authoritative Challenger` — Direct, contrarian, proof-backed, zero-nonsense.
   - `Empathetic Guide` — Supportive, story-driven, transformational, warm.
   - `Elite Luxury / High-End` — Minimalist, aspirational, refined confidence.
   - `High-Energy Direct Response` — Urgent, benefit-stacked, conversion-focused.
3. **Round 3 (Funnel Focus & Core Offer)**:
   - `(Recommended) Bottom-of-Funnel Direct Sale / Promo` — Immediate transaction, launch offer.
   - `Middle-of-Funnel Trial / Demo` — Product-led trial, strategy session.
   - `Top-of-Funnel Lead Magnet` — Free high-value guide, benchmark, audit.

#### [MODE B] Debate Mode (🔥 الاستجواب والمناظرة اللانهائية)
- Activated via `/debate`, explicit user prompt ("مناظرة" / "استجوبني"), or Mode A escalation.
- Relentlessly challenges marketing assumptions, price elasticity, CAC-to-LTV payback periods, and unproven claims.
- Presents binary architectural trade-offs one step at a time via `ask_question`.
- Terminates only upon explicit user trigger (`"END DEBATE"` / `"اعتماد"`), emitting a formal synthesis.

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

2. Format YAML snapshot `.tidyfactor/marketing-brief.snapshot.yaml` for deterministic local staleness tracking (Rule 15).

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
Display a concise summary and suggest the next logical marketing command (`/strategy`, `/advertising`, `/email`, `/content`, `/audit`).

---

## Validation checklist

- [ ] Context Delta Resolution computed prior to prompting user.
- [ ] No questions asked for parameters already discovered on disk.
- [ ] Unknowns presented via native interactive modal tool (`ask_question`).
- [ ] `.tidyfactor/marketing-brief.md` created or verified on disk.
- [ ] Regional calibration (GCC, Egypt, Global) explicitly recorded.
- [ ] Brand voice archetype explicitly recorded.
- [ ] Confirmed baseline summary displayed to user with next command suggestions.
