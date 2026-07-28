import { readdirSync, unlinkSync, existsSync, mkdirSync } from 'fs';
import { join } from 'path';

export function cleanupOldVersions(buildDir: string): void {
  if (!existsSync(buildDir)) {
    mkdirSync(buildDir, { recursive: true });
    return;
  }

  const files = readdirSync(buildDir);

  // Remove old versioned PDFs (document-v*.pdf)
  const oldPdfs = files.filter(f =>
    f.startsWith('document-v') && f.endsWith('.pdf')
  );

  if (oldPdfs.length > 0) {
    console.log(`\n🧹 Cleaning up ${oldPdfs.length} old PDF version(s)...`);
    for (const pdf of oldPdfs) {
      const pdfPath = join(buildDir, pdf);
      try {
        unlinkSync(pdfPath);
        console.log(`  ✓ Removed ${pdf}`);
      } catch (error) {
        console.warn(`  ⚠ Failed to remove ${pdf}:`, error);
      }
    }
  }

  // Remove stale LaTeX build artifacts so biber doesn't inherit
  // a malformed .bcf from a previous failed pdflatex run.
  const staleExtensions = [
    '.aux', '.bcf', '.bbl', '.blg', '.log', '.out',
    '.toc', '.run.xml', '.fls', '.fdb_latexmk',
    '.synctex.gz', '.pdf',
  ];
  const stale = files.filter(f => staleExtensions.some(ext => f.endsWith(ext)));

  if (stale.length > 0) {
    console.log(`🧹 Removing ${stale.length} stale build artifact(s)...`);
    for (const f of stale) {
      try {
        unlinkSync(join(buildDir, f));
      } catch { /* best-effort */ }
    }
  }
}
