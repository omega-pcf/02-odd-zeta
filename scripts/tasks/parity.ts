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
 *   (c) the token inside that region equals `computeDisplayVersion()` — the
 *       same derivation `selfcitations:check` applies (delegated, not
 *       re-implemented);
 *   (d) `validate` runs `selfcitations:check`.
 *
 * It is wired into `validate`, so a repository that drifts fails its own
 * gate instead of drifting silently.  Read-only: it writes nothing and
 * derives everything from `package.json`, `main.tex` and git.
 */
import { readFileSync } from 'fs';
import { computeDisplayVersion, VERSION_TOKEN } from './selfcitations.js';

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
  const pkg = JSON.parse(readFileSync(PACKAGE, 'utf8')) as { scripts?: Record<string, string> };
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

      // (c) the token equals computeDisplayVersion().
      const token = VERSION_TOKEN.exec(content);
      if (!token) {
        fail('(c)', `no version token inside the "${TEX}" markers`);
      } else {
        const expected = computeDisplayVersion();
        if (token[0] !== expected) fail('(c)', `${TEX} prints ${token[0]}, expected ${expected}`);
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
      'token equals computeDisplayVersion(), validate runs selfcitations:check.'
  );
  return 0;
}

process.exit(main());
