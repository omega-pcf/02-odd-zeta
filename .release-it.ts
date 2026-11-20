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
    // No especificar autoGenerate ni releaseNotes
    // release-it automáticamente usa context.changelog del plugin
    // que contiene solo los cambios de la versión actual
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
      'pnpm exec tsx scripts/build.ts ${version}',
    ],
    // Generate figures first, then generate .zenodo.json from CITATION.cff,
    // then build PDF with correct version number
    // release-it automatically does `git add . --update` before commit
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
        // .zenodo.json is now generated from CITATION.cff via cffconvert
        // in scripts/tasks/citation.ts, so we don't update it here
      ],
    },
    '@release-it/conventional-changelog': {
      infile: 'CHANGELOG.md',
      preset: {
        name: 'conventionalcommits',
        types: [
          { type: 'feat', section: 'Features' },
          { type: 'fix', section: 'Bug Fixes' },
          { type: 'style', section: 'Styles' },
          { type: 'docs', section: 'Documentation' },
          { type: 'refactor', section: 'Refinements' },
          { type: 'perf', section: 'Performance Improvements' },
          { type: 'chore', section: 'Chores' },
          { type: 'build', section: 'Build System' },
          { type: 'release', section: 'Releases' },
        ],
      },
      tagPrefix: 'v',
    },
  },
} satisfies Config;

