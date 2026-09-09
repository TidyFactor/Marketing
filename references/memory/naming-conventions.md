<!-- last-verified: 2026-09-09 -->
# Memory: naming-conventions

Standardized naming taxonomy for campaigns, ad groups, UTM tracking parameters, email tags, and marketing assets across the TidyFactor ecosystem.

---

## 1. Universal Campaign Naming Taxonomy

Every paid and organic campaign must follow the deterministic 5-token kebab-case structure:

```text
[GEO]_[OBJECTIVE]_[AUDIENCE]_[OFFER]_[LAUNCH-DATE]
```

### Token Definitions

| Token | Accepted Values | Examples |
|---|---|---|
| `GEO` | Regional or country code | `gcc`, `ksa`, `uae`, `eg`, `global` |
| `OBJECTIVE` | Campaign funnel intent | `tof` (Awareness/Traffic), `mof` (Lead/Consideration), `bof` (Purchase/Conversion), `ret` (Retargeting) |
| `AUDIENCE` | Targeting cluster | `broad`, `lal1-buyers`, `interest-marketing`, `b2b-founders`, `cart-abandoners` |
| `OFFER` | Vehicle or angle descriptor | `flashsale-20`, `free-audit`, `demo-trial`, `starter-bundle` |
| `LAUNCH-DATE` | ISO year-month | `2026-09`, `2026-10` |

### Concrete Examples
- `ksa_bof_lal1-buyers_flashsale-20_2026-09`
- `eg_tof_interest-marketing_free-audit_2026-09`
- `global_mof_b2b-founders_demo-trial_2026-09`

---

## 2. Standardized UTM Parameter Rules

All outbound marketing URLs must include standardized, lowercase, alphanumeric UTM tags:

| Parameter | Construction Rule | Example |
|---|---|---|
| `utm_source` | Platform identifier (lowercase) | `meta`, `google`, `linkedin`, `tiktok`, `email`, `x` |
| `utm_medium` | Channel type | `cpc`, `cpm`, `social-organic`, `newsletter`, `lifecycle` |
| `utm_campaign` | Exact canonical campaign name | `ksa_bof_lal1-buyers_flashsale-20_2026-09` |
| `utm_term` | Target keyword or search intent (paid search only) | `saas-marketing-automation` |
| `utm_content` | Creative variant / angle descriptor | `angle1-pain-video-01`, `angle2-roi-carousel-02` |

### Validation Rule
- **Lowercase Only**: Never use uppercase or spaces in UTM parameters (`utm_source=Meta` ❌ → `utm_source=meta` ✔️).
- **Hyphen Separation**: Separate words with hyphens (`-`), never underscores or `%20` within values.

---

## 3. Creative & Ad Asset Naming

Every creative file, video, or banner asset must be named deterministically:

```text
[ASPECT-RATIO]_[ANGLE]_[FORMAT]_[HOOK-ID]
```

- **Ratios**: `9x16` (Reels/TikTok/Stories), `1x1` (Feed Square), `16x9` (YouTube/Landscape).
- **Angles**: `pain` (Problem-agitate), `roi` (Logic/numbers), `proof` (Social proof/case study).
- **Formats**: `video`, `statichigh`, `carousel`, `ugc`.
- **Examples**:
  - `9x16_pain_ugc_hook01-frustration.mp4`
  - `1x1_roi_statichigh_hook03-benchmark.png`
  - `9x16_proof_video_hook02-beforeafter.mp4`

---

## 4. Email Tagging & Segment Naming

For CRM and email automation engines (Klaviyo, Mailchimp, Loops, Supabase):

- **Lifecycle Flows**: `flow_[stage]_[name]` (e.g., `flow_tof_welcome-series`, `flow_bof_cart-recovery-3step`).
- **One-off Broadcasts**: `camp_[YYYY-MM-DD]_[subject-slug]` (e.g., `camp_2026-09-15_flash-sale-announcement`).
- **User State Tags**: `status:[active|churned|vip|at-risk]`, `market:[gcc|eg|global]`.
