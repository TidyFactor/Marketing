# Contributing to TidyFactor Marketing

Thank you for your interest in contributing to **TidyFactor Marketing**!

---

## 🏛️ Development Philosophy & Invariants

All contributions must respect the **TidyFactor Skill Methodology**:

1. **SKILL.md is a Dispatcher**: Zero inline procedural instructions; routes to commands, workflows, and memory.
2. **One Workflow = One Outcome**: Every workflow must end with a strict `## Validation Checklist`.
3. **Operational Memory**: Memory files must strictly house formulas, tables, templates, and metrics.
4. **Anti-Cliché Rule**: Banish generic marketing fluff. Every sentence must carry a mechanism or a verifiable number.
5. **Bilingual Direct Response**: Parity between English and Modern Standard Arabic copy.

---

## 🛠️ Local Development & Testing

1. Clone or navigate to the repository:
   ```bash
   cd tidyfactor-marketing
   ```
2. Test CLI commands locally:
   ```bash
   node bin/create-kit.js
   node bin/add-skill.js
   ```
3. Run structural compliance audit:
   ```bash
   python scratch/deep_audit_marketing_skill.py
   ```

---

## 📝 Pull Request Guidelines

1. Create a feature branch: `git checkout -b feature/your-feature-name`.
2. Commit your changes with clear, semantic commit messages.
3. Ensure all file path references resolve cleanly (0 broken links).
4. Update `CHANGELOG.md` with your additions.
5. Submit a Pull Request targeting the `main` branch.
