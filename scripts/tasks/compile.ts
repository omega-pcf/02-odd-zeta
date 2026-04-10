import { execSync } from 'child_process';
import { existsSync, renameSync } from 'fs';
import { getCommitEpoch } from '../utils/git.js';
import type { ReleaseConfig } from '../types.js';

// Usar kjarosh/latex por mejor versionado explícito
// Alternativa: blang/latex:ubuntu (más popular pero menos versionado)
const DOCKER_IMAGE = 'kjarosh/latex:2024.4-full';

function runDockerCommand(command: string, commitEpoch: number): void {
  const dockerCmd = `docker run --rm \
    -v $(pwd):$(pwd) \
    -w $(pwd) \
    -e SOURCE_DATE_EPOCH=${commitEpoch} \
    -e LC_ALL=C \
    -e LANG=C \
    -e TZ=UTC \
    ${DOCKER_IMAGE} \
    ${command}`;

  execSync(dockerCmd, { stdio: 'inherit' });
}

export function compilePDF(config: ReleaseConfig): void {
  const { sourceTex, outputPdf } = config;
  const commitEpoch = getCommitEpoch();
  const baseName = sourceTex.replace('.tex', '');

  console.log(`\n📄 Compiling PDF with SOURCE_DATE_EPOCH=${commitEpoch}...`);

  // Step 1: First pdflatex pass
  console.log('  Running pdflatex (pass 1/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  // Step 2: bibtex for bibliography
  console.log('  Running bibtex (pass 2/4)...');
  runDockerCommand(`bibtex build/${baseName}`, commitEpoch);

  // Step 3: Second pdflatex pass for bibliography
  console.log('  Running pdflatex (pass 3/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  // Step 4: Third pdflatex pass for cross-references
  console.log('  Running pdflatex (pass 4/4)...');
  runDockerCommand(`pdflatex -interaction=nonstopmode -output-directory=build ${sourceTex}`, commitEpoch);

  const sourcePdf = 'build/main.pdf';
  if (!existsSync(sourcePdf)) {
    throw new Error(`PDF compilation failed - ${sourcePdf} not found`);
  }

  renameSync(sourcePdf, outputPdf);
  console.log(`✓ Compiled ${outputPdf} with SOURCE_DATE_EPOCH=${commitEpoch}`);
}

