export interface CitationFile {
  'cff-version': string;
  message?: string;
  title: string;
  version: string;
  'date-released': string;
  authors: Author[];
  'repository-code'?: string;
  license?: string | string[];
  keywords?: string[];
  languages?: string[];
  abstract?: string;
}

export interface Author {
  'family-names': string;
  'given-names': string;
  orcid?: string;
  affiliation?: string;
  email?: string;
}

export interface ZenodoMetadata {
  title: string;
  version: string;
  upload_type: string;
  publication_type?: string;
  description: string;
  creators: ZenodoCreator[];
  access_right: string;
  license: string;
  language: string;
  keywords: string[];
  publication_date?: string;
  communities?: Array<{ identifier: string }>;
  related_identifiers?: RelatedIdentifier[];
  repository_url?: string;
}

export interface ZenodoCreator {
  name: string;
  affiliation?: string;
  orcid?: string;
}

export interface RelatedIdentifier {
  identifier: string;
  relation: string;
  scheme: string;
  resource_type: string;
}

export interface ReleaseConfig {
  version: string;
  buildDir: string;
  sourceTex: string;
  outputPdf: string;
  checksumsFile: string;
}

