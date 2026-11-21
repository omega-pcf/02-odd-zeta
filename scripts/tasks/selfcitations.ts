#!/usr/bin/env tsx
/**
 * Deterministic self-citation regions in README.md (SPEC-001 §5.3).
 *
 * Reads CITATION.cff (post-sync) + package.json -> metadata.citationKey and
 * regenerates the two marked regions of README.md:
 *
 *   id="badge"     - the DOI badge line directly under the H1 (empty when the
 *                    CFF has no `doi`; the markers stay).
 *   id="citation"  - the whole `## Citation` section: heading, APA paragraph,
 *                    blank line, bibtex fence.
 *
 * It also owns the version printed by the paper: the marked line of main.tex
 * (id="version") always carries the clean release form `vX.Y.Z` read from
 * package.json, so the committed tree is green by construction (SPEC-004 §2
 * as amended 2026-11-20).  The development form `vX.Y.Z-dev@<shortsha>`
 * (+`-dirty` while `git status --porcelain` is not empty) never enters the
 * file: scripts/build.ts injects it with injectDevVersion() right before the
 * render and restores the original bytes from memory afterwards.  --check
 * fails on a mismatch; the default mode rewrites the token in place.
 *
 * Determinism: no Date, no Math.random, no locale-dependent formatting, no
 * network, fixed bibtex field order, LF, exactly one trailing newline per
 * region. Output satisfies f(f(x)) = f(x).
 *
 * Modes:
 *   (default)  rewrite only the bytes between the markers
 *   --check    four validations, exit 1 on any mismatch: (i) exactly one
 *              marker pair per id, not inverted; (ii) the README regions equal
 *              the rendered output (a unified diff is printed); (iii) the
 *              committed main.tex token is the clean `vX.Y.Z` of
 *              package.json — never a `-dev@<sha>` suffix, so a committed tree
 *              is green at rest; (iv) that token sits inside `\texttt{…}` on
 *              the page-1 line — only the identifier is monospace, the labels
 *              stay `\textbf` and `Version: ` itself is not typed.  The
 *              default mode restores (iii) and (iv) in place.  Exit 0
 *              otherwise.
 */
import { readFileSync, writeFileSync, existsSync } from 'fs';
import { execSync } from 'child_process';
import { parse as parseYaml } from 'yaml';

const PATHS = {
  README: 'README.md',
  CFF: 'CITATION.cff',
  PACKAGE: 'package.json',
  TEX: 'main.tex',
} as const;

const REGION_IDS = ['badge', 'citation'] as const;
type RegionId = (typeof REGION_IDS)[number];

const BEGIN = (id: string): string => `<!-- selfcite:begin id="${id}" -->`;
const END = (id: string): string => `<!-- selfcite:end id="${id}" -->`;

/**
 * The marked line of main.tex that carries the paper version, in LaTeX
 * comment form (main.tex has no HTML comments).  package.json is the single
 * source of the version: the sync writes it here, --check fails when the two
 * disagree.
 */
const TEX_VERSION_ID = 'version';
const TEX_VERSION_BEGIN = `% selfcite:begin id="${TEX_VERSION_ID}"`;
const TEX_VERSION_END = `% selfcite:end id="${TEX_VERSION_ID}"`;
/**
 * The version token as it prints in the paper.  The committed form is always
 * the clean release `v0.1.0`; the rendered form may be the development shape
 * `v0.1.0-dev@a1b2c3d` / `v0.1.0-dev@a1b2c3d-dirty` (SPEC-004 §2 as amended
 * 2026-11-20 — that shape exists only inside the PDF, injected at build time).
 * Applied only inside the `id="version"` region.
 */
export const VERSION_TOKEN = /v\d+\.\d+\.\d+(?:-dev@[0-9a-f]{7,}(?:-dirty)?)?/;

/** Tier 1 is never suffixed: `package.json` and the release argument stay clean. */
const CLEAN_VERSION = /^\d+\.\d+\.\d+$/;

/** The opener of the monospace wrapper around the token (8 characters). */
const TEXTT_OPEN = '\\texttt{';

