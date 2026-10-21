---
name: tidyfactor-marketing
description: "Production-grade AI marketing and growth engine with Contextual Decision Layer (CDL) & MENA Intelligence. Handles 7 pillars and 28 capabilities: brand voice, campaign strategy, product launches, SEO pillar-clusters, social media, email lifecycles, paid ads, and copy auditing. Trigger on commands 'brief', 'strategy', 'content', 'social', 'email', 'advertising', 'promotions', 'growth', 'audit', or requests for marketing plans, ad copy, and launch campaigns."
---
# TidyFactor Marketing Engine

A command dispatcher. This file routes marketing and growth intents to corresponding command, workflow, and memory modules with zero procedural execution logic.

## Commands

| User Intent | Command | What It Loads |
|---|---|---|
| **Discovery**: Strategic brief & baseline caching | `references/commands/brief.md` | `references/workflows/brief.md` + `references/memory/decision-points.md` |
| **Strategy**: Brand voice, positioning & launch | `references/commands/strategy.md` | `references/workflows/campaign-launch.md` + `references/memory/frameworks.md` |
| **Content**: SEO pillar-clusters & publishing | `references/commands/content.md` | `references/workflows/content-engine.md` + `references/memory/arabic-writing.md` |
| **Social**: Founder branding & platform playbooks | `references/commands/social.md` | `references/workflows/social-growth.md` + `references/memory/platform-specs.md` |
| **Email**: Welcome, cart recovery & win-back | `references/commands/email.md` | `references/workflows/email-lifecycle.md` + `references/memory/lifecycle-flows.md` |
| **Advertising**: 3-angle copy & CRO wireframes | `references/commands/advertising.md` | `references/workflows/paid-acquisition.md` + `references/memory/ad-copy-templates.md` |
| **Promotions**: Flash sales, decoy pricing & math | `references/commands/promotions.md` | `references/workflows/promo-conversion.md` + `references/memory/promotions-math.md` |
| **Growth**: Referral loops, viral growth & retention | `references/commands/growth.md` | `references/workflows/viral-retention.md` + `references/memory/20-brain-baas-integration.md` |
| **Audit**: Copy quality audit & cliché detection | `references/commands/audit.md` | `scripts/audit_copy.py` + `references/memory/quality-bar.md` |

## Non-Negotiable Quality Constraints

1. **CDL v2.0 & Debate Mode**: Auto-sense parameters before prompting; present genuine Unknowns via `ask_question`.
2. **Zero Robotic Preamble**: Never output conversational monologue dumps, textbook essays, or greetings.
3. **7-Axis Pre-Emit Critique**: All copy must self-audit against P5 H5 E5 S5 R5 V5 D5 (`references/memory/quality-bar.md`).
4. **Multi-Angle Requirement**: Ad generation must produce 3 psychological angles (Pain, ROI, Proof).
5. **Margin Protection Rule**: Promos must verify gross margins with `calc_promo_math.py`.
6. **Bilingual MENA Direct Response**: Compose Arabic copy natively per `references/memory/arabic-writing.md`.

## Anti-Triggers

- Do NOT use for generic text formatting or non-commercial writing.
- Do NOT use for backend database operations or platform infrastructure.

## Tooling Scope (Rule 10)

- `audit_copy` (`scripts/audit_copy.py`): Sub-second AST & cliché linter.
- `calc_promo_math` (`scripts/calc_promo_math.py`): Break-even ROAS & margin math.
- `clean_orphaned_assets` (`scripts/clean_orphaned_assets.py`): SHA-256 duplicate & orphan cleaner.

## Skill vs MCP Boundary (Rule 12)

- **Inside Skill**: Static marketing frameworks, copy matrices, Arabic tone rubrics, and local auditing tools.
- **MCP Layer**: Sovereign Brain persistence (`search_knowledge_base`, `extract_knowledge_item`) operating under Fail-Open protocol.
