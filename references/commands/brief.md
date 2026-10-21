# Marketing Brief Command (`/brief`)

> **Dispatches to**: `references/workflows/brief.md`
> **Memory Loaded**: `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/frameworks.md`

---

## 🎯 Command Intent
Conducts a rapid, structured discovery protocol to establish strategic parameters (Market, Voice, Funnel Stage, Offer) and writes `.tidyfactor/marketing-brief.md` as the authoritative baseline for all subsequent campaigns, ads, emails, and content generation.

---

## ⚡ Execution Protocol
1. **Delta Auto-Sensing**: Inspect `brand.yaml` and `.tidyfactor/` before prompting the user.
2. **Interactive Modal Wizard (CDL v2.0)**: Present genuine Unknowns exclusively via the native interactive modal tool (`ask_question`). Never dump static chat questionnaires.
3. **Dual Operational Modes**:
   - **Mode A (Smart 3-Round Protocol)**: R1 Market & ICP → R2 Voice & Mechanism → R3 Funnel & Margin Guardrails.
   - **Mode B (Debate Mode — `/debate`)**: Relentlessly stress-tests marketing claims, price elasticity, CAC payback, and competitive moat until explicit user sign-off.
4. **SSOT Persistence**: Save resulting decisions into `.tidyfactor/marketing-brief.md` and `.tidyfactor/marketing-brief.snapshot.yaml`.