/**
 * Is the `length`-long token that starts at `at` inside `text` wrapped in
 * `\texttt{…}`?
 *
 * The page-1 line sets ONLY the version identifier in monospace
 * (`\textbf{Version:} \texttt{vX.Y.Z}` — the label stays bold and `Version: `
 * itself is not typed).  The wrapper is part of the contract: `--check` fails
 * without it, the default mode restores it, `parity` reuses this predicate,
 * and `injectDevVersion()` replaces the token strictly inside it.
 */
export function isVersionTokenWrapped(text: string, at: number, length: number): boolean {
  const open = text.lastIndexOf(TEXTT_OPEN, at);
  return open >= 0 && open + TEXTT_OPEN.length === at && text.charAt(at + length) === '}';
}

/** Non-volatile fields of the block (SPEC-001 §3.3/§3.4). */
interface SelfCitationData {
  title: string;
  authors: { family: string; given: string }[];
  year: string;
  doi?: string;
  repositoryCode: string;
  repositorySlug: string; // owner/name, derived from repository-code
  citationKey: string;
}

interface Region {
  contentStart: number;
  contentEnd: number;
}

/* ------------------------------------------------------------------ inputs */

function readRequired(path: string): string {
  if (!existsSync(path)) throw new Error(`Missing required file: ${path}`);
  return readFileSync(path, 'utf8');
}

function loadData(): SelfCitationData {
  const cff = parseYaml(readRequired(PATHS.CFF)) as Record<string, any>;

  if (!cff || typeof cff.title !== 'string' || !cff.title.trim()) {
    throw new Error(`${PATHS.CFF}: missing required field "title"`);
  }
  const rawAuthors = Array.isArray(cff.authors) ? cff.authors : [];
  if (rawAuthors.length === 0) {
    throw new Error(`${PATHS.CFF}: missing required field "authors" (non-empty list)`);
  }
  if (typeof cff['repository-code'] !== 'string' || !cff['repository-code'].trim()) {
    throw new Error(`${PATHS.CFF}: missing required field "repository-code"`);
  }
  const dateReleased = typeof cff['date-released'] === 'string' ? cff['date-released'] : '';
  const yearMatch = /^(\d{4})/.exec(dateReleased);
  if (!yearMatch) {
    throw new Error(`${PATHS.CFF}: missing or malformed "date-released" (expected YYYY-MM-DD)`);
  }

  const pkg = JSON.parse(readRequired(PATHS.PACKAGE));
  const citationKey = pkg?.metadata?.citationKey;
  if (typeof citationKey !== 'string' || !citationKey.trim()) {
    throw new Error(`${PATHS.PACKAGE}: missing required field "metadata.citationKey"`);
  }

  const repositoryCode = (cff['repository-code'] as string).trim().replace(/\/+$/, '');

  return {
    title: cff.title,
    authors: rawAuthors.map((a: any, i: number) => {
      if (typeof a?.['family-names'] !== 'string' || !a['family-names'].trim()) {
        throw new Error(`${PATHS.CFF}: authors[${i}] has no "family-names"`);
      }
      return {
        family: a['family-names'],
        given: typeof a['given-names'] === 'string' ? a['given-names'] : '',
      };
    }),
    year: yearMatch[1],
    doi: typeof cff.doi === 'string' && cff.doi.trim() ? cff.doi.trim() : undefined,
    repositoryCode,
    repositorySlug: repositorySlug(repositoryCode),
    citationKey,
  };
}

/** `https://github.com/omega-pcf/05-kkgt` -> `omega-pcf/05-kkgt`. */
function repositorySlug(repositoryCode: string): string {
  const segments = repositoryCode
    .replace(/\.git$/, '')
    .split('/')
    .filter((s) => s.length > 0);
  if (segments.length < 2) {
    throw new Error(`Cannot derive owner/name from repository-code: ${repositoryCode}`);
  }
  return segments.slice(-2).join('/');
}

/* ------------------------------------------------------------------ render */

/** `Jorge Armando` -> `J. A.` */
function initials(given: string): string {
  return given
    .split(/\s+/)
    .filter(Boolean)
    .map((w) => `${w.charAt(0)}.`)
    .join(' ');
}

