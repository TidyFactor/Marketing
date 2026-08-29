---
name: tidyfactor-marketing
description: "Production-grade AI marketing and growth engine with Contextual Decision Layer (CDL) & MENA Intelligence. Handles 7 pillars and 28 capabilities: brand voice, campaign strategy, product launches, SEO pillar-clusters, social media, email lifecycles, and paid ads. Trigger on commands 'brief', 'strategy', 'content', 'social', 'email', 'advertising', 'promotions', 'growth', or requests for marketing plans, ad copy, and launch campaigns."
---
# TidyFactor Marketing Engine

A command dispatcher. This file routes marketing and growth intents to the corresponding command, workflow, and memory modules. It holds zero procedural copy or execution logic.

## Commands

| User Intent / Capability | Command | What It Loads |
|---|---|---|
| **Discovery**: Pre-flight marketing brief, strategic alignment, market baseline caching | `references/commands/brief.md` | `references/workflows/brief.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` |
| **Strategy**: Brand voice & positioning statement, Competitive differentiation, Campaign strategy, Product launch plan | `references/commands/strategy.md` | `references/workflows/campaign-launch.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/frameworks.md` + `references/memory/arabic-writing.md` |
| **Content**: Social media posts, SEO strategy (Pillar + Cluster), Content calendar, Newsletter strategy | `references/commands/content.md` | `references/workflows/content-engine.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/frameworks.md` + `references/memory/arabic-writing.md` |
| **Social Media**: LinkedIn B2B & Founder personal branding, Instagram strategy, TikTok strategy, Social media audit | `references/commands/social.md` | `references/workflows/social-growth.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/platform-specs.md` |
| **Email**: Grow email list, Welcome email sequence, Abandoned cart emails, Win-back flows | `references/commands/email.md` | `references/workflows/email-lifecycle.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/lifecycle-flows.md` + `references/memory/arabic-writing.md` |
| **Advertising**: Write ad copy, Landing page strategy, Facebook/Meta ads plan, Google Ads plan, First ad campaign | `references/commands/advertising.md` | `references/workflows/paid-acquisition.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/ad-copy-templates.md` + `references/memory/arabic-writing.md` |
| **Promotions**: Plan a sale / Flash sales, Giveaway or contest, Margin-safe coupon strategy, Decoy pricing | `references/commands/promotions.md` | `references/workflows/promo-conversion.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/promotions-math.md` |
| **Growth**: Customer retention & churn reduction, Loyalty program design, Referral program, Influencer outreach | `references/commands/growth.md` | `references/workflows/viral-retention.md` + `references/memory/decision-points.md` + `references/memory/quality-bar.md` + `references/memory/frameworks.md` |

## Non-Negotiable Quality Constraints

1. **Contextual Decision Layer (CDL)**: Resolve regional, voice, and offer baseline via `.tidyfactor/marketing-brief.md` or thin protocol in `references/memory/decision-points.md` before generating campaigns.
2. **7-Axis Pre-Emit Self-Critique (`P/H/E/S/R/V/D`)**: All output must self-audit against Pain Specificity, Hook Power, Execution, Stage Fit, Restraint, Voice, and Decision Alignment (`quality-bar.md`).
3. **Multi-Angle Requirement**: All ad copy generation must produce at least 3 distinct psychological angles (Pain/Loss Aversion, Logic/ROI/Efficiency, and Aspiration/Social Proof).
4. **Margin Protection Rule**: Any discounting or promotional strategy must verify unit gross margins and prioritize threshold-based AOV expansion over arbitrary price slashing.
5. **Bilingual Direct Response & Native Arabic**: Compose Arabic copy natively per `arabic-writing.md` using Modern Standard Arabic (فصحى معاصرة رنانة) or calibrated regional dialects without mechanical translation artifacts.
6. **MENA Platform & Trust Calibration**: Adhere to country-specific platform rankings, trust signals, and payment methods (`platform-specs.md`).

