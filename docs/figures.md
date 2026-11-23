# Figures

This manuscript generates no figures. No `images/` directory is tracked, and
`pnpm run figures` answers that there is nothing to regenerate; the
`pnpm run generate:figures` entry point (`scripts/figures/main.py`) is there
for auditing only.

The measured inventory is the `images.files` counter of the generated ledger
[`counts.md`](counts.md), and the pipeline row that records the decision is
row 7 (Figures) of [`architecture.md`](architecture.md). With no figure there
is no caption, generator or determinism contract to document in this
repository; those rules belong to the siblings that do ship figures.
