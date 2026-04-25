import { readFileSync, writeFileSync, existsSync, rmSync, mkdirSync } from 'fs';
import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';
import { Ajv, type ValidateFunction } from 'ajv';
import addFormats from 'ajv-formats';
// @ts-ignore
import { Cite } from '@citation-js/core';
import '@citation-js/plugin-csl';
import '@citation-js/plugin-cff';
import '@citation-js/plugin-bibtex';
import '@citation-js/plugin-zenodo';
import type { CslItem } from '@citestyle/types';
import type { 
  CitationFileFormat, 
  Reference,
  ZenodoDepositionMetadata
} from '../types.js';

/** 
 * Configuration Constants 
 */
const PATHS = {
  CSL: 'citation.csl.json',
  CFF: 'CITATION.cff',
  ZENODO: '.zenodo.json',
  BIB: 'src/bibliography.bib',
  CFF_SCHEMA: 'scripts/schemas/cff-schema.json',
  ZENODO_SCHEMA: 'scripts/schemas/zenodo-schema.json',
  BUILD: 'build'
};

/**
 * Validation Engine
 */
class ValidationEngine {
  private ajv = new Ajv({ allErrors: true, strict: false });
  private validators: Map<string, ValidateFunction> = new Map();

  constructor() {
    (addFormats as any)(this.ajv);
  }

  public validate(data: unknown, schemaPath: string, label: string): void {
    if (!existsSync(schemaPath)) return;
    
    let validateFn = this.validators.get(schemaPath);
    if (!validateFn) {
      const schema = JSON.parse(readFileSync(schemaPath, 'utf8'));
      validateFn = this.ajv.compile(schema);
      if (validateFn) {
        this.validators.set(schemaPath, validateFn);
      }
    }

    if (!validateFn) {
      throw new Error(`Failed to compile schema: ${schemaPath}`);
    }

    if (!validateFn(data)) {
      const errors = this.ajv.errorsText(validateFn.errors, { separator: '\n    ' });
      throw new Error(`[${label}] Schema validation failed:\n    ${errors}`);
    }
    console.log(`  ✓ ${label} validated.`);
  }
}

/**
 * Metadata Orchestration leveraging citation-js
 */
export class MetadataPipeline {
  private validator = new ValidationEngine();

  public sync(version: string): void {
    this.cleanup();
    console.log(`  Initiating standards-compliant metadata sync v${version}...`);

    const cslData = this.loadCsl();
    
    // 1. Bibliography (handled by citation-js)
    this.syncBibtex(cslData);

    // 2. Project Identity (CFF root remains source of truth, references from CSL)
    const cff = this.syncCff(cslData, version);

    // 3. Zenodo Metadata (derived from sanitized CFF)
    this.syncZenodo(cff, version);
  }

  private cleanup(): void {
    console.log('  Purging rebuildable artifacts...');
    [PATHS.BUILD, PATHS.BIB, PATHS.ZENODO].forEach(path => {
      if (existsSync(path)) {
        rmSync(path, { recursive: true, force: true });
        console.log(`    - Deleted ${path}`);
      }
    });
    if (!existsSync(PATHS.BUILD)) {
      mkdirSync(PATHS.BUILD, { recursive: true });
    }
  }

  private loadCsl(): CslItem[] {
    if (!existsSync(PATHS.CSL)) throw new Error(`Missing source: ${PATHS.CSL}`);
    return JSON.parse(readFileSync(PATHS.CSL, 'utf8'));
  }

  private syncBibtex(items: CslItem[]): void {
    const data = new Cite(items);
    const bib = data.format('bibtex');
    writeFileSync(PATHS.BIB, bib);
    console.log(`  ✓ ${PATHS.BIB} generated.`);
  }

