<!-- last-verified: 2026-09-09 -->
# Memory: campaign-mindmap

Mermaid visual architecture illustrating the 7 marketing pillars, audience progression, and conversion loops within the TidyFactor Marketing Engine.

---

## 1. 360° Growth & Pillar Architecture

```mermaid
graph TD
    classDef foundation fill:#0f172a,stroke:#38bdf8,stroke-width:2px,color:#f8fafc;
    classDef topFunnel fill:#1e293b,stroke:#a855f7,stroke-width:2px,color:#f8fafc;
    classDef midFunnel fill:#1e293b,stroke:#eab308,stroke-width:2px,color:#f8fafc;
    classDef bottomFunnel fill:#1e293b,stroke:#22c55e,stroke-width:2px,color:#f8fafc;
    classDef retention fill:#1e293b,stroke:#ec4899,stroke-width:2px,color:#f8fafc;

    subgraph Pillar1["🏛️ Pillar 1: Strategy & Foundation"]
        S1["Brand Positioning & Voice"]
        S2["Competitive Differentiation"]
        S3["Unit Economics & Margin Safety"]
    end
    class S1,S2,S3 foundation;

    subgraph TopOfFunnel["🎯 Acquisition & Traffic (Pillars 2, 3, 5)"]
        C1["Pillar 2: SEO Pillar-Cluster & Guides"]
        SM1["Pillar 3: Social 0-3s Video Hooks & B2B"]
        AD1["Pillar 5: 3-Angle Paid Ads (Pain / ROI / Proof)"]
    end
    class C1,SM1,AD1 topFunnel;

    subgraph MiddleOfFunnel["⚡ Nurturing & Consideration (Pillars 2, 4)"]
        N1["Pillar 2: Educational Newsletter Cadence"]
        E1["Pillar 4: 5-Step Welcome Email Sequence"]
        W1["Landing Page CRO Wireframe"]
    end
    class N1,E1,W1 midFunnel;

    subgraph BottomOfFunnel["💰 Conversion & Transaction (Pillars 5, 6)"]
        PR1["Pillar 6: 72h Flash Sale & Decoy Pricing"]
        AD2["Pillar 5: Retargeting Ads (FOMO / Proof)"]
        E2["Pillar 4: 3-Stage Abandoned Cart Flow"]
    end
    class PR1,AD2,E2 bottomFunnel;

    subgraph RetentionLoop["🔄 Retention & Viral Growth (Pillar 7)"]
        G1["Pillar 7: 2-Sided Viral Referral Program"]
        G2["Pillar 7: Win-Back & Churn Intervention"]
        G3["Pillar 7: VIP Loyalty & Micro-Influencers"]
    end
    class G1,G2,G3 retention;

    %% Data flow connections
    Pillar1 --> TopOfFunnel
    TopOfFunnel --> MiddleOfFunnel
    MiddleOfFunnel --> BottomOfFunnel
    BottomOfFunnel --> RetentionLoop
    RetentionLoop -.->|"Re-invest Margin & Referrals"| TopOfFunnel
```

---

## 2. Lead Journey & Signal Progression

```mermaid
sequenceDiagram
    autonumber
    actor User as Prospect / Visitor
    participant Social as Social & Paid Ads
    participant LP as CRO Landing Page
    participant Email as Email Lifecycle Flow
    participant Cart as Checkout & Payment

    User->>Social: Stops scroll at 0-3s hook (Pain/ROI angle)
    Social->>LP: Clicks standardized UTM link
    LP->>User: Demonstrates mechanism & proof points
    alt Takes Primary Offer
        User->>Cart: Completes checkout with margin-safe offer
    else Leaves without converting
        LP->>Email: Captures lead via high-value lead magnet
        Email->>User: Delivers 5-step nurture sequence
        User->>Cart: Returns via cart recovery or flash sale discount
    end
    Cart->>User: Delivers product + triggers viral referral loop
```
