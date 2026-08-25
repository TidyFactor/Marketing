# Marketing Contextual Decision Layer (CDL) — Thin Arbitration Protocol

> **Purpose**: Governs pre-generation marketing elicitation. Resolves strategic, market, and copy ambiguities before campaign or copy emission without generating duplicate memory catalogs or conversational slop.

---

## 🏛️ Marketing Decision Matrix (M1 – M5)

When a marketing workflow begins and the request contains ambiguous parameters, the agent arbitrates across 5 standardized decision points:

| ID | Decision Dimension | Reference SSOT Catalog | Conservative Default |
|:---|:---|:---|:---|
| **M1** | **Target Market & Regional Calibration** | `memory/frameworks.md` & `platform-specs.md` | `Bilingual / MENA-Ready (GCC + Egypt)` |
| **M2** | **Brand Voice Archetype & Tone** | `memory/frameworks.md` | `Authoritative Challenger (Direct, ROI-backed)` |
| **M3** | **Funnel Stage & User Sophistication** | `memory/lifecycle-flows.md` & `ad-copy-templates.md` | `Middle-of-Funnel (Solution-Aware)` |
| **M4** | **Conversion Model & Core Offer** | `memory/promotions-math.md` & `frameworks.md` | `Value-First / Discovery Call / Freemium` |
| **M5** | **Output Density & Asset Depth** | `memory/frameworks.md` | `Full Campaign Blueprint (Multi-Channel)` |

---

## 🚦 Deterministic Boolean Skip Conditions

The agent MUST skip asking questions and proceed directly to execution when any of the following conditions evaluate to `true`:

```text
1. Cached Brief Exists         → .tidyfactor/marketing-brief.md exists on disk
2. Explicit Dimension in Prompt → User prompt explicitly specifies Region, Tone, Audience, or Offer
3. Direct Command Invocation   → User called specific sub-command (e.g. /email, /advertising, /promotions)
4. Copy Refresh / Optimization → Existing copy or campaign is provided for iterative rewrite
5. Fast-Track Flag             → User appended --yes, -y, or "do not ask questions"
```

---

## 🎯 Direct Invocation vs. Refresh Invariants

1. **Direct Invocation Invariant**: When a user explicitly runs `/advertising`, `/email`, `/promotions`, or `/strategy`, the agent skips general discovery and uses targeted command parameters immediately.
2. **Zero-Regression Copy Refresh Bias**: When auditing, refreshing, or rewriting existing campaigns, the agent silently preserves the established brand voice, regional calibration, and offer economics unless an overhaul is explicitly requested.

---

## ⚡ Single-Round Batching & Priority Hierarchy

If multiple marketing dimensions remain ambiguous and no skip condition is met:

1. **Maximum Questions**: Present at most **3 focused questions in a single round**. Never conduct multi-round interrogations.
2. **Strict Priority Hierarchy**:
   $$\mathbf{M1 \text{ (Region/Market)}} > \mathbf{M2 \text{ (Brand Voice)}} > \mathbf{M3 \text{ (Funnel Stage)}} > \mathbf{M4 \text{ (Offer)}} > \mathbf{M5 \text{ (Depth)}}$$
3. **Priority Overflow**: If more than 3 dimensions are unknown, ask M1, M2, and M3; resolve M4 and M5 silently using the **Conservative Defaults**.

---

## 🛑 Terminal Hard-Stop Contract

When presenting decision options to the user, the agent MUST end its turn immediately and await user selection. It MUST NOT output partial marketing plans, draft placeholder copy, or speculate on unconfirmed choices in the same turn.

---

## 💾 Brief Persistence Schema (`.tidyfactor/marketing-brief.md`)

When `/brief` runs or decisions are confirmed, save them to `.tidyfactor/marketing-brief.md`:

```markdown
# Marketing Brief Baseline

- **Product / Brand**: [Name]
- **Target Market (M1)**: [MENA-GCC | MENA-Egypt | Global-US]
- **Brand Voice (M2)**: [Authoritative Challenger | Empathetic Guide | Luxury Premium | Direct Response]
- **Funnel Stage (M3)**: [Problem-Aware | Solution-Aware | Product-Aware / Most Aware]
- **Core Offer (M4)**: [Lead Magnet | Free Trial | Discovery Call | Direct Transaction]
- **Deliverable Scope (M5)**: [Sprint Copy | Full Campaign Blueprint]
- **Last Updated**: [YYYY-MM-DD]
```
