# AGENTS.md — TidyFactor Marketing Engine (`tidyfactor-marketing`)

Production-grade **Direct-Response Marketing & Growth Engine** following the strict **TidyFactor Skill Methodology**. Handles all 7 marketing pillars and 28 capabilities with zero fluff, data-backed metrics, quantitative benchmarks, and platform-native conversion frameworks.

---

## ⚡ Skill & 7 Core Command Dispatchers (28 Capabilities)

This project exposes an Agentic Skill under `SKILL.md` (and `.claude-skill/SKILL.md`). The following 7 command modules covering all 28 capabilities are supported:

| Pillar | Command | Purpose | Reference Spec |
|---|---|---|---|
| **1. Strategy** | `strategy` | Brand Voice & Positioning Statement, Competitive Differentiation, Campaign Strategy, Product Launch Plan (T-30 to T+14) | `references/commands/strategy.md` |
| **2. Content** | `content` | Social Media Posts, SEO Pillar + Cluster Architecture, Email Campaigns, Content Calendar, Newsletters | `references/commands/content.md` |
| **3. Social Media** | `social` | LinkedIn B2B & Founder Personal Branding, Instagram, TikTok 0-3s Hooks, Profile Audits, First 1,000 Followers, Hashtags | `references/commands/social.md` |
| **4. Email** | `email` | Lead Magnet Mechanics, 5-Email Welcome Flow, 3-Stage Cart Recovery, 30/60/90-Day Win-Back Sequences | `references/commands/email.md` |
| **5. Advertising** | `advertising` | 3-Angle Ad Copy Matrices, 7-Dimension CRO Landing Page Wireframes, Meta Ads, Google RSA Ads, First Test Campaign | `references/commands/advertising.md` |
| **6. Promotions** | `promotions` | 72-Hour Flash Sales, 3-Tier Decoy Pricing, Viral Giveaways/Contests, Margin-Safe Coupon Strategy | `references/commands/promotions.md` |
| **7. Growth** | `growth` | Retention & Churn Reduction Diagnosis, Loyalty Program Design (Points/Tiers/Perks), 2-Sided Referral Loops, Influencer Outreach, Brand Awareness | `references/commands/growth.md` |

---

## 🛠️ CLI Execution Modes

- **Interactive Setup Wizard** (`npx @tidyfactor/cli-marketing`): Launches interactive terminal setup prompting developers for project niche, primary channel focus, and target market (Global vs MENA).
- **Skill Injection Mode** (`npx @tidyfactor/cli-marketing add-skill`): Injects `.agents/skills/tidyfactor-marketing/` directly into any target repository.
- **AI Agent Non-Interactive Mode**: Claude, Antigravity, Cursor, and Windsurf execute slash commands directly via `references/commands/<name>.md`.

---

## 🛡️ Critical Marketing Guardrails (Non-Negotiable)

1. **Anti-Cliché Rule**:
   - Zero generic fluff phrases ("cutting-edge", "seamless experience", "نسعى دائماً لتقديم الأفضل").
   - Every adjective must be replaced by a concrete number, mechanism, or proof point.
2. **Multi-Angle Ad Copy**:
   - Every ad copy generation produces at least 3 distinct psychological angles (Loss Aversion, Logic/ROI/Efficiency, and Aspiration/Status).
3. **Margin Protection & Decoy Pricing**:
   - Never discount without verifying unit gross margins. Anchor 3-tier pricing around a clear target option.
4. **Bilingual & Cultural Native**:
   - Full support for Modern Standard Arabic (فصحى معاصرة رنانة) and English direct-response copywriting.
