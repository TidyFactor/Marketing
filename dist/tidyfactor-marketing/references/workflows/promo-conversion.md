# Workflow: promo-conversion

One outcome: A profitable seasonal or flash sale plan, Decoy Effect pricing structure, a viral contest/giveaway architecture, or a margin-safe discount and coupon strategy.

---

## Execution Steps

### 0. CDL Marketing Brief Resolution
1. Check `.tidyfactor/marketing-brief.md`. If present, adopt established target market (M1), voice archetype (M2), and conversion model (M4).
2. If absent and user prompt contains ambiguous parameters, run thin arbitration from `../memory/decision-points.md` (single-round batching, max 3 questions).
3. If skip conditions apply, proceed immediately with conservative defaults.

### 1. Margin Safeguard & Discount Math
Using `../memory/promotions-math.md`:
- Input Product Price ($) and Unit Cost / COGS ($) to determine Gross Margin %.
- Calculate the maximum allowable discount that maintains positive net contribution.
- If margin is < 40%, route away from flat percentage discounts to **Threshold Bundling** (e.g. "Spend $100 Get $15") or **Value-Add Free Bonuses**.

### 2. Pricing Architecture & Psychological Anchoring
Using `../memory/frameworks.md`:
- Structure 3-Tier Good/Better/Best pricing table.
- Implement the **Decoy Effect**: Position the middle tier as the irresistible target by making the lower tier slightly less attractive and the top tier the high-anchor enterprise tier.
- Frame annual billing with a 15-20% discount ("Get 2 Months Free").
- If MENA market: Add localized BNPL installment messaging ("Split into 4 interest-free payments of X SAR/AED with Tabby/Tamara").

### 3. 72-Hour Flash Sale & Seasonal Promotion Execution Plan
Structure the promotional timeline:
- **T-3 Days (Pre-Announcement Teaser)**: VIP early-access signup with exclusive bonus for first 50 buyers.
- **Day 1 (Hour 0 - Launch Blitz)**: Main launch email broadcast + top banner on website + retargeting ad surge.
- **Day 2 (Hour 24 - Momentum & FAQs)**: Social proof highlights + answers to common questions.
- **Day 3 (Hour 48 - Last Chance / Hard Close)**: 3-part urgency email cadence (Morning, Afternoon, 2-Hours-Left) + countdown timer banner.

### 4. Viral Giveaway & Contest Architecture
Design a high-ROI contest:
- **Niche-Specific Prize**: Value proposition tailored exclusively to ideal customers (not generic electronics/cash).
- **Entry Funnel**: Verified email signup (1 entry) -> Redirect to Thank-You Page with unique viral referral link.
- **Viral Gamification**: +5 entries per friend who joins through referral link.
- **Non-Winner Conversion Offer**: On announcement day, deliver a surprise 48-hour voucher to all non-winning participants.

### 5. Pre-Emit Quality Self-Critique
Before emitting pricing, promotions, or sale mechanics, evaluate against all 7 axes from `../memory/quality-bar.md` and stamp:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```

---

## Validation Checklist

- [ ] CDL brief parameters resolved from `.tidyfactor/marketing-brief.md` or prompt defaults
- [ ] Discount structure verified against gross margins to prevent profit erosion
- [ ] Decoy Effect and price anchoring applied to 3-tier pricing setups
- [ ] 72-hour promotional calendar contains hourly triggers for email, web banners, and ads
- [ ] Giveaway prize is strictly relevant to dream customer avatar
- [ ] Non-winner consolation offer included in contest design
- [ ] Expiration deadlines and urgency mechanisms are explicit and realistic
- [ ] 7-Axis Quality Stamp included with scores >= 4/5
