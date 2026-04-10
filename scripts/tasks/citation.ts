import { parse, stringify } from 'yaml';
import { readFileSync, writeFileSync, existsSync } from 'fs';
import type { CitationFile, ZenodoMetadata, RelatedIdentifier } from '../types.js';

const CITATION_PATH = 'CITATION.cff';
const ZENODO_PATH = '.zenodo.json';

export function updateCitationDate(version: string): void {
  if (!existsSync(CITATION_PATH)) {
    throw new Error(`CITATION.cff not found at ${CITATION_PATH}`);
  }

  const content = readFileSync(CITATION_PATH, 'utf8');
  const citation = parse(content) as CitationFile;

  citation['date-released'] = new Date().toISOString().split('T')[0];
  citation.version = version;

  writeFileSync(CITATION_PATH, stringify(citation));
  console.log(`✓ Updated date-released to ${citation['date-released']} and version to ${version}`);
}

/**
 * Generates .zenodo.json from CITATION.cff using native YAML parsing.
 * Preserves Zenodo-specific fields while syncing common metadata.
 */
export function generateZenodoJson(): void {
  console.log('  Synchronizing .zenodo.json with CITATION.cff (Native Sync)...');

  if (!existsSync(CITATION_PATH)) {
    throw new Error(`CITATION.cff not found at ${CITATION_PATH}`);
  }

  try {
    const cffContent = readFileSync(CITATION_PATH, 'utf8');
    const cff = parse(cffContent) as any;

    // 1. Read existing .zenodo.json if it exists to preserve Zenodo-only fields
    let existingMetadata: Partial<ZenodoMetadata> = {};
    if (existsSync(ZENODO_PATH)) {
      try {
        existingMetadata = JSON.parse(readFileSync(ZENODO_PATH, 'utf8'));
      } catch (e) {
        console.warn(`  Warning: Could not parse existing ${ZENODO_PATH}`);
      }
    }

    // 2. Map CFF fields to Zenodo fields
    // Map authors to creators
    const creators = (cff.authors || []).map((a: any) => ({
      name: a['family-names'] && a['given-names'] 
        ? `${a['family-names']}, ${a['given-names']}`
        : (a['family-names'] || a['given-names'] || 'Unknown'),
      affiliation: a.affiliation,
      orcid: a.orcid ? a.orcid.split('orcid.org/').pop() : undefined,
    }));

    // 3. Construct the merged metadata
    const final: ZenodoMetadata = {
      ...existingMetadata,
      title: cff.title || existingMetadata.title || '',
      version: cff.version || existingMetadata.version || '',
      description: (cff.abstract || existingMetadata.description || '').trim(),
      creators: creators.length > 0 ? creators : (existingMetadata.creators || []),
      keywords: cff.keywords || existingMetadata.keywords || [],
      license: (cff.license || existingMetadata.license || 'cc-by-4.0').toLowerCase(),
      publication_date: cff['date-released'] || existingMetadata.publication_date || new Date().toISOString().split('T')[0],
      // Preserve fixed Zenodo-specific fields
      upload_type: existingMetadata.upload_type || 'publication',
      publication_type: existingMetadata.publication_type || 'preprint',
      access_right: existingMetadata.access_right || 'open',
      language: cff.languages?.[0] || existingMetadata.language || 'eng',
      related_identifiers: existingMetadata.related_identifiers || [
        {
          identifier: cff['repository-code'] || 'https://github.com/omega-pcf/02-odd-zeta',
          relation: 'isSupplementTo',
          scheme: 'url',
          resource_type: 'software',
        }
      ],
    };

    // 4. Save final .zenodo.json
    writeFileSync(ZENODO_PATH, JSON.stringify(final, null, 2) + '\n');
    console.log(`✓ Successfully synchronized ${ZENODO_PATH} with ${CITATION_PATH}`);

  } catch (error) {
    console.error('  Failed to synchronize Zenodo metadata:', error instanceof Error ? error.message : error);
    throw error;
  }
}
