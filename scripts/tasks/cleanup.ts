import { rmSync, existsSync, mkdirSync, readdirSync } from 'fs';

export function cleanupOldVersions(buildDir: string): void {
  if (!existsSync(buildDir)) {
    mkdirSync(buildDir, { recursive: true });
    return;
  }

  // Remove old versioned PDFs (document-v*.pdf) before nuking the dir
  const files = readdirSync(buildDir);
  const oldPdfs = files.filter(f =>
    f.startsWith('document-v') && f.endsWith('.pdf')
  );

  if (oldPdfs.length > 0) {
    console.log(`\n🧹 Cleaning up ${oldPdfs.length} old PDF version(s)...`);
    for (const pdf of oldPdfs) {
      console.log(`  ✓ Removed ${pdf}`);
    }
  }

  // Nuke the entire build/ directory recursively. This is critical because
  // hyperref writes .out files with UTF-16 encoding that, if stale, cause
  // "File ended while scanning use of \@newl@bel / \@BOOKMARK" on the next
  // run. A shallow readdirSync cleanup misses files in subdirectories
  // (e.g. build/src/*.aux from \input chapters).
  rmSync(buildDir, { recursive: true, force: true });
  mkdirSync(buildDir, { recursive: true });
}
