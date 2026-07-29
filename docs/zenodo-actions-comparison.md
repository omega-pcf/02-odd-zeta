# GitHub Actions for Zenodo Deposition — Detailed Comparison

## Research Date: 2026-07-29

---

## 1. Action Comparison Table

| Feature | `megasanjay/upload-to-zenodo` | `rseng/zenodo-release` | `nmfs-opensci/zenodo-gha` | `zenodraft/action` | `DiamondLightSource/zenodo-uploader` |
|---------|-------------------------------|------------------------|---------------------------|---------------------|-------------------------------------|
| **GitHub Stars** | 12 | 12 | 3 | 7 | 3 |
| **Last Updated** | 2026-02-10 | 2025-05-07 | 2025-02-12 | 2024-02-08 | 2020-03-30 ⚠️ |
| **Language** | Node.js 16 ⚠️ | Python (composite) | Python (composite) | Node.js 20 | Python (standalone lib) |
| **Open Issues** | 7 | 4 | 2 | 17 ⚠️ | 1 |
| **Action Type** | Official GH Action | Composite action | Composite action | Official GH Action | ❌ Not an action |
| **Upload Source Zip** | ✅ Yes (zipball) | ✅ Yes (archive) | ✅ Yes (zipball) | ✅ Yes (zipball or tar.gz) | N/A |
| **Upload Additional Files (PDF)** | ✅ Yes (all release assets) | ❌ Single archive only | ❌ Single archive only | ✅ Yes (filenames input) | N/A |
| **Concept DOI Versioning** | ✅ Yes (via deposition_id) | ✅ Yes (via --doi) | ✅ Yes (via doi input) | ✅ Yes (via concept input) | ❌ No |
| **Update CITATION.cff** | ✅ Yes | ❌ No | ❌ No (but reads it) | ✅ Yes (upsert-doi) | ❌ No |
| **Update .zenodo.json** | ✅ Yes | ❌ No | ❌ No (but reads it) | ❌ No | ❌ No |
| **Update codemeta.json** | ✅ Yes | ❌ No | ❌ No | ❌ No | ❌ No |
| **Metadata from file** | Via .zenodo.json | Via --zenodo-json | Via zenodo_json input | Via --metadata | Via JSON file |
| **Publish Automatically** | Configurable | Always | Always | Configurable | Manual |
| **Sandbox Support** | ✅ Yes | ❌ No | ❌ No | ✅ Yes | ✅ Yes |
| **Outputs DOI** | ✅ doi, version | ✅ doi, badge, conceptdoi, etc. | ✅ doi, badge, conceptdoi, etc. | ✅ doi, record_id, etc. | N/A |

---

## 2. Detailed Analysis of Each Action

### 2.1 `megasanjay/upload-to-zenodo` (⭐ 12, Most Feature-Complete)

**What it does (from source code analysis):**

1. Downloads metadata files (CITATION.cff, .zenodo.json, codemeta.json) from the repo
2. Downloads ALL GitHub release assets (PDF, checksums, etc.) to a local folder
3. Creates a new version on Zenodo via `POST /api/deposit/depositions/{id}/actions/newversion`
4. Deletes all files from the new draft version
5. Updates metadata files locally (version, DOI, publication_date) and commits them back to GitHub
6. Downloads the updated zipball (now containing updated CITATION.cff etc.)
7. **Uploads ALL files from the release assets folder** (source zip + PDF + checksums) to Zenodo bucket
8. Optionally publishes the deposition

**Key code flow (src/index.js):**
```javascript
// Downloads release assets (PDF, checksums, etc.)
await downloadReleaseAssets(context_object, releaseAssetsFolderPath);

// Creates new version on Zenodo
const deposition_id = await createNewZenodoDepositionVersion(context_object, ZENODO_TOKEN);

// Gets the bucket URL for file uploads
const bucket_url = deposition.links.bucket;

// Uploads ALL files in release-assets folder
for (const file of files_in_release_assets_folder) {
    await uploadFileToZenodo(context_object, deposition_id, ZENODO_TOKEN, bucket_url, file, file_path);
}
```

