# Contributing

Keep each change tied to a concrete learning outcome. Use docs/TUTORIAL_TEMPLATE.md.

- Use synthetic or explicitly publishable data only.
- Record exact tested versions and official sources; distinguish proposals from executed results.
- Keep examples isolated. Do not add model credentials, mandatory paid APIs or broad framework dependencies to the baseline.
- Test failure paths and no-evidence outcomes, not just successful output.
- Run `python3 -m unittest discover -s tests -v` and `git diff --check`.
- Review relative Markdown links and all example commands after changing paths.
- Put new runnable projects in appropriately scoped directories or separate repositories. Do not copy proprietary source.

English is the canonical teaching language. Update docs/en first and synchronize material technical corrections in docs/zh-Hant; mark any untranslated changes. Do not claim cross-version support from syntax inspection alone.