function nameOf(a: { family: string; given: string }): string {
  const init = initials(a.given);
  return init ? `${a.family}, ${init}` : a.family;
}

function apaAuthors(data: SelfCitationData): string {
  const names = data.authors.map(nameOf);
  if (names.length === 1) return names[0];
  return `${names.slice(0, -1).join(', ')}, & ${names[names.length - 1]}`;
}

function bibtexAuthors(data: SelfCitationData): string {
  return data.authors.map(nameOf).join(' and ');
}

function identifierClause(data: SelfCitationData): string {
  if (data.doi) return `DOI: [${data.doi}](https://doi.org/${data.doi}).`;
  return `Repository: [${data.repositorySlug}](${data.repositoryCode}).`;
}

/** Region `id="badge"`: Zenodo DOI badge, empty when the CFF has no doi. */
function renderBadge(data: SelfCitationData): string {
  if (!data.doi) return '';
  return `[![DOI](https://zenodo.org/badge/DOI/${data.doi}.svg)](https://doi.org/${data.doi})\n`;
}

/** Region `id="citation"`: heading + APA paragraph + bibtex fence (SPEC-001 §5.2). */
function renderCitation(data: SelfCitationData): string {
  const apa = `${apaAuthors(data)} (${data.year}). *${data.title}*. Preprint. ${identifierClause(data)}`;

  // Fixed literal field order — never object-key order (SPEC-001 §5.2).
  const bibFields: string[] = [
    `  author  = {${bibtexAuthors(data)}},`,
    `  title   = {${data.title}},`,
    `  journal = {Preprint},`,
    `  year    = {${data.year}},`,
  ];
  if (data.doi) bibFields.push(`  doi     = {${data.doi}},`);
  bibFields.push(`  url     = {${data.doi ? `https://doi.org/${data.doi}` : data.repositoryCode}}`);

  const lines = ['## Citation', '', apa, '', '```bibtex', `@article{${data.citationKey},`, ...bibFields, '}', '```'];
  return `${lines.join('\n')}\n`;
}

/* ------------------------------------------------------------------ regions */

function markerRe(kind: 'begin' | 'end', id: string): RegExp {
  const label = kind === 'begin' ? 'begin' : 'end';
  // Tolerates an optional annotation after the id (SPEC-001 §5.2 form).
  return new RegExp(`<!--\\s*selfcite:${label}\\s+id="${id}"[^>]*-->`, 'g');
}

function findRegions(readme: string): Map<RegionId, Region> {
  const regions = new Map<RegionId, Region>();
  for (const id of REGION_IDS) {
    const begins = [...readme.matchAll(markerRe('begin', id))];
    const ends = [...readme.matchAll(markerRe('end', id))];
    if (begins.length !== 1 || ends.length !== 1 || begins[0].index === undefined || ends[0].index === undefined) {
      throw new Error(
        `${PATHS.README}: expected exactly one marker pair for id="${id}", ` +
          `found ${begins.length} begin / ${ends.length} end marker(s)`
      );
    }
    const beginEnd = begins[0].index + begins[0][0].length;
    const endStart = ends[0].index;
    if (endStart < beginEnd) {
      throw new Error(`${PATHS.README}: marker pair for id="${id}" is inverted (end before begin)`);
    }
    const contentStart = readme.charAt(beginEnd) === '\n' ? beginEnd + 1 : beginEnd;
    regions.set(id, { contentStart, contentEnd: endStart });
  }
  return regions;
}

function replaceRegions(readme: string, regions: Map<RegionId, Region>, rendered: Map<RegionId, string>): string {
  // Apply from the end of the file backwards so earlier offsets stay valid.
  const ordered = REGION_IDS.map((id) => ({ id, ...regions.get(id)! })).sort((a, b) => b.contentStart - a.contentStart);
  let out = readme;
  for (const { id, contentStart, contentEnd } of ordered) {
    out = out.slice(0, contentStart) + rendered.get(id)! + out.slice(contentEnd);
  }
  return out;
}

/* ---------------------------------------------------------- paper version */

/** The version of record: package.json owns it, the paper prints it. */
function packageVersion(): string {
  const pkg = JSON.parse(readRequired(PATHS.PACKAGE));
  const version = pkg?.version;
  if (typeof version !== 'string' || !CLEAN_VERSION.test(version)) {
    throw new Error(`${PATHS.PACKAGE}: missing or malformed "version" (expected a clean X.Y.Z)`);
  }
  return version;
}

function git(args: string): string {
  return execSync(`git ${args}`, { encoding: 'utf8' }).trim();
}

/**
 * The two-tier display version (SPEC-004 §2).
 *
 * Tier 1 (release): an explicit clean version — `scripts/build.ts ${version}`
 * as run by `.release-it.ts`'s `after:bump` — or a release environment
 * (`RELEASE_IT` set) → `vX.Y.Z`.  Tier 2 (development): everything else →
 * `vX.Y.Z-dev@<shortsha>`, with `-dirty` while `git status --porcelain` is not
 * empty.  It is a display string for the PDF only: it never enters
 * `package.json`, `CITATION.cff`, `.zenodo.json`, a tag — nor `main.tex` on
 * disk (SPEC-004 §2 as amended 2026-11-20); it reaches the page only through
 * injectDevVersion(), applied by build.ts around the render and undone right
 * after it.
 */
export function computeDisplayVersion(releaseVersion?: string): string {
  const release = releaseVersion ?? (process.env.RELEASE_IT ? packageVersion() : undefined);
  if (release !== undefined) {
    if (!CLEAN_VERSION.test(release)) {
      throw new Error(`release version must be a clean X.Y.Z (got "${release}")`);
    }
    return `v${release}`;
  }
  const sha = git('rev-parse --short HEAD');
  if (!/^[0-9a-f]{7,}$/.test(sha)) throw new Error(`cannot derive a short git sha (got "${sha}")`);
  const dirty = git('status --porcelain') !== '';
  return `v${packageVersion()}-dev@${sha}${dirty ? '-dirty' : ''}`;
}

/**
 * Return `tex` with the token of the `id="version"` region replaced by the
 * display version (SPEC-004 §2): the clean `vX.Y.Z` on the release path, the
 * development `vX.Y.Z-dev@<sha>[-dirty]` otherwise.
 *
 * This is the *only* place the development shape is produced, and it works on
 * a string: scripts/build.ts writes the result, compiles, and writes the
 * original bytes back in a `finally`, so the committed main.tex never carries
 * a suffix.  Throws when the marker pair is missing, duplicated or inverted,
 * or when the region holds no version token.
 */
export function injectDevVersion(tex: string, releaseVersion?: string): string {
  const display = computeDisplayVersion(releaseVersion);
  const region = findTexVersionRegion(tex);
  const token = VERSION_TOKEN.exec(region.content);
  if (!token) {
    throw new Error(`${PATHS.TEX}: no version token inside the "${TEX_VERSION_ID}" markers`);
  }
  if (!isVersionTokenWrapped(region.content, token.index, token[0].length)) {
    throw new Error(
      `${PATHS.TEX}: the version token inside the "${TEX_VERSION_ID}" markers is outside ` +
        `\\texttt{…} — only the identifier is monospace on the page-1 line.  ` +
        `Run \`pnpm run selfcitations\`.`
    );
  }
  // The replacement stays strictly inside the \texttt{...} wrapper: only the
  // token's own bytes are swapped, so the dev form prints in monospace too.
  const at = region.start + token.index;
  return tex.slice(0, at) + display + tex.slice(at + token[0].length);
}

interface TexRegion {
  start: number; // offset of the marked line inside main.tex
  content: string; // the marked line, without the markers
}

function literalRe(text: string): RegExp {
  return new RegExp(text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'g');
}

/** Exactly one marker pair of TEX_VERSION_ID, or a thrown error. */
function findTexVersionRegion(tex: string): TexRegion {
  const begins = [...tex.matchAll(literalRe(TEX_VERSION_BEGIN))];
  const ends = [...tex.matchAll(literalRe(TEX_VERSION_END))];
  if (begins.length !== 1 || ends.length !== 1 || begins[0].index === undefined || ends[0].index === undefined) {
    throw new Error(
      `${PATHS.TEX}: expected exactly one marker pair for id="${TEX_VERSION_ID}", ` +
        `found ${begins.length} begin / ${ends.length} end marker(s)`
    );
  }
  const beginEnd = begins[0].index + begins[0][0].length;
  const endStart = ends[0].index;
  if (endStart < beginEnd) throw new Error(`${PATHS.TEX}: marker pair for id="${TEX_VERSION_ID}" is inverted`);
  const contentStart = tex.charAt(beginEnd) === '\n' ? beginEnd + 1 : beginEnd;
  return { start: contentStart, content: tex.slice(contentStart, endStart) };
}

/**
 * Keep the printed version of main.tex equal to package.json's clean version,
 * and keep it monospaced.
 *
 * The committed token is always the release form `vX.Y.Z` (SPEC-004 §2 as
 * amended 2026-11-20): the `-dev@<sha>` suffix exists only in the rendered
 * PDF, injected by build.ts and never written here.  It must additionally sit
 * inside `\texttt{…}` on the page-1 line — only the identifier is monospace
 * (order of 2026-11-20).  (--check compares and fails on either violation;
 * the default mode rewrites the token in place, wrapping it when the wrapper
 * is missing — the same contract as the README regions.)  Returns true when
 * the on-disk line differs from package.json or lacks the wrapper.
 */
function syncPaperVersion(check: boolean): boolean {
  const tex = readRequired(PATHS.TEX);
  const expected = `v${packageVersion()}`;
  const region = findTexVersionRegion(tex);
  const token = VERSION_TOKEN.exec(region.content);
  if (!token) {
    throw new Error(`${PATHS.TEX}: no version token inside the "${TEX_VERSION_ID}" markers`);
  }
  const wrapped = isVersionTokenWrapped(region.content, token.index, token[0].length);
  const clean = token[0] === expected;
  if (wrapped && clean) return false;

  if (check) {
    if (!clean) {
      process.stderr.write(
        `selfcitations:check failed — ${PATHS.TEX} carries "${token[0]}", expected the clean ${expected} ` +
          `(the committed token never carries a -dev@ suffix; SPEC-004 §2 as amended). ` +
          `Run \`pnpm run selfcitations\`.\n`
      );
    }
    if (!wrapped) {
      process.stderr.write(
        `selfcitations:check failed — ${PATHS.TEX} carries the version token "${token[0]}" outside ` +
          `\`\\texttt{…}\`` +
          `: the page-1 line sets only the identifier in monospace (the labels stay \`\\textbf\`, ` +
          `\`Version: \` itself is not typed).  Run \`pnpm run selfcitations\`.\n`
      );
    }
    return true;
  }

  if (!wrapped && region.content.includes(TEXTT_OPEN)) {
    throw new Error(
      `${PATHS.TEX}: the version token sits inside an unexpected \`\\texttt{…}\` span of the ` +
        `"${TEX_VERSION_ID}" line — fix that line by hand.`
    );
  }

  const at = region.start + token.index;
  const replacement = wrapped ? expected : `${TEXTT_OPEN}${expected}}`;
  writeFileSync(PATHS.TEX, tex.slice(0, at) + replacement + tex.slice(at + token[0].length));
  const changes: string[] = [];
  if (!clean) changes.push(`paper version set to ${expected} (was ${token[0]})`);
  if (!wrapped) changes.push(`version token wrapped in \\texttt{…}`);
  console.log(`  ✓ ${PATHS.TEX} ${changes.join(', ')}.`);
  return true;
}

/* -------------------------------------------------------------------- diff */

function unifiedDiff(onDisk: string, rendered: string, header: string): string {
  const a = onDisk.split('\n');
  const b = rendered.split('\n');
  const n = a.length;
  const m = b.length;
  const lcs: number[][] = Array.from({ length: n + 1 }, () => new Array<number>(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      lcs[i][j] = a[i] === b[j] ? lcs[i + 1][j + 1] + 1 : Math.max(lcs[i + 1][j], lcs[i][j + 1]);
    }
  }
  const body: string[] = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    if (a[i] === b[j]) {
      body.push(` ${a[i]}`);
      i++;
      j++;
    } else if (lcs[i + 1][j] >= lcs[i][j + 1]) {
      body.push(`-${a[i]}`);
      i++;
    } else {
      body.push(`+${b[j]}`);
      j++;
    }
  }
  while (i < n) body.push(`-${a[i++]}`);
  while (j < m) body.push(`+${b[j++]}`);
  return `--- ${header} (on disk)\n+++ ${header} (rendered from ${PATHS.CFF})\n@@ -1,${n} +1,${m} @@\n${body.join('\n')}\n`;
}

