# Project Documentation

This directory contains technical documentation for the shared build and release pipeline.

## Structure

```
docs/
├── README.md          # This file
├── architecture.md    # Release system architecture
├── installation.md    # Prerequisites and setup
└── usage.md           # Build and release commands
```

## Contents

- **architecture.md**: Tech stack, execution flow, reproducibility measures, scripts structure.
- **installation.md**: Prerequisites and setup instructions.
- **usage.md**: Daily workflow, conventional commits, build and release commands.

## Conventions

All commits follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<scope>): <description>
```

**Common types:** `feat`, `fix`, `docs`, `refactor`, `chore`.
