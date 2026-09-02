<!-- last-verified: 2026-09-02 -->
# Brain MCP & Sovereign BaaS Marketing Integration Contract

Authoritative operational specification governing how `tidyfactor-marketing` integrates with self-hosted `tidyfactor-brain` MCP instances and sovereign agency nodes without creating hard dependencies or blocking offline workflows.

---

## 🏛️ 1. Sovereign Architecture Model (Self-Hosted Primacy)

TidyFactor Marketing operates on a **Sovereign, Self-Hosted Architecture**:
- **Zero Centralized SaaS Dependency**: `tidyfactor-brain` and its MCP server run locally on the developer's machine or on an agency's self-hosted server instance.
- **Tenant Definition**: A `tenant` represents an isolated client or brand workspace (e.g. `tenant_alwkala`, `tenant_client_a`) mapped to a dedicated SQLite file (`data/tenants/{tenant_id}_brain.sqlite`) or scoped local knowledge directory (`~/.gemini/knowledge/projects/{project_id}/`).
- **No Global Auth Overhead**: Local stdio connections run authentication-free. Remote self-hosted nodes use static bearer tokens configured in `mcp_config.json`.

---

## ⚡ 2. The Deterministic Fail-Open Contract

Brain MCP is strictly an **optional acceleration layer**, NEVER a required runtime dependency.

### Strict Resolution Algorithm:

```
Step 1: Check Local Disk Workspace
        ├── IF `BRAND-GUIDELINES.md` or `.tidyfactor/marketing-brief.md` exists:
        │   └── LOAD directly from disk without asking questions. Done.
        └── ELSE: Proceed to Step 2.

Step 2: Check Active MCP Toolset Availability
        ├── IF tool `search_knowledge_base` is present in agent's active tool list:
        │   ├── Execute: `search_knowledge_base(query="marketing persona brand voice", scope="project", project_id=CURRENT_PROJECT)`
        │   ├── IF valid marketing KI returned:
        │   │   └── POPULATE context baseline immediately. Done.
        │   └── ELSE (Empty/Error):
        │       └── Silent fallback (0ms delay) to Step 3.
        └── ELSE (Tool not registered / Standalone environment / Offline):
            └── Silent fallback (0ms delay) to Step 3.

Step 3: Interactive Micro-Discovery (CDL 3-Question Dialogue)
        └── Present concise, structured A/B/C/D choices to the user. Zero conversational preamble. Done.
```

### Invariants:
1. **Zero Robotic Preamble**: Never output introductory greetings like *"أهلاً بك بصفتي محرك التسويق..."* or ask the user whether a brief exists on disk.
2. **Instant Silent Bypass**: If MCP is unavailable or errors, proceed immediately to the 3-question interview without delay or error messages.

---

## 📦 3. Marketing Strategy Knowledge Item (KI) Contract

When exporting marketing baselines via explicit `--sync-brain` flag on `/brief` or `/strategy`, the deliverable formats as an Atomic KI conforming to the following JSON payload:

```json
{
  "schema_version": "1.0.0",
  "ki_type": "marketing_strategy_baseline",
  "project_id": "current-project-slug",
  "timestamp": "2026-09-02T06:00:00Z",
  "persona": {
    "target_market": "GCC|Egypt|Levant|Global_B2B|Bilingual_MENA",
    "voice_archetype": "authoritative_challenger|empathetic_guide|elite_luxury|direct_response",
    "funnel_stage": "top_of_funnel|middle_of_funnel|bottom_of_funnel",
    "core_offer": "lead_magnet|trial_demo|direct_sale",
    "primary_conversion_channel": "whatsapp|direct_checkout|strategy_call|instapay"
  },
  "trust_signals": [
    "cash_on_delivery",
    "installments_tabby_tamara",
    "official_cr_tax_id"
  ],
  "artifacts": [
    ".tidyfactor/marketing-brief.md",
    "copy/campaign-strategy.md"
  ]
}
```

---

## 🛠️ 4. Tooling Execution Bridge (`run_skill_tool`)

When `tidyfactor-brain` executes `tidyfactor-marketing` scripts via `manifest.json`:

| Tool Name | Script Entrypoint | Latency Class | Execution Mode |
|---|---|---|---|
| `audit_copy` | `scripts/audit_copy.py` | Sub-second (<100ms) | Direct CLI / Text AST & Cliché Linter |
| `calc_promo_math` | `scripts/calc_promo_math.py` | Sub-second (<50ms) | Deterministic Profit & ROAS Calculator |

---