**Pros:**
- ✅ **Uploads multiple files** (source zip + PDF + checksums)
- ✅ Updates CITATION.cff, .zenodo.json, codemeta.json with new version/DOI
- ✅ Commits metadata changes back to GitHub
- ✅ Handles concept DOI versioning
- ✅ Most actively maintained (updated Feb 2026)
- ✅ Has sandbox support

**Cons:**
- ⚠️ **Uses Node.js 16** (EOL) — will need updating to Node.js 20
- ⚠️ Requires `zenodo_deposition_id` input (must store the initial deposition ID)
- ⚠️ 7 open issues — some may be bugs
- ⚠️ Complex setup with many inputs
- ⚠️ Commits metadata changes back to repo (may not be desired)

---

### 2.2 `rseng/zenodo-release` (⭐ 12, Simple & Reliable)

**What it does (from deploy.py source analysis):**

1. Takes a single archive file path as input
2. If `--doi` is provided, finds the existing deposit and creates a new version
3. If no DOI, creates a new deposition (requires .zenodo.json)
4. Uploads the single archive file via bucket PUT
5. Sets metadata from .zenodo.json + version + publication_date
6. Optionally adds `related_identifiers` with the GitHub release URL
7. Publishes the deposition

**Key code flow (scripts/deploy.py):**
```python
def upload_archive(archive, version, html_url=None, zenodo_json=None, doi=None, ...):
    cli = Zenodo(sandbox=sandbox)
    
    if doi:
        upload = cli.update_doi(doi=doi)  # Creates new version
    else:
        upload = cli.new_doi()  # Creates new deposition
    
    # Upload single archive file
    for path in glob(archive):
        cli.upload_archive(upload, path)
    
    # Set metadata
    data = cli.upload_metadata(upload, zenodo_json, version, html_url, ...)
    
    # Publish
    cli.publish(data)
```

**Pros:**
- ✅ Simple, clean Python implementation
- ✅ Handles concept DOI versioning (via `update_doi` → `newversion`)
- ✅ Clean outputs (doi, badge, conceptdoi, record, etc.)
- ✅ Supports description override (text or file)
- ✅ Used by nmfs-opensci/zenodo-gha (fork/improvement)

**Cons:**
- ❌ **Only uploads a single archive** — no support for additional files (PDF)
- ❌ No metadata file updates (CITATION.cff, .zenodo.json)
- ❌ No sandbox support
- ⚠️ Requires `archive` input (must create zip before calling action)
- ⚠️ Last updated May 2025

---

### 2.3 `nmfs-opensci/zenodo-gha` (⭐ 3, Fork of rseng)

**What it does:**

This is a **composite action** that wraps `rseng/zenodo-release`'s `deploy.py` script with additional features:

1. Downloads the release zipball automatically (no need to provide archive path)
2. If `zenodo_json` input is "CITATION.cff", converts it to zenodo.json format using `cffconvert`
3. Runs the same deploy.py script as rseng/zenodo-release
4. Adds release name and body to the metadata

**Key difference from rseng:** Automatically downloads the zipball and supports CITATION.cff → zenodo.json conversion.

**Pros:**
- ✅ Auto-downloads zipball (simpler workflow)
- ✅ Supports CITATION.cff conversion to zenodo.json
- ✅ Composite action (no Node.js dependency)
- ✅ Recently maintained (Feb 2025)

**Cons:**
- ❌ **Only uploads a single archive** — no support for additional files (PDF)
- ❌ No metadata file updates
- ❌ No sandbox support
- ⚠️ Only 3 stars, less community adoption

---

### 2.4 `zenodraft/action` (⭐ 7, Most Flexible Upload)

**What it does (from action.yml):**

1. Can upload either a zipball/tar.gz of the entire repo, OR specific files
2. The `filenames` input accepts a space-separated list of files to upload
3. Can create new versions via `concept` input
4. Can update CITATION.cff with pre-reserved DOI before upload
5. Supports sandbox (defaults to true!)