/* ------------------------------------------------------------------- entry */

interface RunResult {
  changed: boolean;
  checked: RegionId[]; // ids compared in --check mode
  stale: RegionId[]; // ids whose on-disk content differed
  staleTex: boolean; // main.tex's printed version differs from package.json
}

function run(check: boolean): RunResult {
  const readme = readRequired(PATHS.README);
  const data = loadData();
  const regions = findRegions(readme);
  const staleTex = syncPaperVersion(check);

  const rendered = new Map<RegionId, string>([
    ['badge', renderBadge(data)],
    ['citation', renderCitation(data)],
  ]);

  const stale: RegionId[] = [];
  for (const id of REGION_IDS) {
    const region = regions.get(id)!;
    const onDisk = readme.slice(region.contentStart, region.contentEnd);
    if (onDisk !== rendered.get(id)!) stale.push(id);
  }

  if (check) {
    for (const id of stale) {
      const region = regions.get(id)!;
      process.stdout.write(
        unifiedDiff(readme.slice(region.contentStart, region.contentEnd), rendered.get(id)!, `${PATHS.README} id="${id}"`)
      );
    }
    if (stale.length > 0) {
      process.stderr.write(
        `selfcitations:check failed — region(s) out of sync with ${PATHS.CFF}: ${stale.join(', ')}. ` +
          `Run \`pnpm run selfcitations\`.\n`
      );
    }
    return { changed: false, checked: [...REGION_IDS], stale, staleTex };
  }

  if (stale.length === 0 && !staleTex) return { changed: false, checked: [...REGION_IDS], stale, staleTex };

  if (stale.length > 0) writeFileSync(PATHS.README, replaceRegions(readme, regions, rendered));
  return { changed: true, checked: [...REGION_IDS], stale, staleTex };
}

