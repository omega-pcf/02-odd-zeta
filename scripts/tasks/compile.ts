import { execSync, spawnSync } from 'child_process';
import { existsSync, mkdirSync, readFileSync, renameSync } from 'fs';
import { getCommitEpoch } from '../utils/git.js';
import type { ReleaseConfig } from '../types.js';

const DOCKER_IMAGE = 'kjarosh/latex:2024.4-full';

const DOCKER_TEX_ENV = [
  '-e TEXMFDIST=/opt/texlive/texmf-dist',
  '-e TEXMFHOME=/dev/null',
  '-e TEXMFLOCAL=/opt/texlive/texmf-local',
  '-e TEXMFSYSCONFIG=/opt/texlive/texmf-config',
  '-e TEXMFSYSVAR=/opt/texlive/texmf-var',
].join(' ');

export function compilePDF(config: ReleaseConfig): void {
  const { sourceTex, outputPdf } = config;
  const commitEpoch = getCommitEpoch();

  console.log(`\n📄 Compiling PDF with SOURCE_DATE_EPOCH=${commitEpoch}...`);
  mkdirSync('build', { recursive: true });

  console.log('  Running latexmk in Docker...');
  const cwd = process.cwd();

  const args = [
    'run', '--rm',
    '-v', `${cwd}:${cwd}`,
    '-w', cwd,
    '-e', `SOURCE_DATE_EPOCH=${commitEpoch}`,
    '-e', 'LC_ALL=C',
    '-e', 'LANG=C',
    '-e', 'TZ=UTC',
    ...DOCKER_TEX_ENV.split(' '),
    DOCKER_IMAGE,
    'latexmk', '-pdf', '-interaction=nonstopmode', '-quiet', sourceTex,
  ];

  const result = spawnSync('docker', args, {
    stdio: 'pipe',
    encoding: 'utf8',
    maxBuffer: 10 * 1024 * 1024,
  });

  if (result.stdout) process.stdout.write(result.stdout);
  if (result.stderr) process.stderr.write(result.stderr);

  const baseName = sourceTex.replace('.tex', '');
  const bcfPath = `build/${baseName}.bcf`;
  if (existsSync(bcfPath)) {
    const bcfContent = readFileSync(bcfPath, 'utf8');
    const versionMatch = bcfContent.match(/bltxversion="(\d+\.\d+)"/);
    if (versionMatch && versionMatch[1] !== '3.20') {
      throw new Error(
        `Biber/biblatex version mismatch: bcf has bltxversion=${versionMatch[1]}, expected 3.20.`
      );
    }
  }

  const sourcePdf = 'build/main.pdf';
  if (!existsSync(sourcePdf)) {
    throw new Error(
      `PDF compilation failed - ${sourcePdf} not found.\n` +
      `Docker exit: ${result.status}`
    );
  }

  renameSync(sourcePdf, outputPdf);
  console.log(`✓ Compiled ${outputPdf} with SOURCE_DATE_EPOCH=${commitEpoch}`);
}
