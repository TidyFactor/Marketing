# Changelog - TidyFactor Marketing

All notable changes to the **[@tidyfactor/marketing](https://www.npmjs.com/package/@tidyfactor/marketing)** package will be documented in this file.

## [1.4.0] - 2026-09-02

### 🧠 Added — Sovereign Brain MCP Integration, Copy Auditor & Fail-Open Protocol
- **Brain Integration Contract (`references/memory/20-brain-baas-integration.md`)**: Operational specification defining sovereign self-hosted architecture, isolated client SQLite database scoping, and Marketing Strategy Knowledge Item (KI) payload schemas.
- **Fail-Open Resolution Protocol (`references/workflows/brief.md`)**: Embedded deterministic context discovery: (1) Local workspace auto-sensing first, (2) Optional Brain MCP context acceleration (`search_knowledge_base`) when active, (3) Instant 0ms silent fallback to 3-question structured interview with zero robotic preamble.
- **Runtime Tooling Manifest & Quality Engine (`manifest.json`)**: Declared portable `audit_copy` and `calc_promo_math` tools with schema validation for direct CLI and MCP `run_skill_tool` execution.
- **Automated Copy Quality Auditor (`scripts/audit_copy.py`)**: Standalone and MCP-compatible CLI engine scanning copy for AI cliches, banned fluff, and 7-axis pre-emit critique stamps.
- **Unit Economics & Margin Calculator (`scripts/calc_promo_math.py`)**: Deterministic calculations for gross margin safety, break-even ROAS targets, and discount compression.
- **Anti-Triggers & Tooling Scope**: Enriched `SKILL.md` with explicit Rule 10 Tooling Scope and anti-triggers.

---

## [1.3.0] - 2026-08-29

### Added - Arabic Direct-Response & MENA Intelligence Engine
- **Arabic Direct-Response Engineering (`memory/arabic-writing.md`)**: Linguistic frameworks, active voice rules, Idafa constructs, and dialectical tone calibration for Egypt, Gulf/Saudi Arabia, Libya, and Pan-Arab markets without mechanical translation artifacts.
- **MENA Trust & Platform Calibration (`memory/platform-specs.md`)**: Integrated per-country platform prioritization (Meta, Snapchat, TikTok, X, Instagram, WhatsApp) and local payment conversion gateways (InstaPay, Fawry, Mada, Tabby, Tamara, KNET, CliQ).
- **Anti-Slop Arabic Cliché Banishment**: Replaced empty promotional phrases with falsifiable, quantified outcomes and testable hooks.
- **7-Badge Standard Ecosystem Suite (`style=for-the-badge`)**: Upgraded documentation headers to unified 7-badge matrix with Skills-LAB and universal AI Agent compatibility.

## [1.2.0] - 2026-08-29

### Added - Global Multi-Tier & Multi-Language Documentation Architecture
- **Rule 13 Implementation**: Two-tier documentation separation between Canonical Technical Documentation (`README.md` SSOT) and First-Class Market Localizations.
- **Universal Multi-Language Switcher**: Standardized 8-language switcher navigation bar across all documentation files (`EN`, `AR`, `FA`, `ES`, `PT`, `ZH`, `DE`, `FR`).
- **First-Class Localized Developer Adoption Guides**: `README.es.md`, `README.pt.md`, `README.fa.md`, `README.zh.md`, `README.de.md`, `README.fr.md`.
- **Automated Validation & Packaging**: Updated `tools/build-skill.js` and `tools/validate_skill.py`.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-08-25

### Fixed
- **Rule 9 Frontmatter Constraint Compliance**: Refactored `SKILL.md` frontmatter `description` down to 415 characters (well within Claude's 1024-character/byte upload ceiling) following the concise "what + when" pattern.
- **Claude & IDE Autocomplete Compatibility**: Wrapped YAML description in valid double quotes with single-quoted triggers, preventing parse exceptions during skill upload on Claude Web / Anthropic platform and Antigravity IDE.

---

## [1.1.0] - 2026-08-25

### Added
- **Contextual Decision Layer (CDL v1.0)**: Added `references/memory/decision-points.md` defining a thin arbitration protocol for resolving strategic marketing ambiguities (M1–M5: Market, Voice, Funnel Stage, Offer, Scope) before campaign emission.
- **Marketing Brief Command (`/brief`)**: Added `references/commands/brief.md` and `references/workflows/brief.md` for pre-flight discovery interviews and caching baseline decisions in `.tidyfactor/marketing-brief.md`.
- **Single-Round Batching & Priority Overflow**: Codified strict single-round batching (max 3 questions) with priority hierarchy (`M1 > M2 > M3 > M4 > M5`) and auto-conservative defaults for silent downstream execution.
- **Direct Invocation & Zero-Regression Invariants**: Guaranteed that explicit command calls (`/strategy`, `/content`, `/advertising`, `/email`) present full options directly, while copy refresh workflows silently preserve established brand baselines.
- **7-Axis Pre-Emit Self-Critique (`P/H/E/S/R/V/D`)**: Expanded pre-emit quality gate with Axis 7 (`D` - Decision Alignment) in `references/memory/quality-bar.md` and across all 7 workflows.
- **Automated Validation & Build Suite**: Added `tools/validate_skill.py` and `tools/build-skill.js` with cross-agent synchronization across all target environments.

---

## [1.0.0] - 2026-08-18

### 🚀 Initial Production Release
- **7 Core Pillars & 28 Capabilities**: Strategy, Content & SEO, Social & B2B LinkedIn, Email Lifecycles, Paid Advertising & CRO, Promotions & Decoy Pricing, and Retention & Growth.
- **12 Psychological Mental Models of Persuasion**: Anchoring, Decoy Effect, Loss Aversion, Zeigarnik Effect, Goal Gradient, Social Proof Stacking, and Scarcity.
- **Anti-Cliché Replacement Engine**: Strict ban on 12 English & Arabic filler phrases with mandatory mechanism replacement rule.
- **MENA Regional Intelligence & Payment Gateways**: Platform rankings and payment benchmarks for KSA, UAE, Egypt, Kuwait, Qatar, Jordan, and Morocco.
- **7-Dimension CRO Audit & ICE Experiment Scoring**: 5-second clarity testing, CTA friction diagnosis, and scientific hypothesis scoring ($\text{Impact} \times \text{Confidence} \times \text{Ease}$).
- **Bilingual Native Support**: Modern Standard Arabic (فصحى معاصرة رنانة) and English direct-response parity.
- **Dual Deployment & Agent Integration**: CLI wizard, `.agents/skills/`, `.claude-skill/`, and IDE-wide global config.
