#!/usr/bin/env tsx
import { readFileSync, writeFileSync } from 'fs';
import { syncCitationMetadata } from './tasks/citation.js';
import { syncSelfCitations, injectDevVersion } from './tasks/selfcitations.js';
import { cleanupOldVersions } from './tasks/cleanup.js';
import { compilePDF } from './tasks/compile.js';
import { generateChecksums } from './tasks/checksums.js';
import type { ReleaseConfig } from './types.js';

function createReleaseConfig(version: string): ReleaseConfig {
  return {
    version,
    buildDir: 'build',
    sourceTex: 'main.tex',
    outputPdf: `build/document-v${version}.pdf`,
    checksumsFile: 'checksums.txt',
  };
}

async function main(): Promise<void> {
  // Version from the command line argument (provided by release-it) or package.json.
  // The RAW argument picks the tier of the token *rendered into the PDF*
  // (SPEC-004 §2 as amended): with it the release build prints `vX.Y.Z`,
  // without it a development build prints `vX.Y.Z-dev@<sha>` — so the
  // package.json fallback must not be passed down.  Either way the committed
  // main.tex keeps its clean token; the suffix is injected and restored below.
  const releaseVersion = process.argv[2];
  let version = releaseVersion;

  if (!version) {
    const packageJsonPath = new URL('../package.json', import.meta.url);
    const packageJson = JSON.parse(await import('fs').then(m => m.promises.readFile(packageJsonPath, 'utf8')));
    version = packageJson.version;
  }

  if (!version) {
    console.error('Error: Version not provided and not found in package.json');
    process.exit(1);
  }

  const config = createReleaseConfig(version);

  try {
    console.log(`\n🔨 Building release artifacts for v${version}...\n`);

    cleanupOldVersions(config.buildDir);
    syncCitationMetadata(config.version);
    syncSelfCitations();

    // SPEC-004 §2 (amended 2026-11-20): the committed main.tex keeps the clean
    // `vX.Y.Z` token; the development form lives only in the rendered PDF.
    // Inject -> render -> restore, and the restore comes from the bytes read
    // here, never from `git checkout`, so a failing compile cannot leave a
    // suffixed token behind.
    const originalTex = readFileSync(config.sourceTex, 'utf8');
    writeFileSync(config.sourceTex, injectDevVersion(originalTex, releaseVersion));
    try {
      compilePDF(config);
    } finally {
      writeFileSync(config.sourceTex, originalTex);
    }
    generateChecksums(config);

    console.log(`\n✅ Build completed successfully for v${version}\n`);
    console.log(`Generated files:`);
    console.log(`  - ${config.outputPdf}`);
    console.log(`  - ${config.checksumsFile}`);
    console.log(`  - CITATION.cff (updated)`);
    console.log(`  - .zenodo.json (generated from CITATION.cff)`);
    console.log(`  - README.md (self-citation regions regenerated)\n`);
  } catch (error) {
    console.error(`\n❌ Build failed:`, error);
    process.exit(1);
  }
}

main().catch((error) => {
  console.error('Fatal error:', error);
  process.exit(1);
});

