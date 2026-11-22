import type { Config } from 'release-it';

export default {
  git: {
    commitMessage: 'chore: release v${version}',
    tagName: 'v${version}',
    requireCleanWorkingDir: true,
    requireBranch: 'main',
    requireUpstream: true,
    push: true,
    commit: true,
    tag: true,
    addUntrackedFiles: true,
  },
  github: {
    release: true,
    releaseName: 'v${version}',
    assets: ['build/document-v*.pdf', 'checksums.txt'],
  },
  npm: {
    publish: false,
  },
  hooks: {
    'before:init': [
      // SPEC-004 §2 guardrail (a): a suffixed package.json.version must fail
      // the release before anything is written.
      `node --input-type=commonjs -e "const v=JSON.parse(require('fs').readFileSync('package.json','utf8')).version;if(!/^\\d+\\.\\d+\\.\\d+$/.test(v)){console.error('before:init: package.json.version must be a clean X.Y.Z, got '+v);process.exit(1)}"`,
    ],
    'after:bump': [
      'pnpm run generate:figures',
      'pnpm exec tsx scripts/build.ts ${version}',
    ],
  },
  plugins: {
    '@release-it/bumper': {
      in: 'package.json',
      out: [
        {
          file: 'CITATION.cff',
          path: 'version',
          type: 'text/yaml',
        },
        {
          file: 'pyproject.toml',
          path: 'project.version',
          type: 'text/toml',
        },
      ],
    },
    '@release-it/conventional-changelog': {
      infile: 'CHANGELOG.md',
      // Canonical Conventional Commits bump mapping, family-wide (the table
      // with an example lives in docs/usage.md §Commits):
      //   `feat!` / `BREAKING CHANGE:` footer -> major
      //   `feat`                              -> minor
      //   `fix`                               -> patch
      //   every other type                    -> NO release
      // `bumpStrict` is the official preset switch for that last row: a type
      // marked `hidden` never recommends a version, so a range holding only
      // docs/chore/test/build/refactor/perf/ci/style/revert (or no commits at
      // all) cuts no release, while `!` and the BREAKING CHANGE/BREAKING-CHANGE
      // footers stay major whatever the type carries. One flag serves both the
      // recommendation and the changelog sections: a hidden type also stays out
      // of CHANGELOG.md (breaking commits are rendered regardless), and the
      // release commit `chore: release v${version}` therefore never triggers
      // the next patch by itself. The table below is the preset's own default
      // type list; `perf` and `revert` are the two entries this family hides
      // beyond those defaults, because only feat/fix release here. A type
      // outside this table (unknown to the convention) still falls back to
      // patch — the preset counts any non-hidden type as a possible fix.
      preset: {
        name: 'conventionalcommits',
        bumpStrict: true,
        types: [
          { type: 'feat', section: 'Features' },
          { type: 'feature', section: 'Features' },
          { type: 'fix', section: 'Bug Fixes' },
          { type: 'perf', section: 'Performance Improvements', hidden: true },
          { type: 'revert', section: 'Reverts', hidden: true },
          { type: 'docs', section: 'Documentation', hidden: true },
          { type: 'style', section: 'Styles', hidden: true },
          { type: 'chore', section: 'Miscellaneous Chores', hidden: true },
          { type: 'refactor', section: 'Code Refactoring', hidden: true },
          { type: 'test', section: 'Tests', hidden: true },
          { type: 'build', section: 'Build System', hidden: true },
          { type: 'ci', section: 'Continuous Integration', hidden: true },
        ],
      },
      tagPrefix: 'v',
    },
  },
} satisfies Config;
