# Command: promotions

Runtime dispatcher for Flash Sales, Seasonal Promotions, Decoy Pricing Structures, Viral Contests, and Margin-Safe Coupon Strategies.

---

## Capabilities Handled

1. **Plan a Sale / Flash Sales**: 72-hour countdown promotion execution timeline (Teaser, Launch Day, Momentum, Hard Close).
2. **Margin-Safe Coupon Strategy**: Contribution margin safeguards and threshold-based bundling ("Spend $100 Get $15").
3. **Decoy Pricing & Anchoring**: 3-tier Good/Better/Best table design with decoy placement and annual discount framing.
4. **Giveaway / Contest Architecture**: Dream customer niche prizes, viral referral loops, and non-winner consolation offers.

---

## What It Loads

- **Workflow**: `../workflows/promo-conversion.md`
- **Memory**: `../memory/decision-points.md` + `../memory/quality-bar.md` + `../memory/promotions-math.md` + `../memory/frameworks.md`

---

## What It Does NOT Load

- Do not load `../workflows/paid-acquisition.md` (paid ad traffic management is handled by `../commands/advertising.md`).
- Do not load `../workflows/viral-retention.md` (standing affiliate loyalty loops are handled by `../commands/growth.md`).
