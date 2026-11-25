#!/usr/bin/env tsx
/**
 * Generated witness inventory — `docs/witness-inventory.md` (DOCS-CONSOLIDATION-001 Fase 4).
 *
 * The census of this repository's marks — how many inline and own-line marks
 * there are, which decoration and accounting macros are used, which of the
 * family's gates hold here, which id parts fail the naming standard and which
 * file carries which marks — is MEASURED, never typed.  `pnpm run
 * witness:inventory` rewrites `docs/witness-inventory.md` from the working
 * tree; `pnpm run inventory:check` (wired into `validate`, right after
 * `counts:check`) fails with a unified diff when it has drifted, so a stale
 * census is loud instead of a report's footnote.
 *
 * Corpus: every tracked `.tex` source of the manuscript — `main.tex` and the
 * recursive `src/` tree.  Two exclusions, both stated in the generated file:
 * a line whose first non-space character is `%` is a TeX comment, and a line
 * that DEFINES one of the counted macros (`\newcommand{\witness}…` and kin) is
 * a definition, not a use.
 *
 * Determinism: no Date, no locale, no network, no commit id — only local
 * measurements over the tracked sources, so f(f(x)) = f(x) and two consecutive
 * runs are byte-identical.  Dated reports under `docs/reports/` are snapshots
 * of a moment and stay outside this mechanism.
 *
 * Modes:
 *   (default)  rewrite docs/witness-inventory.md
 *   --check    compare, print the diff, exit 1 on any drift
 */
import { execSync } from 'child_process';
import { existsSync, readFileSync, writeFileSync } from 'fs';
import { basename, resolve } from 'path';

const OUT = 'docs/witness-inventory.md';

/* ------------------------------------------------------------- measurement */

function sh(cmd: string): string {
  return execSync(`${cmd} 2>&1`, { encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] });
}

function isComment(line: string): boolean {
  return line.trimStart().startsWith('%');
}

function defLine(line: string, name: string): boolean {
  const n = name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return (
    new RegExp(`\\\\(?:new|renew|provide)command\\{\\\\${n}(?![A-Za-z@])`).test(line) ||
    new RegExp(`\\\\DeclareRobustCommand\\{\\\\${n}(?![A-Za-z@])`).test(line) ||
    new RegExp(`\\\\def\\\\${n}(?![A-Za-z@])`).test(line)
  );
}

interface Source {
  file: string;
  /** Non-comment lines, with their original 1-based line numbers. */
  lines: { no: number; text: string }[];
}

function corpus(): Source[] {
  const tracked = sh("git ls-files -- '*.tex'")
    .split('\n')
    .filter((p) => p.length > 0)
    .filter((p) => p === 'main.tex' || p.startsWith('src/'))
    .sort();
  return tracked.map((file) => ({
    file,
    lines: readFileSync(file, 'utf8')
      .split('\n')
      .map((text, i) => ({ no: i + 1, text }))
      .filter((l) => !isComment(l.text)),
  }));
}

/** `\tier[ids]{X}` / `\tier{X}` — group 1 = the optional argument, group 2 = the class. */
const TIER = /\\tier\s*(?:\[([^\]]*)\])?\s*\{([^{}]*)\}/g;
/** `\witness{X}{…}` — group 1 = the class (the ids may contain nested braces). */
const WITNESS = /\\witness\s*\{([^{}]*)\}/g;

function matches(text: string, re: RegExp): RegExpExecArray[] {
  re.lastIndex = 0;
  const out: RegExpExecArray[] = [];
  let m: RegExpExecArray | null;
  while ((m = re.exec(text)) !== null) out.push(m);
  return out;
}

/** Split a tag argument on the commas that sit outside every brace group. */
function splitIds(arg: string): string[] {
  const parts: string[] = [];
  let depth = 0;
  let cur = '';
  for (const ch of arg) {
    if (ch === '{') depth += 1;
    else if (ch === '}') depth -= 1;
    if (ch === ',' && depth === 0) {
      parts.push(cur);
      cur = '';
    } else {
      cur += ch;
    }
  }
  parts.push(cur);
  return parts.map((p) => p.trim()).filter((p) => p.length > 0);
}

