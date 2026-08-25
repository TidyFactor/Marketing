# Workflow: email-lifecycle

One outcome: A complete email list growth blueprint, 5-part welcome onboarding sequence, 3-stage abandoned cart recovery flow, or broadcast email campaign.

---

## Execution Steps

### 0. CDL Marketing Brief Resolution
1. Check `.tidyfactor/marketing-brief.md`. If present, adopt established target market (M1), voice archetype (M2), and funnel stage (M3).
2. If absent and user prompt contains ambiguous parameters, run thin arbitration from `../memory/decision-points.md` (single-round batching, max 3 questions).
3. If skip conditions apply, proceed immediately with conservative defaults.

### 1. List Growth & Lead Magnet Engineering
Define the lead capture mechanism:
- **Lead Magnet Format**: Specific checklist, cheat sheet, calculator, mini-course, or discount voucher (must deliver immediate win in under 10 minutes).
- **Opt-in Form Copy**: Headline focused on the outcome, 2 bullet points of what's inside, single low-friction form field (Email only).
- **Placement Strategy**: Sticky header bar, inline blog callout, exit-intent popup (triggered on mouse leave or 60s dwell time).

### 2. 5-Part Welcome & Indoctrination Drip Sequence
Using `../memory/lifecycle-flows.md` and `../memory/frameworks.md`, draft full copy for each email:
- **Email 1 (Day 0 - Immediate)**: Delivery + Whitelist instruction + Expectation setting.
- **Email 2 (Day 1 - 24h)**: Origin Story & Epiphany Bridge (Building emotional connection).
- **Email 3 (Day 2 - 48h)**: Paradigm Shift / Myth Busting (Overcoming internal objections).
- **Email 4 (Day 3 - 72h)**: Case Study & Proof (Overcoming external objections).
- **Email 5 (Day 4 - 96h)**: The Invitation / Fast-Action Offer with Urgency.

### 3. 3-Stage Abandoned Cart Recovery (E-Commerce / Digital Offer)
Draft the 3 sequential messages:
- **Stage 1 (1 Hour)**: Helpful Customer Care & Cart Link (No discount).
- **Stage 2 (24 Hours)**: Top 3 Customer Testimonials + FAQs & Guarantee.
- **Stage 3 (48 Hours)**: Expiring 10% Discount Code or Free Bonus Gift + Deadline Countdown.

### 4. Broadcast Campaign (Promotions / Newsletters)
For one-off announcements or sales:
- Structure copy using PAS or BAB.
- Implement urgency triggers (closing date/time).

### 5. Pre-Emit Quality Self-Critique
Before emitting the final email copy or flows, evaluate against all 7 axes from `../memory/quality-bar.md` and stamp:
```markdown
/* Pre-emit critique: P5 H5 E5 S5 R5 V5 D5 */
```

---

## Validation Checklist

- [ ] CDL brief parameters resolved from `.tidyfactor/marketing-brief.md` or prompt defaults
- [ ] Lead magnet promises a specific, actionable win achievable in < 10 minutes
- [ ] Every email includes 3 distinct subject line options (Curiosity, Direct, Urgency)
- [ ] Delay intervals and triggers explicitly specified for every automated step
- [ ] Mobile-optimized layout with short paragraphs (1-3 sentences) and distinct button/text CTAs
- [ ] Cart recovery flow escalates logically from support -> social proof -> discount urgency
- [ ] 7-Axis Quality Stamp included with scores >= 4/5
