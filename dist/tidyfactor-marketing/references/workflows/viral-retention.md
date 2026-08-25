# Workflow: viral-retention

One outcome: A complete customer retention diagnosis, loyalty program design (points/tiers/perks), 2-sided customer referral program, influencer outreach campaign, or brand awareness distribution engine.

---

## Execution Steps

### 0. CDL Marketing Brief Resolution
1. Check `.tidyfactor/marketing-brief.md`. If present, adopt established target market (M1), voice archetype (M2), and conversion model (M4).
2. If absent and user prompt contains ambiguous parameters, run thin arbitration from `../memory/decision-points.md` (single-round batching, max 3 questions).
3. If skip conditions apply, proceed immediately with conservative defaults.

### 1. Customer Retention & Drop-Off Diagnosis
Diagnose retention friction before designing loyalty incentives:
- **SaaS / Subscription**: Diagnose time-to-first-value (onboarding "aha moment"), feature adoption drop-offs, and pre-renewal disengagement signals.
- **E-Commerce / Retail**: Identify post-first-purchase drop-offs, lack of re-order triggers, and competitor price sensitivity.
- **Service Businesses**: Address post-project check-in cadence, retainer transitions, and client relationship health.

### 2. Loyalty Program Architecture (Matching Business Model)
Select the optimal loyalty model:
- **Points / Rewards**: For high-frequency, low-AOV purchases (retail, food, consumable goods).
- **Tiered Status**: For businesses with a clear VIP heavy-user segment (Bronze / Silver / Gold).
- **Perks-Based (No-Points)**: For early-stage brands and boutique SaaS (exclusive early access, free priority support/shipping, private community).
- **Cashback / Store Credit**: Cleanest, lowest friction for general digital stores.

### 3. Two-Sided Viral Referral Program Architecture
Structure a self-sustaining referral loop:
- **Incentive Structure (Give $X, Get $Y)**:
  - *Inviter Reward*: $20 store credit / 1 free month / cash payout after referred friend's first purchase.
  - *Invitee Reward*: 15% discount on their first order / extended 30-day trial.
- **Trigger Touchpoints**: Post-purchase thank you page, positive NPS survey email (+7 to +14 days), inside user account dashboard.
- **Gamified Milestones**: Unlock bonus tier rewards at 3, 5, and 10 successful referrals.

### 4. Influencer Vetting & Cold Outreach Campaign
Structure an influencer partnership pipeline:
- **Vetting Criteria Scorecard**: Engagement Rate > 3.0%, comment authenticity, audience demographic alignment.
- **Outreach Scripts (DM & Email)**: Personalized compliment on recent post + 1-sentence value proposition + zero-friction initial ask (gifting/sample).
- **Compensation & Tracking**: Dedicated discount code (e.g. `INFLUENCER10`) + UTM tracking link.

### 5. Brand Awareness & Organic Distribution Engine
- **Podcast & Media Pitching**: 3 contrarian angles showcasing unique case studies.
- **Co-Marketing**: Joint webinars, bundle drops, or newsletter swaps with complementary non-competing brands.
- **Content Repurposing Flywheel**: 1 core long-form asset -> 5 short-form clips + 3 text posts + 1 newsletter.

### 6. Pre-Emit Quality Self-Critique
Before emitting loyalty programs, referral systems, or outreach scripts, evaluate against all 7 axes from `../memory/quality-bar.md` and stamp:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```

---

## Validation Checklist

- [ ] CDL brief parameters resolved from `.tidyfactor/marketing-brief.md` or prompt defaults
- [ ] Retention drop-off point diagnosed before prescribing loyalty mechanics
- [ ] Loyalty model explicitly matches business model (Points vs Tiers vs Perks)
- [ ] Referral loop defines concrete incentives for both the referrer and the new referee
- [ ] Referral placement points mapped across customer journey (post-purchase, email, app dashboard)
- [ ] Influencer vetting scorecard includes quantitative engagement and audience authenticity checks
- [ ] Tracking mechanisms (UTMs, custom affiliate promo codes) defined for attribution
- [ ] 7-Axis Quality Stamp included with scores >= 4/5
