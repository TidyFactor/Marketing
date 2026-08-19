# Command: promotions

Runtime dispatcher for Sales & Seasonal Offers, Pricing Strategy (Decoy Effect & Anchoring), Giveaways/Contests, and Margin-Safe Coupon Strategies.

---

## Capabilities Handled

1. **Pricing Strategy & Packaging**: 3-Tier Good/Better/Best architecture, Decoy Effect positioning, value metrics, annual discount elasticity, and localized BNPL integration (Tabby/Tamara).
2. **Plan a Sale**: 72-hour flash sale blueprints, Black Friday/Cyber Monday execution, tiered cart incentives.
3. **Giveaway or Contest**: Viral contest mechanics, high-converting prize criteria, non-winner consolation funnels.
4. **Coupon Strategy**: Margin erosion calculations, threshold-based discounting (AOV expansion).

---

## What It Loads

- **Workflow**: `../workflows/promo-conversion.md`
- **Memory**: `../memory/promotions-math.md` + `../memory/frameworks.md`

---

## What It Does NOT Load

- Do not load `../workflows/campaign-launch.md` (full product launch strategies belong in `../commands/strategy.md`).
- Do not load `../workflows/viral-retention.md` (referral programs belong in `../commands/growth.md`).
