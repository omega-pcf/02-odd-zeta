# Build and Release Workflow

## Daily Development

**Workflow:** LaTeX Workshop (James Yu) in VS Code
- Automatically compiles to `build/main.pdf`.
- Real-time preview on save.

**Build:**
```bash
pnpm run build
```

## Counts

The numbers the documentation states about the repository are **measured,
never typed** (family mechanism ported from `05-kkgt`, whose `CVR-001` §5
named the stale counts): this repository states no count in its prose — it
commits no figures and its manuscript carries no `\testref{...}` anchor — so
its ledger reports the Lean source statistics of the one library
`lean/lakefile.toml` declares and the `images/` inventory, and it carries no
marked region.

```bash
pnpm run counts         # rewrite the marked regions and regenerate docs/counts.md
pnpm run counts:check   # fail, with a diff, when either has drifted
```

`counts:check` runs inside `validate`, after `parity`. The mechanism follows
the `selfcitations` precedent (the family SPEC-001 §5.2): a region is delimited
by `<!-- counts:begin id="..." -->` … `<!-- counts:end id="..." -->` in prose,
and by `# counts:begin id="..."` … `# counts:end id="..."` on lines of their
own inside a code fence, where an HTML comment would print as text. Should a
future document state a count, the region is added next to the claim and the
task owns it from then on.

Dated documents are snapshots of a moment: they are corrected by hand with
the reason recorded, never rewritten by the task.

## Commits

All commits follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```

**Common types:** `feat`, `fix`, `docs`, `refactor`, `chore`.

**Examples:**
```bash
git commit -m "fix(build): resolve Docker bind-mount race condition"
git commit -m "feat(citation): add ORCID support"
git commit -m "docs: update architecture guide"
```

**Automatic Changelog:** The `@release-it/conventional-changelog` plugin generates `CHANGELOG.md` from conventional commits on each release.

## Versioning

- **Standard:** [Semantic Versioning](https://semver.org) — `vX.Y.Z`
  (major.minor.patch), where `feat` → minor, `fix` → patch,
  `BREAKING CHANGE`/`!` → major, as declared in the commit subjects above.
- **Single source:** the `version` field of `package.json`.
- **Synchronization chain:** `release-it` bumps `package.json` →
  `@release-it/bumper` writes the same value into `CITATION.cff` →
  `citation.ts` regenerates `.zenodo.json` from the CFF → the GitHub release
  carries the tag → **Zenodo archives exactly this version** under the
  repository's Concept DOI (one DOI per version, one Concept DOI for all of
  them). Zenodo therefore consumes the same string the repository declares;
  the pipeline detail lives in [architecture.md](architecture.md), and the
  row-by-row chain (source → generator → derived file) in
  [architecture.md §Sources of truth](architecture.md#sources-of-truth).
- **The paper prints it.** The page-1 footnote of the family is standardised
  as:

  ```latex
  \renewcommand{\datename}{\textbf{Received:}}
  \date{<Month D, YYYY>; \textbf{Last modified:} \today; \textbf{Version:} \texttt{vX.Y.Z}}
  ```

  which renders `Received: <Month D, YYYY>; Last modified: <today>; Version:
  vX.Y.Z.` — with only the identifier in monospace: the labels stay
  `\textbf`, `Version: ` itself is not typed, and the token sits inside
  `\texttt{…}`. The first label lives in `\datename` because amsart prefixes
  the footnote with it (its own default would read `Date: Received: …`). The
  version token mirrors the `version` field of `package.json` (v1.7.2), so
  the printed version, the committed version and the version archived by
  Zenodo cannot diverge; `pnpm run selfcitations:check` (and `parity`) fails
  when the token sits outside `\texttt{…}`, and `pnpm run selfcitations`
  wraps it back.

## Release

```bash
pnpm run release         # Full release: bump → build → tag → GitHub → Zenodo
pnpm run release:dry-run # Preview without changes
```

## Installation

```bash
pnpm install
```

**Requirements:** Node.js 20+, pnpm 9+, Docker.
