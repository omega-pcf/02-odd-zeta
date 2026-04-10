import { readdirSync, unlinkSync, existsSync } from 'fs';
import { join } from 'path';

export function cleanupOldVersions(buildDir: string): void {
  if (!existsSync(buildDir)) {
    return;
  }
  
  const files = readdirSync(buildDir);
  const oldPdfs = files.filter(f => 
    f.startsWith('document-v') && f.endsWith('.pdf')
  );
  
  if (oldPdfs.length === 0) {
    return;
  }
  
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