**Key feature — multiple file upload:**
```yaml
filenames:
  description: List of space-separated filenames that should be uploaded
  # Can specify: "source.zip document.pdf checksums.txt"
```

**Pros:**
- ✅ **Can upload multiple specific files** via `filenames` input
- ✅ Updates CITATION.cff with pre-reserved DOI
- ✅ Supports concept DOI versioning
- ✅ Sandbox support (default: true)
- ✅ Node.js 20 (current)

**Cons:**
- ❌ **17 open issues** — suggests maintenance problems
- ❌ Last updated Feb 2024 (2+ years ago)
- ❌ No automatic release asset downloading
- ❌ No .zenodo.json or codemeta.json updates
- ⚠️ Less documentation/examples

---

### 2.5 `DiamondLightSource/zenodo-uploader` (⚠️ Not a GitHub Action)

**What it actually is:** A standalone Python library for uploading to Zenodo. **NOT a GitHub Action** — has no `action.yml` file.

**What it does:**
- Creates new depositions
- Uploads multiple files
- Sets basic metadata (title, description, creators, keywords)
- Validates metadata structure

**Cons:**
- ❌ **Not a GitHub Action** — cannot be used with `uses:`
- ❌ No concept DOI versioning
- ❌ No CITATION.cff/.zenodo.json support
- ❌ Last updated March 2020 (6+ years ago)
- ❌ Very basic metadata support

---

## 3. Zenodo REST API Flow for Multiple Files

The Zenodo REST API supports uploading multiple files to a single deposition:

```
1. Create deposition (or create new version)
   POST /api/deposit/depositions
   
2. Get bucket URL from response
   response.links.bucket → "https://zenodo.org/api/files/{bucket_id}"

3. Upload file 1 (source zip)
   PUT {bucket_url}/source.zip
   Body: binary file content

4. Upload file 2 (PDF)
   PUT {bucket_url}/document.pdf
   Body: binary file content

5. Upload file 3 (checksums)
   PUT {bucket_url}/checksums.txt
   Body: binary file content

6. Set metadata
   PUT /api/deposit/depositions/{id}
   Body: { "metadata": { ... } }

7. Publish
   POST /api/deposit/depositions/{id}/actions/publish
```

**Key insight:** The bucket API accepts any filename — you can PUT as many files as you want. The filename in the URL becomes the displayed filename on Zenodo.

---

## 4. Recommendation

### Option A: Use `megasanjay/upload-to-zenodo` (Recommended)

**Why:** It's the only well-maintained action that:
1. ✅ Uploads multiple files (source zip + PDF + checksums)
2. ✅ Handles concept DOI versioning
3. ✅ Updates CITATION.cff, .zenodo.json, codemeta.json
4. ✅ Commits metadata changes back to GitHub
5. ✅ Most actively maintained (Feb 2026)

**Workflow:**
```yaml
name: Release on Zenodo
on:
  release:
    types: [published]

jobs:
  upload-to-zenodo:
    runs-on: ubuntu-latest
    steps:
      - name: Upload to Zenodo
        id: release
        uses: megasanjay/upload-to-zenodo@main  # or specific version
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          zenodo_token: ${{ secrets.ZENODO_TOKEN }}
          zenodo_deposition_id: ${{ vars.ZENODO_DEPOSITION_ID }}
          zenodo_publish: true
          zenodo_sandbox: false
          update_metadata_files: true  # Updates CITATION.cff, .zenodo.json
          citation_cff: true
          zenodo_json: true
          codemeta_json: true
      - name: Get the DOI
        run: echo "DOI was ${{ steps.release.outputs.doi }}"
```

**Prerequisites:**
- Store initial `zenodo_deposition_id` as a repository variable (after first release)
- Ensure CITATION.cff, .zenodo.json, codemeta.json exist in repo

