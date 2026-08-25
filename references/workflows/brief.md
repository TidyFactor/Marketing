# Marketing Discovery & Brief Workflow

> **Outcome**: Generates an authoritative `.tidyfactor/marketing-brief.md` file capturing target market, brand voice, funnel stage, conversion model, and delivery scope.

---

## 📋 Step 0: Check Existing Baseline

1. Check if `.tidyfactor/marketing-brief.md` already exists on disk.
2. If it exists and user did not specify `--force` or `--reset`:
   - Display the active brief summary.
   - Ask if the user wants to keep the existing baseline or update specific parameters.

---

## 💬 Step 1: Conduct 3-Question Targeted Discovery

If no baseline exists, present at most 3 clear, structured questions in a single turn:

### Question 1: Target Market & Regional Tone (M1)
- **A) Gulf / GCC (Saudi Arabia 🇸🇦, UAE 🇦🇪, Kuwait 🇰🇼, Qatar 🇶🇦)** — High prestige, trust-first, WhatsApp/Installments framing, modern polished Arabic.
- **B) Egypt & Levant (Egypt 🇪🇬, Jordan 🇯🇴)** — Practical ROI, high energy, relatable wit, cash-on-delivery & InstaPay framing.
- **C) Global / B2B SaaS** — Direct, metric-dense, self-serve focused, English-first.
- **D) Bilingual / Unified MENA** (Default).

### Question 2: Brand Voice Archetype (M2)
- **A) Authoritative Challenger** (Direct, contrarian, proof-backed, no-nonsense).
- **B) Empathetic Guide** (Supportive, story-driven, transformational, warm).
- **C) Elite Luxury / High-End** (Minimalist, aspirational, refined confidence).
- **D) High-Energy Direct Response** (Urgent, benefit-stacked, conversion-focused).

### Question 3: Funnel Focus & Core Offer (M3 + M4)
- **A) Top-of-Funnel Lead Magnet** (Free guide, checklist, audit, quiz).
- **B) Middle-of-Funnel Trial / Demo** (Product-led trial, 1-on-1 strategy call).
- **C) Bottom-of-Funnel Direct Sale / Promo** (E-commerce purchase, limited-time launch offer).

---

## 💾 Step 2: Write `.tidyfactor/marketing-brief.md`

Format and persist the confirmed choices:

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

---

## 🎯 Step 3: Self-Critique & Handoff

Stamp the 7-axis critique:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```

---

## ## Validation checklist

- [ ] `.tidyfactor/marketing-brief.md` created or verified on disk.
- [ ] Exactly 3 or fewer questions asked in a single round.
- [ ] Regional calibration (GCC, Egypt, Global) explicitly recorded.
- [ ] Brand voice archetype explicitly recorded.
- [ ] Confirmed baseline summary displayed to user with next command suggestions (`/strategy`, `/advertising`, `/email`, `/content`).
