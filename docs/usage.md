# Build and Release Workflow

## Daily Development

**Workflow:** LaTeX Workshop (James Yu) in VS Code
- Automatically compiles to `build/main.pdf`.
- Real-time preview on save.

**Build:**
```bash
pnpm run build
```

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
