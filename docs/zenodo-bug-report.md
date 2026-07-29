# Zenodo Deposition Bug Report

## Error
```
Record '21662216' has no file 'omega-pcf/04-mersenne-cr-v0.2.1.zip'.
```

Affects all 4 repos: 01-hilbert-polya, 02-odd-zeta, 03-crystalline-worldsheet, 04-mersenne-cr.

## Symptoms
- Zenodo GitHub integration receives the webhook
- Creates a record (e.g. 21662216)
- Fails to attach the source zip archive
- The `zipball_url` IS present in the GitHub payload

## Evidence from Zenodo Dashboard
The CITATION.cff displayed on Zenodo is **wrong** — shows:
```
cff-version: 1.1.0
authors:
- family-names: Joe
  given-names: Johnson
orcid: @url:`https://orcid.org/0000-0000-0000-0000`
```
This is NOT our CITATION.cff (ours is 1.2.0 with 4 real authors).

## Root Cause Analysis

### Hypothesis 1: CITATION.cff parsing failure
Zenodo's CITATION.cff parser fails, falls back to a template. This could cause
the entire metadata processing to fail, preventing the zip attachment.

### Hypothesis 2: .zenodo.json metadata issue
Per Zenodo docs, `.zenodo.json` takes priority over CITATION.cff. But if
Zenodo's parser fails on either file, it may abort the entire deposition.

### Hypothesis 3: Zip file not found
Zenodo expects the source zip at a specific internal path. The zipball_url
exists but Zenodo may not be downloading it correctly.

## What worked before
The last working release was before the `fix(citation)` commits that changed
the citation pipeline (bib key replacement, institution.country cleanup,
upload_type change).

## Proposed Fix: Migrate to GitHub Actions
Instead of relying on Zenodo's webhook integration, use a GitHub Action that:
1. Creates the GitHub release with PDF + checksums as visible assets
2. Uploads source zip + PDF to Zenodo via REST API
3. Handles concept DOI versioning
4. Gives full control over metadata and timing

See: docs/zenodo-github-action-migration.md
