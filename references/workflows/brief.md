# Marketing Discovery & Brief Workflow

> **Outcome**: Generates an authoritative `.tidyfactor/marketing-brief.md` file capturing target market, brand voice, funnel stage, conversion model, and delivery scope.

---

## 📋 Step 0: Local Workspace Auto-Sensing First

1. Scan workspace for `BRAND-GUIDELINES.md`, `brand.json`, `.tidyfactor/marketing-brief.md`, and project files.
2. If present, immediately extract brand voice, target audience, and conversion baseline without asking questions.
3. If `.tidyfactor/marketing-brief.md` already exists and user did not specify `--force` or `--reset`:
   - Display a concise 4-line baseline summary.
   - Suggest next action (`/strategy`, `/advertising`, `/email`, `/content`).

---

## ⚡ Step 0.5: Check Active MCP Acceleration (Fail-Open Fallback)

1. If local files do not exist AND `search_knowledge_base` is available in active agent tools:
   - Query `search_knowledge_base(query="marketing persona brand voice", scope="project")`.
   - If a valid marketing KI is returned, populate the context baseline immediately.
2. **Fail-Open Policy**: If MCP is unavailable, offline, or returns empty:
   - Silently and instantly proceed to Step 1 with 0ms delay. Never show connection warnings or error logs.

---

## 💬 Step 1: Conduct Structured Micro-Discovery (Zero Robotic Preamble)

> **Anti-Bot Invariant**: Strictly forbid bot persona greetings (*"أهلاً بك بصفتي..."*) or asking whether files exist. Present structured A/B/C/D options directly:

### Question 1: Target Market & Regional Tone (M1)
- **(A) Gulf / GCC (Saudi Arabia 🇸🇦, UAE 🇦🇪, Kuwait 🇰🇼, Qatar 🇶🇦)** — High prestige, trust-first, WhatsApp/Installments framing, modern polished Arabic.
- **(B) Egypt & Levant (Egypt 🇪🇬, Jordan 🇯🇴)** — Practical ROI, high energy, relatable wit, cash-on-delivery & InstaPay framing.
- **(C) Global / B2B SaaS** — Direct, metric-dense, self-serve focused, English-first.
- **(D) Bilingual / Unified MENA** (Default).

### Question 2: Brand Voice Archetype (M2)
- **(A) Authoritative Challenger** (Direct, contrarian, proof-backed, no-nonsense).
- **(B) Empathetic Guide** (Supportive, story-driven, transformational, warm).
- **(C) Elite Luxury / High-End** (Minimalist, aspirational, refined confidence).
- **(D) High-Energy Direct Response** (Urgent, benefit-stacked, conversion-focused).

### Question 3: Funnel Focus & Core Offer (M3 + M4)
- **(A) Top-of-Funnel Lead Magnet** (Free guide, checklist, audit, quiz).
- **(B) Middle-of-Funnel Trial / Demo** (Product-led trial, 1-on-1 strategy call).
- **(C) Bottom-of-Funnel Direct Sale / Promo** (E-commerce purchase, limited-time launch offer).

---

## 💾 Step 2: Persist Baseline & Optional Brain Sync

1. Format and write `.tidyfactor/marketing-brief.md`:
```markdown
# Marketing Brief Baseline

- **Product / Brand**: [Extracted or Confirmed Name]
- **Target Market (M1)**: [Confirmed Selection]
- **Brand Voice (M2)**: [Confirmed Archetype]
- **Funnel Stage (M3)**: [Top / Middle / Bottom]
- **Core Offer (M4)**: [Lead Magnet / Trial / Direct Transaction]
- **Deliverable Scope (M5)**: [Sprint Copy / Multi-Channel Blueprint]
- **Last Updated**: [Current Date]
```

2. **Optional Brain Sync (`--sync-brain`)**:
   - When invoked with `--sync-brain`, format the deliverable as an Atomic KI per `20-brain-baas-integration.md` and export to local Brain MCP via `extract_knowledge_item`.
   - If Brain MCP is offline, complete local file generation without failing.

---

## 🎯 Step 3: Self-Critique & Actionable Summary

Stamp the 7-axis critique:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```
Display a concise summary and suggest the next logical marketing command (`/strategy`, `/advertising`, `/email`, `/content`).

---

## ## Validation checklist

- [ ] `.tidyfactor/marketing-brief.md` created or verified on disk.
- [ ] Exactly 3 or fewer questions asked in a single round.
- [ ] Regional calibration (GCC, Egypt, Global) explicitly recorded.
- [ ] Brand voice archetype explicitly recorded.
- [ ] Confirmed baseline summary displayed to user with next command suggestions (`/strategy`, `/advertising`, `/email`, `/content`).
