# Architecture

## Stack

- **release-it**: Semantic versioning + GitHub releases.
- **@release-it/bumper**: Synchronizes version `package.json` → `CITATION.cff`.
- **TypeScript + tsx**: Orchestration scripts (build, metadata generation).
- **Docker** (`kjarosh/latex:2024.4-full`): Reproducible LaTeX compilation via `latexmk`.
- **Native Metadata Sync**: Generates `.zenodo.json` from `CITATION.cff` directly.
- **Zenodo webhook**: Automatic integration from GitHub.

## Flow

```
pnpm run release
  → @release-it/bumper: updates version in package.json, CITATION.cff

  → after:bump:
    → pnpm run build: orchestration script
      → cleanup: removes previous document-v*.pdf
      → citation: updates date-released, generates .bib and .zenodo.json
      → compile: Docker latexmk with SOURCE_DATE_EPOCH (git commit timestamp)
      → checksums: SHA256 of the PDF

  → Git: commit + tag v${version} + push

  → GitHub: Release with assets (PDF, checksums)

  → Zenodo: automatic webhook → new version + DOI
```

## Reproducibility

**SOURCE_DATE_EPOCH:** Extracted from `git log -1 --pretty=%ct`.

**LaTeX primitives:** `\pdfinfoomitdate=1`, `\pdftrailerid{}`, etc. (see `main.tex`).

**Docker pinned:** `kjarosh/latex:2024.4-full` (explicit version).

Same commit = same PDF hash (guaranteed).

## Structure

```
scripts/
├── build.ts              # Independent build (hook after:bump)
├── tasks/                # Atomic tasks
│   ├── checksums.ts
│   ├── citation.ts       # CITATION.cff and .zenodo.json logic
│   ├── cleanup.ts
│   └── compile.ts
├── types.ts              # TypeScript types
└── utils/
    └── git.ts            # Git utilities (getCommitEpoch)
```

## Metadata

**Source of truth:** `package.json` version for the build, `CITATION.cff` for project metadata.

**Automatic Synchronization:**
- `CITATION.cff` version (via @release-it/bumper).
- `CITATION.cff` date-released (via build.ts).
- `CITATION.cff` languages (source of truth for Zenodo).
- `.zenodo.json` version and content (generated from `CITATION.cff` via Native Sync).

**Zenodo:** Reads `.zenodo.json` from the tag, creates a version under the same Concept DOI.

## Sources of truth

Every generated file has exactly one editable origin: edit the origin, run
`pnpm run build`, and a hand edit of a derived file is overwritten by the
next build. This table states where each chain **starts** and what it
**writes**; the detail behind row 8 lives in [`usage.md`](usage.md)
§Counts, behind row 9 in [`usage.md`](usage.md) §Shared files, and the
release side of rows 4–6 lives in [`usage.md`](usage.md)
§Versioning — it links it instead of repeating it.

| # | Chain | Source of truth (edit here) | Generator | Derived — never edit |
|---|---|---|---|---|
| 1 | Citation records | `citation.csl.json`, one hand-written record per `\bibitem` | `scripts/tasks/citation.ts` | `src/bibliography.bib` (keys renamed to the CSL ids) |
| 2 | Title, abstract, keywords, DOI | `package.json` — `description`, `metadata.abstract`, `keywords`, `metadata.doi` | `citation.ts` `syncCff`: `if (pkg.description) cff.title = pkg.description` | `CITATION.cff` `title`/`abstract`/`keywords`/`doi`, then `.zenodo.json` `title`/`description` |
| 3 | Citation identity and references | `CITATION.cff` — `authors`, `license`, `repository-code` (the identity root); its `references` come from row 1 | `citation.ts` reads the CFF, overwrites only `version`, `date-released`, `title`, `abstract`, `keywords` and `doi`, and rebuilds `references` from `citation.csl.json` via citation-js | `.zenodo.json` (rebuilt from the CFF) |
| 4 | README self-citation regions | `CITATION.cff` + `package.json` `metadata.citationKey` | `scripts/tasks/selfcitations.ts` (idempotent: `f(f(x)) = f(x)`) | the `badge` and `citation` regions of `README.md` |
| 5 | Printed version | `package.json` `version`, clean `X.Y.Z` | `selfcitations.ts` writes the token between the `id="version"` markers of `main.tex`; `scripts/build.ts` injects `vX.Y.Z-dev@<shortsha>` for the render and restores the source bytes; `@release-it/bumper` copies the value on release | `CITATION.cff` `version`, `pyproject.toml` `project.version`, the `Version:` token of the page-1 footnote |
| 6 | Dates | the commit (`git log -1 --pretty=%ct`) read in the project's fixed zone | `scripts/utils/git.ts` → `SOURCE_DATE_EPOCH` plus `TZ=CST6` for latexmk in Docker; `citation.ts` pins `process.env.TZ = 'CST6'` and formats with `todayInProjectZone()` | `CITATION.cff` `date-released`, `.zenodo.json` `publication_date`, the `\today` of the PDF |
| 7 | Figures | — (this repository commits no figure: no `images/` directory is tracked) | `pnpm run generate:figures` (`uv run python scripts/figures/main.py`), for auditing only; the `pnpm run figures` alias refuses to run while `images/` carries tracked files | nothing: no figure is tracked, so no artifact can go stale |
| 8 | Counts | the measurements of the working tree (no editable origin: the Lean sources with comments stripped, the `images/` inventory) | `scripts/tasks/counts.ts` (idempotent: `f(f(x)) = f(x)`) — `pnpm run counts`, `pnpm run counts:check` inside `validate`, and `build.ts` `syncCounts()` before every render | `docs/counts.md` — this repository states no count in its prose, so it carries no marked region |
| 9 | Shared files | `scripts/shared-files.json` — the family's byte-identity manifest: every file the five repositories must carry unchanged, pinned with its SHA-256 (SPEC-004 §3) | `scripts/tasks/manifest.ts` — `pnpm run manifest` rewrites the hashes from the working tree, `pnpm run manifest:check` runs inside `validate` after `counts:check` | the pinned hashes themselves; a listed file edited in one repository only fails `manifest:check`, naming the file and both digests |

**A title change belongs in `package.json`, not in the CFF.** Row 2 runs on
every build, so an edit of the `title` of `CITATION.cff` survives only until
the next `pnpm run build` overwrites it from `description`. The identity
fields are the opposite: `authors`, `license` and `repository-code` are read
from the CFF and never written back, so they are edited there by hand.

**Why `CST6`.** Both date writers must stamp the project's own calendar day
(UTC−06:00): `toISOString()` is UTC by definition, so a build started after
18:00 local would write tomorrow's date into `CITATION.cff` and
`.zenodo.json`, and the Docker build image carries no
`/usr/share/zoneinfo`, so a named zone such as `America/Mexico_City` would
silently fall back to UTC. POSIX `CST6` is a fixed offset needing no zone
database, which is why `compile.ts` passes `-e TZ=CST6` to latexmk and
`citation.ts` sets the same value in-process. Reference dates parsed from
`citation.csl.json` deliberately stay on the UTC path: they are date-only
strings anchored at UTC midnight, and moving them to the project zone would
shift every reference by a day.

**No test writes a figure.** The verification entrypoint of this repository
(`pnpm run verify:py`) asserts numbers, never figure bytes, and no figure is
tracked by contract — a figure would enter through the pipeline of row 7,
never through a test.
