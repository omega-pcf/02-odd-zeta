import { execSync } from 'child_process';
import { writeFileSync, existsSync } from 'fs';
import type { ReleaseConfig } from '../types.js';

export function generateChecksums(config: ReleaseConfig): void {
  const { outputPdf, checksumsFile } = config;
  
  if (!existsSync(outputPdf)) {
    throw new Error(`PDF file not found: ${outputPdf}`);
  }
  
  const hash = execSync(`sha256sum ${outputPdf}`, { encoding: 'utf8' });
  writeFileSync(checksumsFile, hash);
  console.log(`✓ Generated ${checksumsFile}`);
}

