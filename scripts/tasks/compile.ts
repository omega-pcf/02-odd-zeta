import { spawnSync } from 'child_process';
import { existsSync, mkdirSync, readFileSync, renameSync } from 'fs';
import { getCommitEpoch } from '../utils/git.js';
import type { ReleaseConfig } from '../types.js';

/**
 * Print the tail of the LaTeX log file when compilation fails, so the
 * actual TeX error is visible instead of being swallowed by latexmk.
 */
function printLogTail(logPath: string): void {
  if (!existsSync(logPath)) {
    console.error(`    (log file ${logPath} not found)`);
    return;
  }
  const log = readFileSync(logPath, 'utf8');
  const lines = log.split('\n');
  const tail = lines.slice(-80).join('\n');
  console.error(`\n--- last 80 lines of ${logPath} ---\n${tail}\n--- end log ---\n`);
}

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
    // The paper prints `\today` ("last modified") in its date footnote, so the
    // calendar date must be the commit's own date as git records it (%ci,
    // UTC-6) and not the same instant read in UTC, which after 18:00 local
    // would be the next day.  Still deterministic: the zone is fixed and the
    // timestamp still comes from SOURCE_DATE_EPOCH, never from the clock.
    // POSIX form, not America/Mexico_City: the build image carries no
    // /usr/share/zoneinfo, so a named zone silently falls back to UTC.
    '-e', 'TZ=CST6',
    ...DOCKER_TEX_ENV.split(' '),
    DOCKER_IMAGE,
    'latexmk', '-pdf', '-interaction=nonstopmode', sourceTex,
  ];

  const result = spawnSync('docker', args, {
    stdio: 'pipe',
    encoding: 'utf8',
    maxBuffer: 10 * 1024 * 1024,
  });

  if (result.stdout) process.stdout.write(result.stdout);
  if (result.stderr) process.stderr.write(result.stderr);

  const baseName = sourceTex.replace('.tex', '');

  // Fail loudly: a non-zero latexmk exit must abort the build even if a
  // stale PDF from a previous run is still on disk.
  if (result.status !== 0) {
    printLogTail(`build/${baseName}.log`);
    throw new Error(
      `latexmk failed with exit code ${result.status} - see log tail above.`
    );
  }
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

  // A biber abort (e.g. malformed bibliography data) can leave the build
  // without entries; catch it instead of shipping a PDF with no references.
  const bblPath = `build/${baseName}.bbl`;
  if (existsSync(bcfPath)
      && !(existsSync(bblPath) && readFileSync(bblPath, 'utf8').includes('\\entry'))) {
    printLogTail(`build/${baseName}.log`);
    throw new Error(
      'biber produced no or an empty .bbl - the bibliography would be missing.'
    );
  }

  const sourcePdf = 'build/main.pdf';
  if (!existsSync(sourcePdf)) {
    printLogTail(`build/${baseName}.log`);
    throw new Error(
      `PDF compilation failed - ${sourcePdf} not found.\n` +
      `Docker exit: ${result.status}`
    );
  }

  renameSync(sourcePdf, outputPdf);
  console.log(`✓ Compiled ${outputPdf} with SOURCE_DATE_EPOCH=${commitEpoch}`);
}
