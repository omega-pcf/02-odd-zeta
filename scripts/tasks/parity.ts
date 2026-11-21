#!/usr/bin/env tsx
/**
 * Family contract parity gate — SPEC-004 §3 (phase P5).
 *
 * Fails when this repository drifts from the contract every sibling exposes:
 *
 *   (a) the contract script keys exist in `package.json` and are non-empty:
 *       `build`, `verify`, `figures`, `selfcitations`, `selfcitations:check`, `validate`;
 *   (b) `main.tex` carries exactly one `selfcite id="version"` marker pair,
 *       not inverted;
 *   (c) the token inside that region is the clean release form `vX.Y.Z` of
 *       `package.json` — never a `-dev@<sha>` suffix (SPEC-004 §2 as amended
 *       2026-11-20: that shape lives only in the rendered PDF, injected by
 *       `scripts/build.ts` and restored right after the render) — AND sits
 *       inside `\texttt{…}`, the page-1 line setting only the identifier in
 *       monospace (the labels stay `\textbf`; order of 2026-11-20);
 *   (d) `validate` runs `selfcitations:check`.
 *
 * It is wired into `validate`, so a repository that drifts fails its own
 * gate instead of drifting silently.  Read-only: it writes nothing and
 * derives everything from `package.json` and `main.tex`.
 */
import { readFileSync } from 'fs';
import { VERSION_TOKEN, isVersionTokenWrapped } from './selfcitations.js';

const PACKAGE = 'package.json';
const TEX = 'main.tex';
const REQUIRED_SCRIPTS = ['build', 'verify', 'figures', 'selfcitations', 'selfcitations:check', 'validate'] as const;
const TEX_VERSION_BEGIN = '% selfcite:begin id="version"';
const TEX_VERSION_END = '% selfcite:end id="version"';

const failures: string[] = [];

function fail(check: string, detail: string): void {
  failures.push(`${check} ${detail}`);
}

function main(): number {
  const pkg = JSON.parse(readFileSync(PACKAGE, 'utf8')) as { scripts?: Record<string, string>; version?: string };
  const scripts = pkg.scripts ?? {};

  // (a) the contract script keys.
  for (const key of REQUIRED_SCRIPTS) {
    if (typeof scripts[key] !== 'string' || !scripts[key].trim()) {
      fail('(a)', `package.json scripts.${key} is missing or empty`);
    }
  }

  // (d) validate runs the check.
  if (typeof scripts.validate === 'string' && !scripts.validate.includes('selfcitations:check')) {
    fail('(d)', `validate must run selfcitations:check (got: ${scripts.validate})`);
  }

  // (b) exactly one marker pair, in order.
  const tex = readFileSync(TEX, 'utf8');
  const begins = tex.split(TEX_VERSION_BEGIN).length - 1;
  const ends = tex.split(TEX_VERSION_END).length - 1;
  if (begins !== 1 || ends !== 1) {
    fail('(b)', `expected exactly one marker pair for id="version" in ${TEX}, found ${begins} begin / ${ends} end`);
  } else {
    const beginAt = tex.indexOf(TEX_VERSION_BEGIN);
    const endAt = tex.indexOf(TEX_VERSION_END);
    if (endAt < beginAt) {
      fail('(b)', `marker pair for id="version" is inverted (end before begin)`);
    } else {
      const afterBegin = beginAt + TEX_VERSION_BEGIN.length;
      const contentStart = tex.charAt(afterBegin) === '\n' ? afterBegin + 1 : afterBegin;
      const content = tex.slice(contentStart, endAt);

      // (c) the committed token is the clean release form of package.json —
      // the -dev@<sha> shape exists only in the rendered PDF.
      const token = VERSION_TOKEN.exec(content);
      if (!token) {
        fail('(c)', `no version token inside the "${TEX}" markers`);
      } else if (!/^v\d+\.\d+\.\d+$/.test(token[0])) {
        fail(
          '(c)',
          `${TEX} carries "${token[0]}"; the committed token must be the clean vX.Y.Z ` +
            `(SPEC-004 §2 as amended — no -dev@ suffix ever enters git)`
        );
      } else if (typeof pkg.version !== 'string' || !/^\d+\.\d+\.\d+$/.test(pkg.version)) {
        fail('(c)', `${PACKAGE} "version" is missing or malformed (expected a clean X.Y.Z)`);
      } else if (token[0] !== `v${pkg.version}`) {
        fail('(c)', `${TEX} prints ${token[0]}, ${PACKAGE} says v${pkg.version}`);
      } else if (!isVersionTokenWrapped(content, token.index, token[0].length)) {
        fail(
          '(c)',
          `${TEX} carries ${token[0]} outside \\texttt{…}; the page-1 line must set only the ` +
            `version identifier in monospace (the labels stay \\textbf, "Version: " is not typed)`
        );
      }
    }
  }

  if (failures.length > 0) {
    for (const item of failures) process.stderr.write(`parity ✗ ${item}\n`);
    process.stderr.write(`parity: drifted from the SPEC-004 contract — run \`pnpm run selfcitations\` and re-check package.json.\n`);
    return 1;
  }
  console.log(
    'parity ✓ SPEC-004 contract holds: script keys present, exactly one version marker pair, ' +
      'committed token equals package.json’s clean vX.Y.Z inside \\texttt{…}, ' +
      'validate runs selfcitations:check.'
  );
  return 0;
}

process.exit(main());
