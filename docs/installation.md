# Installation and Requirements

## Prerequisites

1. **[Node.js](https://nodejs.org/) 20+ & [pnpm](https://pnpm.io/) 9+**
   - Required for the release pipeline and TypeScript orchestration scripts.

2. **[Docker](https://www.docker.com/)**
   - Required for the reproducible LaTeX build process.
   - Image: `kjarosh/latex:2024.4-full` (downloaded automatically).

3. **[uv](https://github.com/astral-sh/uv)** *(optional)*
   - Python package manager, only needed if the project includes numerical verification or figure generation.

## Setup

```bash
git clone https://github.com/omega-pcf/<repo>.git
cd <repo>
pnpm install
```

## Build

```bash
pnpm run build          # Compile PDF via Docker
pnpm run release        # Full release (version bump + build + GitHub + Zenodo)
pnpm run release:dry-run # Dry-run, no changes
```
