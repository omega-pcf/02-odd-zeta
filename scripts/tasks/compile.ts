import { execSync } from 'child_process';
import { existsSync, mkdirSync, renameSync } from 'fs';
import { getCommitEpoch } from '../utils/git.js';
import type { ReleaseConfig } from '../types.js';

// Usar kjarosh/latex por mejor versionado explícito
const DOCKER_IMAGE = 'kjarosh/latex:2024.4-full';

function runDockerCommand(command: string, commitEpoch: number): void {
  const dockerCmd = `docker run --rm \
    --user $(id -u):$(id -g) \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e SOURCE_DATE_EPOCH=${commitEpoch} \
    -e LC_ALL=C \
    -e LANG=C \
    -e TZ=UTC \
    ${DOCKER_IMAGE} \
    ${command}`;

  try {
    execSync(dockerCmd, { stdio: 'inherit' });
  } catch {
    // pdflatex with -interaction=nonstopmode exits non-zero on undefined refs
    // even when it produces valid output (.bcf, .aux, .pdf). This is normal
    // for intermediate passes — biber is the only step that must succeed.
  }
}

export function compilePDF(config: ReleaseConfig): void {
  const { sourceTex, outputPdf } = config;
  const commitEpoch = getCommitEpoch();
  const baseName = sourceTex.replace('.tex', '');

  console.log(`\n📄 Compiling PDF with SOURCE_DATE_EPOCH=${commitEpoch}...`);

  // Ensure build/ exists — Docker's pdflatex can't create it via -output-directory
  mkdirSync('build', { recursive: true });

  // Step 1: First pdflatex pass (creates .bcf for biber)
  console.log('  Running pdflatex (pass 1/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  // Step 2: biber for bibliography (must succeed — the only hard failure)
  console.log('  Running biber (pass 2/4)...');
  const biberCmd = `docker run --rm \
    --user $(id -u):$(id -g) \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e SOURCE_DATE_EPOCH=${commitEpoch} \
    -e LC_ALL=C \
    -e LANG=C \
    -e TZ=UTC \
    ${DOCKER_IMAGE} \
    biber build/${baseName}`;
  execSync(biberCmd, { stdio: 'inherit' });

  // Step 3: Second pdflatex pass (incorporates bibliography)
  console.log('  Running pdflatex (pass 3/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  // Step 4: Third pdflatex pass (resolves cross-references)
  console.log('  Running pdflatex (pass 4/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  const sourcePdf = 'build/main.pdf';
  if (!existsSync(sourcePdf)) {
    throw new Error(`PDF compilation failed - ${sourcePdf} not found`);
  }

  renameSync(sourcePdf, outputPdf);
  console.log(`✓ Compiled ${outputPdf} with SOURCE_DATE_EPOCH=${commitEpoch}`);
}