/** Called by scripts/build.ts right after syncCitationMetadata(). */
export function syncSelfCitations(): void {
  const result = run(false);
  console.log(
    result.changed
      ? `  ✓ README.md self-citation regions regenerated (${result.stale.join(', ') || 'paper version'}).`
      : `  ✓ README.md self-citation regions up to date.`
  );
  if (result.staleTex) console.log(`  ✓ main.tex paper version aligned with ${PATHS.PACKAGE}'s clean version.`);
}

function main(): number {
  const check = process.argv.includes('--check');
  try {
    const result = run(check);
    if (check) {
      if (result.stale.length > 0 || result.staleTex) return 1;
      console.log(
        `selfcitations:check ✓ README.md regions match the rendered output and ` +
          `${PATHS.TEX} carries the clean vX.Y.Z token from ${PATHS.PACKAGE}, inside \\texttt{…}.`
      );
      return 0;
    }
    if (result.changed) console.log(`selfcitations ✓ README.md regions updated (${result.stale.join(', ')}).`);
    else console.log('selfcitations ✓ README.md regions already up to date.');
    if (result.staleTex) console.log(`selfcitations ✓ ${PATHS.TEX} paper version synced.`);
    return 0;
  } catch (error) {
    process.stderr.write(`selfcitations: ${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }
}

// Only run when invoked directly (tsx scripts/tasks/selfcitations.ts), not
// when build.ts imports syncSelfCitations().
const invokedDirectly = process.argv[1] !== undefined && process.argv[1].endsWith('selfcitations.ts');
if (invokedDirectly) {
  process.exit(main());
}