const SNAKE = /^[a-z][a-z0-9_]*$/;
const QUALIFIED = /^[A-Za-z_][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_']+)+$/;

/** An id part is standard when it is a test anchor, snake_case or a namespace-qualified name. */
function isStandardId(part: string): boolean {
  const raw = part.trim();
  if (raw.startsWith('\\testref{')) return true;
  const inner = /^\\(?:code|texttt)\{(.*)\}$/.exec(raw);
  const id = (inner ? inner[1] : raw).replace(/\\_/g, '_');
  return SNAKE.test(id) || QUALIFIED.test(id);
}

function citationKeys(): Set<string> {
  if (!existsSync('citation.csl.json')) return new Set();
  const data = JSON.parse(readFileSync('citation.csl.json', 'utf8')) as unknown;
  const records = Array.isArray(data) ? data : [];
  const keys = new Set<string>();
  for (const record of records) {
    const id = (record as { id?: unknown }).id;
    if (typeof id === 'string') keys.add(id);
  }
  return keys;
}

interface Census {
  repo: string;
  files: number;
  tierIdsP: number;
  tierIdsN: number;
  tierBareP: number;
  tierBareN: number;
  witnessOwnP: number;
  witnessOwnN: number;
  witnessMid: number;
  tierTestrefN: number;
  nTagCitations: number;
  nTagDistinct: number;
  macros: { name: string; count: number }[];
  keyLintFailures: number;
  stars: number;
  tierColumns: number;
  pendingD7: { site: string }[];
  openSites: { site: string }[];
  nonStandard: { id: string; count: number }[];
  nonStandardOccurrences: number;
  perFile: { file: string; count: number }[];
}

function countMacro(sources: Source[], name: string): number {
  const re = new RegExp(`\\\\${name}(?![A-Za-z@])`, 'g');
  let total = 0;
  for (const src of sources) {
    for (const line of src.lines) {
      if (defLine(line.text, name)) continue;
      total += matches(line.text, re).length;
    }
  }
  return total;
}

function census(): Census {
  const sources = corpus();
  const keys = citationKeys();

  let tierIdsP = 0;
  let tierIdsN = 0;
  let tierBareP = 0;
  let tierBareN = 0;
  let witnessOwnP = 0;
  let witnessOwnN = 0;
  let witnessMid = 0;
  let tierTestrefN = 0;
  const nTagIds: string[] = [];
  let keyLintFailures = 0;
  let stars = 0;
  let tierColumns = 0;
  const pendingD7: { site: string }[] = [];
  const openSites: { site: string }[] = [];
  const nonStandardCounts = new Map<string, number>();
  const perFile: { file: string; count: number }[] = [];

  for (const src of sources) {
    let fileMarks = 0;
    for (const line of src.lines) {
      const text = line.text;

      for (const m of matches(text, TIER)) {
        const arg = m[1];
        const cls = m[2].trim();
        fileMarks += 1;
        if (arg === undefined || arg === '') {
          if (cls === 'P') tierBareP += 1;
          else if (cls === 'N') tierBareN += 1;
        } else {
          if (cls === 'P') tierIdsP += 1;
          else if (cls === 'N') tierIdsN += 1;
          const parts = splitIds(arg);
          if (cls === 'N') {
            nTagIds.push(...parts);
            if (parts.length > 0 && parts.every((p) => p.startsWith('\\testref{'))) tierTestrefN += 1;
          }
          for (const part of parts) {
            if (isStandardId(part)) continue;
            const id = part.replace(/\\_/g, '_');
            nonStandardCounts.set(id, (nonStandardCounts.get(id) ?? 0) + 1);
          }
          if (keys.size > 0) {
            for (const part of parts) {
              if (keys.has(part) || part.includes('\\cite')) keyLintFailures += 1;
            }
          }
        }
      }

      for (const m of matches(text, WITNESS)) {
        const cls = m[1].trim();
        const ownLine = text.slice(0, m.index ?? 0).trim() === '';
        if (ownLine) {
          if (cls === 'P') witnessOwnP += 1;
          else if (cls === 'N') witnessOwnN += 1;
        } else {
          witnessMid += 1;
        }
        const tail = text.slice((m.index ?? 0) + m[0].length);
        const open = /^\s*\{/.exec(tail);
        if (open) {
          let depth = 0;
          let end = -1;
          for (let i = open.index! + open[0].length - 1; i < tail.length; i++) {
            if (tail[i] === '{') depth += 1;
            else if (tail[i] === '}') {
              depth -= 1;
              if (depth === 0) {
                end = i;
                break;
              }
            }
          }
          if (end > 0) {
            const parts = splitIds(tail.slice(open.index! + open[0].length, end));
            if (cls === 'N') nTagIds.push(...parts);
          }
        }
      }

      if (/\\LeanStar(?![A-Za-z@])/.test(text) && !defLine(text, 'LeanStar')) stars += 1;
      tierColumns += [...text.matchAll(/\|\s*Tier\s*\|/g)].length;
      if (/pending\(D7\)/.test(text)) pendingD7.push({ site: `${src.file}:${line.no}` });
      if (/\(open;/.test(text)) openSites.push({ site: `${src.file}:${line.no}` });
    }
    if (fileMarks > 0) perFile.push({ file: src.file, count: fileMarks });
  }

  const nonStandard = [...nonStandardCounts.entries()]
    .map(([id, count]) => ({ id, count }))
    .sort((a, b) => (b.count - a.count) || (a.id < b.id ? -1 : a.id > b.id ? 1 : 0));

  const macroNames = ['LeanInline', 'LeanStar', 'LeanTally', 'LeanCW', 'leanline', 'code', 'testref', 'witness'];

  return {
    repo: basename(resolve('.')),
    files: sources.length,
    tierIdsP,
    tierIdsN,
    tierBareP,
    tierBareN,
    witnessOwnP,
    witnessOwnN,
    witnessMid,
    tierTestrefN,
    nTagCitations: nTagIds.length,
    nTagDistinct: new Set(nTagIds).size,
    macros: macroNames.map((name) => ({ name, count: countMacro(sources, name) })),
    keyLintFailures,
    stars,
    tierColumns,
    pendingD7,
    openSites,
    nonStandard,
    nonStandardOccurrences: nonStandard.reduce((n, e) => n + e.count, 0),
    perFile,
  };
}

/* ------------------------------------------------------------------ render */

function mdEscape(id: string): string {
  return id.replace(/_/g, '\\_');
}

function render(c: Census): string {
  const out: string[] = [];
  out.push(`# Witness inventory — ${c.repo}`);
  out.push('');
  out.push(
    '> **GENERATED** — `pnpm run witness:inventory` (`scripts/tasks/witness-inventory.ts`) rewrites\n' +
      '> this file from the working tree; `pnpm run inventory:check` (inside `validate`) fails with\n' +
      '> a diff when it drifts. Do not edit by hand.'
  );
  out.push('');
  out.push(
    `Measured over the tracked manuscript sources (\`main.tex\` and \`src/**/*.tex\`) — ${c.files} files. ` +
      'TeX comments (a line whose first non-space character is `%`) and the lines that *define* a counted ' +
      'macro are excluded; nothing here is copied from an older document. The form taxonomy is the one of ' +
      '`docs/witness-contract.md` §6.1.'
  );
  out.push('');
  out.push('## Marks');
  out.push('');
  out.push('| form | count |');
  out.push('|---|--:|');
  out.push(`| \`\\tier[ids]{P}\` | ${c.tierIdsP} |`);
  out.push(`| \`\\tier[ids]{N}\` | ${c.tierIdsN} |`);
  out.push(`| \`\\tier{P}\` (bare) | ${c.tierBareP} |`);
  out.push(`| \`\\tier{N}\` (bare) | ${c.tierBareN} |`);
  out.push(`| own-line \`\\witness{P}{…}\` | ${c.witnessOwnP} |`);
  out.push(`| own-line \`\\witness{N}{…}\` | ${c.witnessOwnN} |`);
  out.push(`| mid-line \`\\witness{…}\` (no block) | ${c.witnessMid} |`);
  out.push(`| \`\\tier[\\testref{…}]{N}\` marks | ${c.tierTestrefN} |`);
  out.push('');
  out.push(`Ids carried by \`N\` marks: **${c.nTagCitations} ids over ${c.nTagDistinct} distinct**.`);
  out.push('');
  out.push('## Decoration and accounting macros');
  out.push('');
  out.push('| macro | occurrences in the manuscript |');
  out.push('|---|--:|');
  for (const m of c.macros) out.push(`| \`\\${m.name}\` | ${m.count} |`);
  out.push('');
  out.push('## Gates measured here');
  out.push('');
  out.push('| gate | result |');
  out.push('|---|---|');
  out.push(`| citation-key lint (no key, no \`\\cite\` inside a tag) | **${c.keyLintFailures} failures** |`);
  out.push(`| stars (\`\\LeanStar\` body uses) | **${c.stars}** |`);
  out.push(`| \`Tier\` column in a table | **${c.tierColumns}** |`);
  out.push(`| \`pending(D7)\` markers | **${c.pendingD7.length}** |`);
  out.push(
    `| \`\\tier[…]\` id parts that are neither a \`\\testref\`, a snake_case id nor a qualified declaration | **${c.nonStandardOccurrences}** |`
  );
  out.push(`| open sites (\`(open;\`) | **${c.openSites.length}** |`);
  out.push('');

  if (c.nonStandard.length > 0) {
    const shown = c.nonStandard.slice(0, 60);
    out.push(
      `\`\\tier[…]\` ids that are neither a \`\\testref\`, a snake_case id nor a namespace-qualified declaration ` +
        `(${c.nonStandardOccurrences} occurrences, ${c.nonStandard.length} distinct):`
    );
    out.push('');
    for (const e of shown) out.push(`- \`${mdEscape(e.id)}\` ×${e.count}`);
    if (c.nonStandard.length > shown.length) {
      out.push(`- … ${c.nonStandard.length - shown.length} further distinct ids`);
    }
    out.push('');
  }

  if (c.pendingD7.length > 0) {
    out.push('`pending(D7)` markers:');
    out.push('');
    for (const s of c.pendingD7) out.push(`- \`${s.site}\``);
    out.push('');
  }

  if (c.openSites.length > 0) {
    out.push('Open sites:');
    out.push('');
    for (const s of c.openSites) out.push(`- \`${s.site}\``);
    out.push('');
  }

  out.push('## Per-file marks');
  out.push('');
  out.push('| file | `\\tier[…]` + `\\tier{…}` marks |');
  out.push('|---|--:|');
  for (const f of c.perFile) out.push(`| \`${f.file}\` | ${f.count} |`);
  out.push('');
  out.push('Re-generate with `pnpm run witness:inventory`; a hand-edited figure is a defect.');
  out.push('');
  return out.join('\n');
}

/* -------------------------------------------------------------------- run */

function unifiedDiff(onDisk: string, rendered: string): string {
  const a = onDisk.split('\n');
  const b = rendered.split('\n');
  const n = a.length;
  const m = b.length;
  const lcs: number[][] = Array.from({ length: n + 1 }, () => new Array<number>(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--) {
    for (let j = m - 1; j >= 0; j--) {
      lcs[i][j] = a[i] === b[j] ? lcs[i][j + 1] + 1 : Math.max(lcs[i + 1][j], lcs[i][j + 1]);
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
  return `--- ${OUT} (on disk)\n+++ ${OUT} (rendered from the measurements)\n@@ -1,${n} +1,${m} @@\n${body.join('\n')}\n`;
}

function main(): number {
  const check = process.argv.includes('--check');
  try {
    const rendered = render(census());
    const onDisk = existsSync(OUT) ? readFileSync(OUT, 'utf8') : '';
    if (check) {
      if (onDisk !== rendered) {
        process.stdout.write(unifiedDiff(onDisk, rendered));
        process.stderr.write(`inventory:check failed — ${OUT} has drifted. Run \`pnpm run witness:inventory\`.\n`);
        return 1;
      }
      console.log(`inventory:check ✓ ${OUT} matches the measured census.`);
      return 0;
    }
    if (onDisk === rendered) {
      console.log(`witness:inventory ✓ ${OUT} already up to date.`);
      return 0;
    }
    writeFileSync(OUT, rendered);
    console.log(`witness:inventory ✓ ${OUT} rewritten from the working tree.`);
    return 0;
  } catch (error) {
    process.stderr.write(`witness:inventory: ${error instanceof Error ? error.message : String(error)}\n`);
    return 1;
  }
}

process.exit(main());