  private syncCff(items: CslItem[], version: string): CitationFileFormat {
    if (!existsSync(PATHS.CFF)) throw new Error(`Missing identity root: ${PATHS.CFF}`);
    const cff = parseYaml(readFileSync(PATHS.CFF, 'utf8')) as CitationFileFormat;

    const pkg = JSON.parse(readFileSync('package.json', 'utf8'));
    cff.version = version;
    cff['date-released'] = new Date().toISOString().split('T')[0];
    cff.abstract = pkg.metadata?.abstract || cff.abstract;
    cff.keywords = pkg.keywords || cff.keywords;
    
    // Map CSL items to CFF references using citation-js
    const data = new Cite(items);
    const cffRefData = data.format('cff', { type: 'object' }) as any;
    
    // Normalize citation-js output to strict CFF 1.2.0
    cff.references = (cffRefData.references || []).map((ref: any) => {
      // 1. Fix date format (YYYY-MM-DD)
      const fixDate = (val: any) => {
        if (!val) return undefined;
        try {
          const d = new Date(val);
          return !isNaN(d.getTime()) ? d.toISOString().split('T')[0] : undefined;
        } catch { return undefined; }
      };
      if (ref['date-published']) ref['date-published'] = fixDate(ref['date-published']);
      if (ref['date-released']) ref['date-released'] = fixDate(ref['date-released']);
      if (ref['date-accessed']) ref['date-accessed'] = fixDate(ref['date-accessed']);

      // 2. Clean DOI formatting
      const cleanDoi = (val: string) => {
        if (!val) return val;
        return val.replace(/^https?:\/\/doi\.org\//, '').replace(/^doi:/, '').trim();
      };
      if (ref.doi) ref.doi = cleanDoi(ref.doi);

      // 3. Validate ISSN formatting
      if (ref.issn) {
        const firstIssn = ref.issn.split(/[,;]/)[0].trim();
        if (/^\d{4}-\d{3}[\dxX]$/.test(firstIssn)) ref.issn = firstIssn;
        else delete ref.issn;
      }

      // 4. Sanitize identifiers
      if (ref.identifiers) {
        ref.identifiers = ref.identifiers.filter((id: any) => {
          if (id.type === 'doi') id.value = cleanDoi(id.value);
          return ['doi', 'url', 'swh', 'isbn', 'issn', 'other'].includes(id.type);
        });
      }
      
      // 5. Normalize publisher metadata (ensure 2-letter ISO country codes)
      if (ref.publisher && ref.publisher.country && !/^[A-Z]{2}$/.test(ref.publisher.country)) {
        delete ref.publisher.country;
      }
      
      // 6. Normalize language codes (ensure 2-3 letter ISO codes)
      if (ref.languages) {
        ref.languages = ref.languages.filter((l: string) => /^[a-z]{2,3}$/.test(l));
        if (ref.languages.length === 0) delete ref.languages;
      }

      // 7. Deduplicate authors
      if (ref.authors) {
        const uniqueAuthors = new Map();
        ref.authors.forEach((a: any) => {
          const key = JSON.stringify(a);
          if (!uniqueAuthors.has(key)) uniqueAuthors.set(key, a);
        });
        ref.authors = Array.from(uniqueAuthors.values());
      }
      
      delete ref.month;
      return ref;
    });

    writeFileSync(PATHS.CFF, stringifyYaml(cff));
    this.validator.validate(cff, PATHS.CFF_SCHEMA, 'CITATION.cff');
    return cff;
  }


  private syncZenodo(cff: CitationFileFormat, version: string): void {
    const references = (cff.references || [])
      .map((ref: any) => {
        const authors = (ref.authors || [])
          .map((a: any) => `${a['family-names'] || a.name}${a['given-names'] ? ', ' + a['given-names'] : ''}`)
          .join('; ');
        
        const year = ref.year || ref['date-published']?.split('-')[0] || '';
        let refStr = `${authors} (${year}). ${ref.title}.`;
        
        // Add container info (journal, volume, issue, pages)
        let container = '';
        if (ref.journal) container += ` ${ref.journal}.`;
        else if (ref['conference-name']) container += ` ${ref['conference-name']}.`;
        else if (ref.publisher?.name) container += ` ${ref.publisher.name}.`;
        
        if (ref.volume) container += ` ${ref.volume}`;
        if (ref.issue) container += `(${ref.issue})`;
        
        const pages = ref.pages || (ref.start && ref.end ? `${ref.start}–${ref.end}` : ref.start || '');
        if (pages) container += `, ${pages}.`; else if (ref.volume || ref.issue) container += '.';

        refStr += container;

        // Add DOI (primary link)
        if (ref.doi) {
          const doiUrl = `https://doi.org/${ref.doi.replace(/^doi:/, '')}`;
          refStr += ` ${doiUrl}`;
        }

        // Add URL (only if not a duplicate of the DOI link)
        if (ref.url) {
          const cleanUrl = ref.url.replace(/^doi:/, '');
          const isDoiLink = cleanUrl.includes('doi.org/');
          if (!isDoiLink || !ref.doi) {
            if (!refStr.includes(cleanUrl)) {
              refStr += ` ${cleanUrl}`;
            }
          }
        }

        return refStr.replace(/\.\./g, '.').trim();
      })
      .sort((a, b) => a.localeCompare(b));

    const pkg = JSON.parse(readFileSync('package.json', 'utf8'));
    const zenodo: ZenodoDepositionMetadata = {
      title: cff.title,
      description: pkg.metadata?.zenodo_description || cff.abstract || cff.title,
      version: version,
      publication_date: cff['date-released'] || new Date().toISOString().split('T')[0],
      creators: (cff.authors || []).map((a: any) => ({
        name: a.name || `${a['family-names']}, ${a['given-names'] || ''}`.trim().replace(/,$/, ''),
        affiliation: a.affiliation,
        orcid: a.orcid?.replace(/.*orcid.org\//, '')
      })),
      keywords: cff.keywords || [],
      upload_type: 'publication',
      publication_type: 'preprint',
      access_right: 'open',
      license: Array.isArray(cff.license) ? cff.license[0] : (cff.license as string || 'cc-by-4.0'),
      language: (cff as any).language || 'eng',
      references: references
    };

    if (cff['repository-code']) {
      zenodo.related_identifiers = [
        {
          identifier: cff['repository-code'],
          relation: 'isSupplementTo',
          resource_type: 'software'
        }
      ];
    }

    // Add references with DOIs as related identifiers
    (cff.references || []).forEach((ref: any) => {
      if (ref.doi) {
        if (!zenodo.related_identifiers) zenodo.related_identifiers = [];
        
        // Map CFF resource types to Zenodo resource types
        let resourceType = 'publication';
        const type = ref.type?.toLowerCase();
        if (type === 'software') resourceType = 'software';
        else if (type === 'dataset') resourceType = 'dataset';
        else if (type === 'image') resourceType = 'image';
        else if (type === 'video') resourceType = 'video';
        
        zenodo.related_identifiers.push({
          identifier: ref.doi,
          relation: 'cites',
          resource_type: resourceType as any
        });
      }
    });

    writeFileSync(PATHS.ZENODO, JSON.stringify(zenodo, null, 2) + '\n');
    this.validator.validate(zenodo, PATHS.ZENODO_SCHEMA, '.zenodo.json');
    console.log(`  ✓ ${PATHS.ZENODO} generated from CITATION.cff.`);
  }
}

/**
 * Entry Point
 */
export function syncCitationMetadata(version: string): void {
  try {
    const pipeline = new MetadataPipeline();
    pipeline.sync(version);
  } catch (error) {
    console.error(`  [Fatal] Sync failed: ${error instanceof Error ? error.message : error}`);
    process.exit(1);
  }
}