**Concerns to address:**
- Node.js 16 EOL → may need to fork and update to Node.js 20
- 7 open issues → review before adopting

---

### Option B: Write a Custom Workflow (Most Control)

**Why:** If `megasanjay/upload-to-zenodo` has issues or doesn't fit perfectly:

```yaml
name: Deposit to Zenodo
on:
  release:
    types: [published]

jobs:
  deposit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Download release assets
        run: |
          # Download source zipball
          curl -L -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            -o source.zip \
            "https://api.github.com/repos/${{ github.repository }}/zipball/${{ github.event.release.tag_name }}"
          
          # Download PDF from release assets
          curl -s -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            "${{ github.event.release.assets_url }}" | \
            jq -r '.[] | select(.name | test("\\.pdf$")) | .browser_download_url' | \
            head -1 | xargs -I{} curl -L -o document.pdf "{}"
      
      - name: Upload to Zenodo
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          # Create new version (or new deposition)
          RESPONSE=$(curl -s -X POST \
            "https://zenodo.org/api/deposit/depositions/${DEPOSITION_ID}/actions/newversion" \
            -H "Authorization: Bearer $ZENODO_TOKEN")
          
          NEW_ID=$(echo "$RESPONSE" | jq -r '.links.latest_draft' | grep -o '[0-9]*$')
          BUCKET=$(curl -s "https://zenodo.org/api/deposit/depositions/$NEW_ID" \
            -H "Authorization: Bearer $ZENODO_TOKEN" | jq -r '.links.bucket')
          
          # Upload multiple files
          curl -X PUT "$BUCKET/source.zip" -H "Authorization: Bearer $ZENODO_TOKEN" --data-binary @source.zip
          curl -X PUT "$BUCKET/document.pdf" -H "Authorization: Bearer $ZENODO_TOKEN" --data-binary @document.pdf
          
          # Set metadata and publish...
```

**Pros:**
- Full control over every step
- No dependency on third-party actions
- Easy to debug and customize

**Cons:**
- More code to maintain
- Need to handle error cases yourself
- Need to store/manage DEPOSITION_ID

---

### Option C: Hybrid — Custom Workflow + `rseng/zenodo-release` Script

**Why:** Use the well-tested `deploy.py` from rseng/zenodo-release directly, extended to upload multiple files:

```yaml
- name: Upload to Zenodo
  run: |
    # Clone the deploy script
    git clone --depth 1 https://github.com/rseng/zenodo-release.git /tmp/zenodo-release
    
    # Upload multiple files by calling the script for each
    python /tmp/zenodo-release/scripts/deploy.py upload \
      "source.zip document.pdf" \
      --version "${{ github.event.release.tag_name }}" \
      --zenodo-json .zenodo.json \
      --doi "${{ vars.ZENODO_CONCEPT_DOI }}"
```

**Note:** The `deploy.py` script uses `glob(archive)` for the archive path, so it can accept multiple files if passed as a glob pattern. However, this is a hack — the script was designed for a single archive.

---

## 5. Final Recommendation

**For omega-pcf's 4 repositories, I recommend:**

1. **Start with `megasanjay/upload-to-zenodo`** — it handles all requirements:
   - Multiple file upload (source zip + PDF + checksums)
   - Concept DOI versioning
   - CITATION.cff/.zenodo.json updates
   - Most actively maintained

2. **If issues arise, fork and fix** — the Node.js 16 EOL is a known concern. Fork the repo, update to Node.js 20, and use the fork.

3. **For maximum control, write a custom workflow** — using the Zenodo REST API directly (as outlined in the existing migration doc). This is ~50 lines of bash and gives full control.

4. **Do NOT use:**
   - `DiamondLightSource/zenodo-uploader` — not a GitHub Action, abandoned
   - `zenodraft/action` — 17 open issues, not maintained
   - `rseng/zenodo-release` — single file only, no PDF support

---

## 6. Files Created/Modified

- `docs/zenodo-actions-comparison.md` — This comparison document
