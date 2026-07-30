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
