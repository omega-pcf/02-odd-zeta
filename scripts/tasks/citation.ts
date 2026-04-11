import { readFileSync, writeFileSync, existsSync, rmSync, mkdirSync } from 'fs';
import { parse as parseYaml, stringify as stringifyYaml } from 'yaml';
import Ajv, { ValidateFunction } from 'ajv';
import addFormats from 'ajv-formats';
import striptags from 'striptags';
import escapeLatex from 'escape-latex';
import { Transform } from 'unicode2latex';
import { exportBibtex } from '@citestyle/bibtex';
import type { CslItem } from '@citestyle/types';
import type { 
  CitationFileFormat, 
  Reference,
  Person
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
 * Professional BibTeX Character Encoding.
 * Transforms Unicode metadata into LaTeX-compatible strings.
 */
class BibtexEncoder {
  private transformer = new Transform('bibtex');

  public encode(text: string): string {
    if (!text) return text;
    
    // 1. Strip HTML tags (e.g., <i>, <sub>) FIRST
    // This prevents the LaTeX transformer from mangling tags into math mode.
    let result = striptags(text);

    // 2. Unicode to LaTeX Transformation
    // unicode2latex handles 𝔽₁, &, %, $, etc.
    result = this.transformer.tolatex(result);

    // 3. Post-processing: Remove any accidental double-escapes (\textbackslash)
    result = result.replace(/\\textbackslash\{\}/g, '\\');

    return result;
  }
}

/**
 * Normalization Utilities
 */
const normalize = {
  doi: (doi?: string): string | undefined => {
    if (!doi) return undefined;
    const clean = doi.replace(/.*doi.org\//, '').trim();
    return clean.startsWith('10.') ? clean : undefined;
  },
  orcid: (orcid?: string): string | undefined => {
    if (!orcid) return undefined;
    const match = orcid.match(/[0-9]{4}-[0-9]{4}-[0-9]{4}-[0-9]{3}[0-9X]/);
    return match ? `https://orcid.org/${match[0]}` : undefined;
  },
  url: (url?: string): string | undefined => {
    if (!url) return undefined;
    const clean = url.trim();
    return clean.startsWith('http') ? clean : `https://${clean}`;
  }
};

/**
 * Validation Engine (Pre-compiled)
 */
class ValidationEngine {
  private ajv = new Ajv({ allErrors: true, strict: false });
  private validators: Map<string, ValidateFunction> = new Map();

  constructor() {
    addFormats(this.ajv);
  }

  public validate(data: unknown, schemaPath: string, label: string): void {
    if (!existsSync(schemaPath)) return;
    
    let validateFn = this.validators.get(schemaPath);
    if (!validateFn) {
      const schema = JSON.parse(readFileSync(schemaPath, 'utf8'));
      validateFn = this.ajv.compile(schema);
      this.validators.set(schemaPath, validateFn);
    }

    if (!validateFn(data)) {
      const errors = this.ajv.errorsText(validateFn.errors, { separator: '\n    ' });
      throw new Error(`[${label}] Schema validation failed:\n    ${errors}`);
    }
    console.log(`  ✓ ${label} validated.`);
  }
}

/**
 * Strictly Typed Mappers
 */
class CitationMapper {
  public static cslToCffReference(item: CslItem): Reference {
    const authors: Person[] = (item.author?.map(a => {
      if (!a.family && !a.literal) return null;
      const person: Person = {
        'family-names': a.family || a.literal || 'Unknown'
      };
      if (a.given?.trim()) person['given-names'] = a.given.trim();
      if (a.affiliation) person.affiliation = a.affiliation;
      if (a.orcid) {
        const normalized = normalize.orcid(a.orcid);
        if (normalized) person.orcid = normalized;
      }
      return person;
    }).filter((p): p is Person => p !== null) || []);

    const uniqueAuthors = authors.filter((a, i, self) => 
      i === self.findIndex(t => JSON.stringify(t) === JSON.stringify(a))
    );

    const ref: Reference = {
      type: item.type === 'article-journal' ? 'article' : 'generic',
      title: item.title,
      authors: uniqueAuthors
    };

    const doi = normalize.doi(item.DOI);
    if (doi) ref.doi = doi;

    const url = normalize.url(item.URL);
    if (url) ref.url = url;

    if (item.volume) ref.volume = item.volume.toString();
    if (item.issue) ref.issue = item.issue.toString();
    if (item['container-title']) ref.journal = item['container-title'];
    
    if (item.page) {
      const parts = item.page.split(/[-–—]/);
      if (parts[0]) ref['loc-start'] = parts[0].trim();
      if (parts[1]) ref['loc-end'] = parts[1].trim();
    }

    const year = item.issued?.['date-parts']?.[0]?.[0];
    if (year) ref.year = year;

    return ref;
  }

  private static formatCffReference(ref: Reference): string {
    const authors = (ref.authors || [])
      .map(a => `${a['family-names']}, ${a['given-names'] || ''}`.trim().replace(/,$/, ''))
      .join(', ');
    const year = ref.year ? `(${ref.year}). ` : '';
    const journal = ref.journal ? `. ${ref.journal}` : '';
    const vol = ref.volume ? `, ${ref.volume}` : '';
    const issue = ref.issue ? `(${ref.issue})` : '';
    const pages = (ref['loc-start'] || ref['loc-end']) 
      ? `, ${ref['loc-start'] || ''}-${ref['loc-end'] || ''}` 
      : '';
    const identifier = ref.doi ? `. DOI: ${ref.doi}` : (ref.url ? `. URL: ${ref.url}` : '');

    return `${authors} ${year}${ref.title}${journal}${vol}${issue}${pages}${identifier}.`.replace(/\.\./g, '.');
  }

  public static cffToZenodo(cff: CitationFileFormat, version: string, existing?: any): any {
    const zenodo: any = {
      ...existing,
      title: cff.title,
      description: cff.abstract || cff.title,
      version: version,
      publication_date: new Date().toISOString().split('T')[0],
      creators: cff.authors.map(a => ({
        name: `${a['family-names']}, ${a['given-names'] || ''}`.trim().replace(/,$/, ''),
        affiliation: a.affiliation,
        orcid: normalize.orcid(a.orcid)?.replace(/.*orcid.org\//, '')
      })),
      keywords: cff.keywords || existing?.keywords || [],
      upload_type: existing?.upload_type || 'publication',
      publication_type: existing?.publication_type || 'preprint',
      access_right: existing?.access_right || 'open',
      license: cff.license || existing?.license || 'cc-by-4.0',
      language: (cff as any).language || 'eng',
      references: (cff.references || []).map(ref => this.formatCffReference(ref))
    };

    if (cff['repository-code']) {
      zenodo.related_identifiers = [
        ...(existing?.related_identifiers || []),
        {
          identifier: cff['repository-code'],
          relation: 'isSupplementTo',
          resource_type: 'software'
        }
      ];
    }

    return zenodo;
  }
}

/**
 * Metadata Orchestration Pipeline
 */
export class MetadataPipeline {
  private validator = new ValidationEngine();
  private encoder = new BibtexEncoder();

  public sync(version: string): void {
    this.cleanup();
    console.log(`  Initiating professional metadata sync v${version}...`);

    const cslData = this.loadCsl();
    
    // 1. Bibliography (Encoded for LaTeX build)
    this.syncBibtex(cslData);

    // 2. Project Identity (CFF root remains Source of Truth)
    const cff = this.syncCff(cslData, version);

    // 3. Output Records
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
    // Ensure build directory exists for pdflatex
    if (!existsSync(PATHS.BUILD)) {
      mkdirSync(PATHS.BUILD, { recursive: true });
    }
  }

  private loadCsl(): CslItem[] {
    if (!existsSync(PATHS.CSL)) throw new Error(`Missing source: ${PATHS.CSL}`);
    return JSON.parse(readFileSync(PATHS.CSL, 'utf8'));
  }

  private syncBibtex(items: CslItem[]): void {
    // Encode every bibliographic field for LaTeX compatibility
    const encodedItems = items.map(item => ({
      ...item,
      title: this.encoder.encode(item.title),
      'container-title': item['container-title'] ? this.encoder.encode(item['container-title']) : undefined,
      publisher: item.publisher ? this.encoder.encode(item.publisher) : undefined,
      note: item.note ? this.encoder.encode(item.note) : undefined,
      abstract: item.abstract ? this.encoder.encode(item.abstract) : undefined
    }));

    const bib = exportBibtex(encodedItems);
    writeFileSync(PATHS.BIB, bib);
    console.log(`  ✓ ${PATHS.BIB} generated with character encoding.`);
  }

  private syncCff(items: CslItem[], version: string): CitationFileFormat {
    if (!existsSync(PATHS.CFF)) throw new Error(`Missing identity root: ${PATHS.CFF}`);
    const cff = parseYaml(readFileSync(PATHS.CFF, 'utf8')) as CitationFileFormat;

    cff.version = version;
    cff['date-released'] = new Date().toISOString().split('T')[0];
    cff.references = items.map(CitationMapper.cslToCffReference);

    writeFileSync(PATHS.CFF, stringifyYaml(cff));
    this.validator.validate(cff, PATHS.CFF_SCHEMA, 'CITATION.cff');
    return cff;
  }

  private syncZenodo(cff: CitationFileFormat, version: string): void {
    const zenodo = CitationMapper.cffToZenodo(cff, version);
    writeFileSync(PATHS.ZENODO, JSON.stringify(zenodo, null, 2) + '\n');
    this.validator.validate(zenodo, PATHS.ZENODO_SCHEMA, '.zenodo.json');
  }
}

/**
 * Entry Point for Task Orchestration
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
