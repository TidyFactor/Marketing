# Test Scenarios: tidyfactor-marketing

Comprehensive evaluation scenarios validating deterministic command dispatch, Contextual Decision Layer auto-sensing, Arabic direct-response generation, margin math protection, and automated copy linting.

---

## Scenario 1: E-Commerce 72-Hour Flash Sale with Margin Guardrails (GCC / KSA 🇸🇦)

### Objective
Generate a margin-safe promotional strategy and high-urgency WhatsApp/Instagram copy for a Saudi Arabian DTC brand launching a 72-hour flash sale.

### Inputs & Context
- **Product**: Leather Travel Bag
- **Price**: 400 SAR, **COGS**: 120 SAR, **Proposed Discount**: 25% (100 SAR off)
- **Target Market**: Saudi Arabia (Riyadh, Jeddah)
- **Channel**: WhatsApp Broadcast + Instagram Story Ads (9:16)

### Expected Execution & Checks
1. **Margin Safety Gate**: `calc_promo_math.py` confirms:
   - Discounted Price: 300 SAR
   - Net Gross Margin: 60% (>30% threshold)
   - Status: `SAFE_TO_RUN`
2. **Copy Generation**:
   - High-urgency hook without slop (`"أطلق العنان"` ❌ forbidden).
   - Trust and payment framing: Mada, Tabby, Tamara 4-installment split.
   - 7-axis pre-emit critique stamp included.

---

## Scenario 2: B2B Multi-Tenant SaaS Phased Launch (Global / English)

### Objective
Formulate a complete T-30 to T+14 launch sequence, positioning statement, and competitive differentiation for an AI agent observability tool.

### Inputs & Context
- **Product**: AgentTrace (Observability for AI Coding Agents)
- **Pricing**: $49/seat/month
- **Primary Moat**: Zero-runtime latency, SQLite-native trace indexing.

### Expected Execution & Checks
1. **Positioning Matrix**: Formulates statement: *For [engineering leaders] who [struggle with invisible agent regressions], [AgentTrace] is an [observability engine] that [indexes traces locally in SQLite with 0ms runtime overhead] unlike [Datadog/LangSmith]*.
2. **Phased Roadmap**:
   - T-30 to T-15: Technical teardown blogs and waitlist alpha.
   - T-14 to T-1: Private beta with 50 design partners.
   - T-0: Product Hunt, Hacker News Show HN, and Twitter thread.
   - T+1 to T+14: Onboarding case studies and customer referral loop.
3. **Checklist Validation**: Workflow satisfies 100% of `references/workflows/campaign-launch.md` checklist.

---

## Scenario 3: 3-Stage Abandoned Cart Recovery Sequence (Egypt 🇪🇬)

### Objective
Build a culturally calibrated 3-email abandoned cart recovery flow for an Egyptian fashion brand utilizing local payment incentives (InstaPay, Cash on Delivery).

### Inputs & Context
- **Market**: Egypt (Cairo, Alexandria)
- **Currency**: EGP
- **Average Order Value**: 850 EGP
- **Tone**: Friendly, relatable, solution-oriented Egyptian Arabic.

### Expected Execution & Checks
1. **Flow Structure**:
   - Email 1 (1 hour post-abandonment): Gentle reminder, photo of cart items, customer service WhatsApp link.
   - Email 2 (24 hours post-abandonment): Overcoming objections, sizing guide, InstaPay instant discount.
   - Email 3 (48 hours post-abandonment): Final urgency notice, reserving items for 12 hours.
2. **Quality Bar**: Free of generic translation artifacts; utilizes authentic Egyptian phrasing with clear CTAs.

---

## Scenario 4: Direct-Response Ad Copy Multi-Angle Audit

### Objective
Generate 3 distinct psychological ad copy angles (Pain, ROI, Proof) and verify zero AI marketing clichés via automated linter.

### Inputs & Context
- **Offer**: Fast-track web performance audit service.
- **Audience**: Agency owners and e-commerce founders.

### Expected Execution & Checks
1. **Angles Emitted**:
   - Angle 1 (Pain): Frustration of paying high Meta ad spend while 60% bounce on slow mobile pages.
   - Angle 2 (ROI/Logic): Every 100ms speed improvement raises conversion rate by 1.1%, recovering lost ad spend.
   - Angle 3 (Social Proof): Before/after case study showing Lighthouse score 34 → 98 and 2.4x ROAS increase.
2. **Linter Execution**:
   - Runs `python scripts/audit_copy.py target.md --json`.
   - Result: `passed: true`, `score: 100`, zero banned clichés detected.
