#!/usr/bin/env tsx
/**
 * Shared-file manifest gate — SPEC-004 §3 ("a family manifest … a repo that
 * drifts fails its own validate") and CVR-001 §5.2 priority 2 (the pinned hash
 * list BLD-001 §4 Option A never built, whose absence let `.latexmkrc` and
 * `scripts/utils/git.ts` drift without any gate noticing — CVR-001 B7/B8/CT-6).
 *
 * The manifest (`scripts/shared-files.json`) lists every file the five
 * repositories of the family must carry BYTE-IDENTICALLY, with its SHA-256.
 * This task has two modes, exactly like `scripts/tasks/counts.ts`:
 *
 *   pnpm run manifest         rewrite the hashes from this working tree
 *   pnpm run manifest:check   fail when any listed file drifted or is missing
 *
 * `manifest:check` is wired into `validate`, so a repository that changes one
 * of these files on its own fails its own gate instead of drifting silently.
 *
 * Rules the manifest encodes (see the `excluded` table in the JSON):
 *   - a shared file is changed FAMILY-WIDE: port the change to every repository,
 *     then refresh the manifest in each one and commit it with the change;
 *   - a file that legitimately stops being shared moves to `excluded` with its
 *     reason, in all five repositories, in the same commit;
 *   - the manifest itself is never listed in `files` (it would be circular)
 *     and `manifest.ts` is, so a drifted gate is caught by the gate.
 *
 * The digest is SHA-256, the ecosystem standard for checksum manifests
 * (`sha256sum -c`), and `sha256sum <file>` prints the same value the check
 * compares against.
 */
import { createHash } from 'crypto';
import { existsSync, readFileSync, writeFileSync } from 'fs';

const MANIFEST = 'scripts/shared-files.json';
const ALGORITHM = 'sha256';

/** The family the manifest speaks for — stated in every failure message. */
const FAMILY = '01-hilbert-polya, 02-odd-zeta, 03-crystalline-worldsheet, 04-mersenne-cr, 05-kk-golden-throat';

interface Manifest {
  algorithm?: string;
  description?: string;
  files?: Record<string, string>;
  excluded?: Record<string, string>;
}

function digest(content: Buffer): string {
  return createHash(ALGORITHM).update(content).digest('hex');
}

function loadManifest(): Manifest {
  if (!existsSync(MANIFEST)) {
    throw new Error(`${MANIFEST} is missing — create it with \`pnpm run manifest\``);
  }
  const parsed = JSON.parse(readFileSync(MANIFEST, 'utf8')) as Manifest;
  if (parsed.algorithm !== ALGORITHM) {
    throw new Error(`${MANIFEST} declares algorithm "${parsed.algorithm ?? '(none)'}"; this task uses "${ALGORITHM}"`);
  }
  if (!parsed.files || Object.keys(parsed.files).length === 0) {
    throw new Error(`${MANIFEST} lists no files`);
  }
  return parsed;
}

/** Report every listed file that is missing or carries different bytes. */
function check(): number {
  let manifest: Manifest;
  try {
    manifest = loadManifest();
  } catch (error) {
    process.stderr.write(`manifest ✗ ${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }

  const files = manifest.files ?? {};
  const excluded = manifest.excluded ?? {};
  const failures: string[] = [];

  for (const shared of Object.keys(files)) {
    if (shared in excluded) {
      failures.push(`${shared} is listed in both "files" and "excluded"`);
    }
    if (!existsSync(shared)) {
      failures.push(
        `${shared} is in the manifest but missing from this repository — restore it (git checkout -- ${shared}) ` +
          `or, if it was removed family-wide, drop it from the manifest in every repository`
      );
      continue;
    }
    const found = digest(readFileSync(shared));
    const expected = files[shared];
    if (found !== expected) {
      failures.push(
        `${shared}\n` +
          `         expected ${ALGORITHM} ${expected}\n` +
          `         found    ${ALGORITHM} ${found}`
      );
    }
  }

  if (failures.length > 0) {
    for (const item of failures) process.stderr.write(`manifest ✗ ${item}\n`);
    process.stderr.write(
      `manifest:check failed — ${failures.length} of ${Object.keys(files).length} shared files drifted.\n` +
        `A listed file is a FAMILY file: the same bytes must live in ${FAMILY}.\n` +
        `  · deliberate change: port it to every repository, run \`pnpm run manifest\` in each one,\n` +
        `    and commit the refreshed ${MANIFEST} together with the change;\n` +
        `  · the file is no longer shared: move it to "excluded" in ${MANIFEST} with its reason,\n` +
        `    in all five repositories.\n`
    );
    return 1;
  }

  console.log(
    `manifest ✓ ${Object.keys(files).length} shared files match ${MANIFEST} (${ALGORITHM}); ` +
      `${Object.keys(excluded).length} documented exclusions.`
  );
  return 0;
}

/** Rewrite the hashes from this working tree. Family-wide use only. */
function write(): number {
  let manifest: Manifest;
  try {
    manifest = loadManifest();
  } catch (error) {
    process.stderr.write(`manifest ✗ ${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }

  const files = manifest.files ?? {};
  const missing = Object.keys(files).filter(file => !existsSync(file));
  if (missing.length > 0) {
    process.stderr.write(`manifest ✗ cannot rewrite: missing ${missing.join(', ')}\n`);
    return 1;
  }

  const refreshed: Record<string, string> = {};
  for (const file of Object.keys(files).sort()) refreshed[file] = digest(readFileSync(file));

  writeFileSync(
    MANIFEST,
    `${JSON.stringify(
      {
        algorithm: manifest.algorithm,
        description: manifest.description,
        files: refreshed,
        excluded: manifest.excluded,
      },
      null,
      2
    )}\n`
  );
  console.log(`manifest ✓ ${MANIFEST} rewritten: ${Object.keys(refreshed).length} files, ${ALGORITHM}.`);
  console.log('  The same change must now exist in every repository of the family.');
  return 0;
}

const checkMode = process.argv.includes('--check');
process.exit(checkMode ? check() : write());
