import { compileFromFile } from 'json-schema-to-typescript';
import { writeFileSync, readFileSync } from 'fs';
import { join } from 'path';

async function generate() {
  console.log('Generating authoritative types from official schemas...');

  const cffSchemaPath = 'scripts/schemas/cff-schema.json';
  const zenodoSchemaPath = 'scripts/schemas/zenodo-schema.json';
  const outputPath = 'scripts/types.ts';

  try {
    // 1. Generate CFF types
    console.log(`  Processing ${cffSchemaPath}...`);
    const cffTypes = await compileFromFile(cffSchemaPath, {
      bannerComment: '/* eslint-disable */\n/** This file was automatically generated from official JSON schemas. DO NOT MODIFY BY HAND. **/',
      style: { singleQuote: true },
      unreachableDefinitions: true
    });

    // 2. Generate Zenodo types
    console.log(`  Processing ${zenodoSchemaPath}...`);
    const zenodoTypes = await compileFromFile(zenodoSchemaPath, {
      bannerComment: '',
      style: { singleQuote: true },
      unreachableDefinitions: true
    });

    // 3. Combine and add CiteStyle/CSL imports
    const finalContent = [
      cffTypes,
      '\n// --- Zenodo Types ---\n',
      zenodoTypes,
      '\n// --- Manual Extensions & Citestyle Integration ---\n',
      "import type { CslItem } from '@citestyle/types';",
      'export type { CslItem };',
      '',
      '/** Helper to ensure our mapping is type-safe */',
      'export interface CitationMetadataState {',
      '  version: string;',
      '  csl: CslItem[];',
      '}'
    ].join('\n');

    writeFileSync(outputPath, finalContent);
    console.log(`  ✓ Types generated and saved to ${outputPath}`);
  } catch (error) {
    console.error('  [Error] Failed to generate types:', error);
    process.exit(1);
  }
}

generate();
