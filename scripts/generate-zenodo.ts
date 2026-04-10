#!/usr/bin/env tsx
import { generateZenodoJson } from './tasks/citation.js';

try {
  console.log('Generating .zenodo.json from CITATION.cff...\n');
  generateZenodoJson();
  console.log('\n✅ Successfully generated .zenodo.json');
  process.exit(0);
} catch (error) {
  console.error('\n❌ Failed to generate .zenodo.json:', error);
  process.exit(1);
}

