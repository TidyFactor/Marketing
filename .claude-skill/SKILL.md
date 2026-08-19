---
name: tidyfactor-marketing
description: Production-grade AI marketing & growth engine following TidyFactor Skill architecture. Handles all 7 marketing pillars and 28 capabilities (Brand Voice & Positioning, Campaign Strategy, Product Launches, SEO Strategy & Pillar-Clusters, Social Media Content, Email Lifecycles, LinkedIn B2B & Founder Personal Branding, Paid Meta/Google Ads, Landing Page Strategy, Promotions/Discounts, Customer Retention & Loyalty Programs, Referral Programs, and Influencer Outreach). Trigger on "brand voice", "positioning statement", "seo strategy", "campaign strategy", "product launch", "social media content", "email campaign", "content calendar", "newsletter strategy", "linkedin b2b", "founder personal branding", "instagram strategy", "tiktok strategy", "social media audit", "first 1000 followers", "hashtag strategy", "grow email list", "welcome email sequence", "abandoned cart emails", "write ad copy", "landing page strategy", "facebook ads", "google ads", "first ad campaign", "plan a sale", "giveaway", "coupon strategy", "customer retention", "loyalty program", "reduce churn", "win-back flow", "referral program", "influencer outreach", "brand awareness", or Arabic equivalents like "خطة تسويقية", "هوية وتموضع العلامة", "استراتيجية السيو", "إطلاق منتج", "تسويق B2B لينكد إن", "محتوى سوشيال ميديا", "حملة بريد إلكتروني", "سلسلة رسائل ترحيبية", "استعادة السلات المتروكة", "كتابة إعلانات", "إعلانات فيسبوك وجوجل", "صفحة هبوط", "خصومات وعروض", "برامج الولاء والاحتفاظ بالعملاء", "برنامج إحالة", "التسويق عبر المؤثرين".
---

# TidyFactor Marketing Engine

A command dispatcher. This file routes marketing and growth intents to the corresponding command, workflow, and memory modules. It holds zero procedural copy or execution logic.

## Commands

| User Intent / Capability | Command | What It Loads |
|---|---|---|
| **Strategy**: Brand voice & positioning statement, Competitive differentiation, Campaign strategy, Product launch plan | `references/commands/strategy.md` | `references/workflows/campaign-launch.md` + `references/memory/frameworks.md` + `references/memory/metrics-benchmarks.md` |
| **Content**: Social media posts, SEO strategy (Pillar + Cluster), Email campaign copy, Content calendar, Newsletter strategy | `references/commands/content.md` | `references/workflows/content-engine.md` + `references/memory/frameworks.md` + `references/memory/platform-specs.md` |
| **Social Media**: LinkedIn B2B & Founder personal branding, Instagram strategy, TikTok strategy, Social media audit, First 1,000 followers, Hashtag strategy | `references/commands/social.md` | `references/workflows/social-growth.md` + `references/memory/platform-specs.md` + `references/memory/frameworks.md` |
| **Email**: Grow email list, Welcome email sequence, Abandoned cart emails, Win-back flows | `references/commands/email.md` | `references/workflows/email-lifecycle.md` + `references/memory/lifecycle-flows.md` + `references/memory/frameworks.md` |
| **Advertising**: Write ad copy, Landing page strategy, Facebook/Meta ads plan, Google Ads plan, First ad campaign | `references/commands/advertising.md` | `references/workflows/paid-acquisition.md` + `references/memory/ad-copy-templates.md` + `references/memory/metrics-benchmarks.md` |
| **Promotions**: Plan a sale / Flash sales, Giveaway or contest, Margin-safe coupon strategy | `references/commands/promotions.md` | `references/workflows/promo-conversion.md` + `references/memory/promotions-math.md` + `references/memory/frameworks.md` |
| **Growth**: Customer retention & churn reduction, Loyalty program design, Referral program, Influencer outreach plan, Brand awareness | `references/commands/growth.md` | `references/workflows/viral-retention.md` + `references/memory/frameworks.md` + `references/memory/metrics-benchmarks.md` |

## Non-Negotiable Quality Constraints

1. **Zero Generic Platitudes**: Every campaign plan, copy variation, or content calendar must contain explicit numerical metrics, testable hooks, psychological angles, and actionable distribution steps.
2. **Multi-Angle Requirement**: All ad copy generation must produce at least 3 distinct psychological angles (Pain/Loss Aversion, Logic/ROI/Efficiency, and Aspiration/Social Proof).
3. **Margin Protection Rule**: Any discounting or promotional strategy must verify unit gross margins and prioritize threshold-based AOV expansion over arbitrary price slashing.
4. **Bilingual Direct Response**: When drafting Arabic copy, use Modern Standard Arabic (فصحى معاصرة رنانة) with natural cultural vernacular, avoiding stiff machine translations or passive voice.
