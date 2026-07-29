# Zenodo GitHub Integration Error & Migration to GitHub Actions

## Research Document — 2026-07-29

---

## 1. Root Cause Analysis: "Record has no file omega-pcf/04-mersenne-cr-v0.2.1.zip"

### What Happens During a Zenodo GitHub Integration Webhook

The Zenodo-GitHub-Integration works as follows (from the [official documentation](https://rue-a.github.io/github-zenodo-integration/documentation/)):

> "As soon as a connection between a GitHub repository and Zenodo is established, each new release of the GitHub repository causes the Zenodo integration software (Zenodo agent) to download the repository as a compressed ZIP archive and to publish it subsequently on Zenodo as a new record (or a new version if a record was already created by a previous release)."

**The Zenodo agent does NOT download release assets.** It only downloads the auto-generated zipball from GitHub. This is confirmed by multiple GitHub issues:

- [zenodo/zenodo#1235](https://github.com/zenodo/zenodo/issues/1235) (2017): "It's common for GitHub releases to include release 'assets'. Since the zipball of the source code is already downloaded, it might be also worth looking at downloading and including the assets in the produced record."
- [zenodo/zenodo#1728](https://github.com/zenodo/zenodo/issues/1728) (2019): "With Zenodo integration turned on, creating the release triggers archiving of the Source code files, but **not** the extra assets."

### The Error: "Record has no file omega-pcf/04-mersenne-cr-v0.2.1.zip"

The filename `omega-pcf/04-mersenne-cr-v0.2.1.zip` matches GitHub's zipball naming convention: `{owner}/{repo}-{tag}.zip`. The Zenodo agent constructs this filename, then tries to download the zipball from:

```
https://api.github.com/repos/omega-pcf/04-mersenne-cr/zipball/v0.2.1
```

**Why the download fails:**

1. **Transient infrastructure issues**: The Zenodo agent runs on Zenodo's servers. If there's a network timeout, rate limiting from GitHub API, or Zenodo-side processing error, the zip download can fail silently, resulting in "Record has no file" with no files attached.

2. **GitHub API rate limiting**: The zipball URL (`api.github.com/repos/.../zipball/...`) is subject to GitHub's API rate limits (60 requests/hour for unauthenticated requests). The Zenodo agent authenticates with its own GitHub app, but rate limits can still occur during high-traffic periods.

3. **Timing/race condition**: The webhook fires immediately when the release is published. If the GitHub API hasn't finished generating the zipball yet (which is usually instantaneous but can lag), the download fails.

4. **The error message is misleading**: "Record has no file" means the Zenodo record was created (a new draft), but the zip upload step failed, leaving the record empty. This is a known issue — Zenodo creates the record before confirming the file download succeeded.

### Why the Release Assets Are Irrelevant

The `.release-it.ts` config shows:
```typescript
github: {
    release: true,
    assets: ['build/document-v*.pdf', 'checksums.txt'],
}
```

This uploads `document-v0.2.0.pdf` and `checksums.txt` as GitHub release assets. But the Zenodo webhook **ignores release assets entirely**. It only tries to download the auto-generated zipball. The `assets: []` in the webhook payload is expected and correct.

### Key Insight

The Zenodo GitHub integration is fundamentally limited:
- **Only downloads the source code zipball** — never release assets
- **Cannot include PDFs, checksums, or other artifacts** in the Zenodo record
- **No control over metadata beyond `.zenodo.json`/`CITATION.cff`**
- **No way to pre-reserve DOIs** before publishing
- **Cannot link to an existing Zenodo Concept DOI** (per the documentation: "It is not possible to link a GitHub repository with an existing Zenodo record")

---

## 2. Migration Path: GitHub Actions + Zenodo REST API

### 2.1 Get a Zenodo API Token

1. Log in to https://zenodo.org/
2. Go to **https://zenodo.org/account/settings/applications/**
3. Click **"New token"**
4. Give it a name like `omega-pcf-github-actions`
5. Select these scopes:
   - ✅ `deposit:write` — Grants write access to depositions
   - ✅ `deposit:actions` — Grants access to publish, edit, and discard edits
6. Click **"Create"**
7. **Copy the token immediately** — it won't be shown again

### 2.2 Store Token as GitHub Actions Secret

1. Go to the GitHub repository: https://github.com/omega-pcf/04-mersenne-cr
2. Navigate to **Settings → Secrets and variables → Actions**
3. Click **"New repository secret"**
4. Name: `ZENODO_TOKEN`
5. Value: (paste the token from step 1.7)
6. Click **"Add secret"**

### 2.3 GitHub Action Workflow YAML

Create `.github/workflows/zenodo-deposit.yml`:

```yaml
name: Deposit to Zenodo

on:
  release:
    types: [published]

jobs:
  deposit:
    runs-on: ubuntu-latest
    name: Upload release to Zenodo
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Download release source zip
        run: |
          # Download the source code zipball from GitHub
          curl -L \
            -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            -o source.zip \
            "https://api.github.com/repos/${{ github.repository }}/zipball/${{ github.event.release.tag_name }}"

      - name: Create new Zenodo deposition
        id: zenodo
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          # Create a new empty deposition
          RESPONSE=$(curl -s -X POST \
            "https://zenodo.org/api/deposit/depositions" \
            -H "Authorization: Bearer $ZENODO_TOKEN" \
            -H "Content-Type: application/json" \
            -d '{}')
          
          DEPOSITION_ID=$(echo "$RESPONSE" | jq -r '.id')
          BUCKET_URL=$(echo "$RESPONSE" | jq -r '.links.bucket')
          
          echo "deposition_id=$DEPOSITION_ID" >> "$GITHUB_OUTPUT"
          echo "bucket_url=$BUCKET_URL" >> "$GITHUB_OUTPUT"
          
          echo "Created deposition $DEPOSITION_ID"
          echo "Bucket URL: $BUCKET_URL"

      - name: Upload source zip to Zenodo
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          BUCKET_URL="${{ steps.zenodo.outputs.bucket_url }}"
          
          curl -s -X PUT \
            "${BUCKET_URL}/source.zip" \
            -H "Authorization: Bearer $ZENODO_TOKEN" \
            --data-binary @source.zip

      - name: Download PDF from release assets
        run: |
          # Find the PDF asset in the release
          ASSETS_URL="${{ github.event.release.upload_url }}"
          ASSETS_URL="${ASSETS_URL%{\?name}*}"
          
          # List release assets and find the PDF
          curl -s \
            -H "Authorization: token ${{ secrets.GITHUB_TOKEN }}" \
            -H "Accept: application/vnd.github.v3+json" \
            "${{ github.event.release.assets_url }}" | \
            jq -r '.[] | select(.name | test("\\.pdf$")) | .browser_download_url' | \
            head -1 | \
            xargs -I{} curl -L -o document.pdf "{}"
          
          # If no PDF found, skip this step
          if [ ! -f document.pdf ]; then
            echo "No PDF found in release assets, skipping PDF upload"
          fi

      - name: Upload PDF to Zenodo (if available)
        if: hashFiles('document.pdf') != ''
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          BUCKET_URL="${{ steps.zenodo.outputs.bucket_url }}"
          
          curl -s -X PUT \
            "${BUCKET_URL}/document.pdf" \
            -H "Authorization: Bearer $ZENODO_TOKEN" \
            --data-binary @document.pdf

      - name: Set Zenodo metadata
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          DEPOSITION_ID="${{ steps.zenodo.outputs.deposition_id }}"
          RELEASE_TAG="${{ github.event.release.tag_name }}"
          # Strip leading 'v' from tag
          VERSION="${RELEASE_TAG#v}"
          
          # Extract metadata from .zenodo.json
          METADATA=$(jq -n \
            --arg title "$(jq -r '.title' .zenodo.json)" \
            --arg description "$(jq -r '.description' .zenodo.json)" \
            --arg version "$VERSION" \
            --arg date "$(date -u +%Y-%m-%d)" \
            --argjson creators "$(jq -c '.creators' .zenodo.json)" \
            --argjson keywords "$(jq -c '.keywords' .zenodo.json)" \
            --arg license "$(jq -r '.license' .zenodo.json)" \
            '{
              metadata: {
                title: $title,
                upload_type: "software",
                publication_date: $date,
                description: $description,
                version: $version,
                creators: $creators,
                keywords: $keywords,
                access_right: "open",
                license: $license,
                language: "eng",
                related_identifiers: [
                  {
                    identifier: ("https://github.com/" + env.GITHUB_REPOSITORY),
                    relation: "isSupplementTo",
                    resource_type: "software"
                  },
                  {
                    identifier: ("https://github.com/" + env.GITHUB_REPOSITORY + "/releases/tag/" + $version),
                    relation: "isSupplementTo",
                    resource_type: "software"
                  }
                ]
              }
            }')
          
          curl -s -X PUT \
            "https://zenodo.org/api/deposit/depositions/${DEPOSITION_ID}" \
            -H "Authorization: Bearer $ZENODO_TOKEN" \
            -H "Content-Type: application/json" \
            -d "$METADATA"
          
          echo "Metadata set for deposition $DEPOSITION_ID"

      - name: Publish Zenodo deposition
        env:
          ZENODO_TOKEN: ${{ secrets.ZENODO_TOKEN }}
        run: |
          DEPOSITION_ID="${{ steps.zenodo.outputs.deposition_id }}"
          
          RESPONSE=$(curl -s -X POST \
            "https://zenodo.org/api/deposit/depositions/${DEPOSITION_ID}/actions/publish" \
            -H "Authorization: Bearer $ZENODO_TOKEN")
          
          DOI=$(echo "$RESPONSE" | jq -r '.doi // .metadata.prereserve_doi.doi // "unknown"')
          DOI_URL=$(echo "$RESPONSE" | jq -r '.doi_url // "unknown"')
          RECORD_ID=$(echo "$RESPONSE" | jq -r '.record_id // "unknown"')
          
          echo "Published deposition $DEPOSITION_ID"
          echo "DOI: $DOI"
          echo "DOI URL: $DOI_URL"
          echo "Record ID: $RECORD_ID"
          
          # Export for use in subsequent steps
          echo "doi=$DOI" >> "$GITHUB_OUTPUT"
          echo "doi_url=$DOI_URL" >> "$GITHUB_OUTPUT"
          echo "record_id=$RECORD_ID" >> "$GITHUB_OUTPUT"
```

### 2.4 Simplified Version (Using Existing Action)

For a simpler setup using the [`megasanjay/upload-to-zenodo`](https://github.com/megasanjay/upload-to-zenodo) action:

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
        uses: megasanjay/upload-to-zenodo@v2.0.1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          zenodo_token: ${{ secrets.ZENODO_TOKEN }}
          zenodo_deposition_id: YOUR_DEPOSITION_ID
          zenodo_publish: true
          zenodo_sandbox: false
          update_metadata_files: false
          zenodo_json: true
      - name: Get the DOI
        run: echo "DOI was ${{ steps.release.outputs.doi }}"
```

**Note**: The `upload-to-zenodo` action only uploads the source code zip (it downloads the zipball from GitHub). To upload additional files (like the PDF), you'd need to extend it or use the custom workflow above.

### 2.5 Handling Concept DOIs (Versioning)

The Zenodo REST API supports versioning via the `newversion` action:

**For the first release:**
- Create a new deposition → it automatically gets a Concept DOI
- Publish it → the Concept DOI and a version-specific DOI are both active

**For subsequent releases:**
1. GET the latest version's deposition ID:
   ```bash
   curl -s "https://zenodo.org/api/records/${RECORD_ID}" \
     -H "Authorization: Bearer $ZENODO_TOKEN" | \
     jq -r '.links.latest_draft'
   ```

2. Create a new version:
   ```bash
   curl -s -X POST \
     "https://zenodo.org/api/deposit/depositions/${LATEST_DEPOSITION_ID}/actions/newversion" \
     -H "Authorization: Bearer $ZENODO_TOKEN"
   ```

3. Get the new draft's deposition ID from the response's `links.latest_draft`

4. Delete old files, upload new files, update metadata, publish

**Automatic approach** (recommended): Zenodo automatically creates a new version when you try to publish a deposition that's already published. The REST API's `newversion` action handles this.

**Storing the Concept DOI:**
- After the first release, the Concept DOI is minted
- Store it in `.zenodo.json` or as a GitHub Actions variable
- Use it in the `related_identifiers` metadata for subsequent versions

### 2.6 Disabling the Zenodo GitHub Integration Webhook

**YES, you should disable it.** Otherwise you'll get duplicate records on Zenodo for each release.

To disable:
1. Go to https://zenodo.org/account/settings/github/
2. Find the `omega-pcf/04-mersenne-cr` repository
3. Toggle the integration **OFF**
4. Confirm the disconnection

The documentation explicitly warns:
> "Remember to remove the webhook from your repository before using this action. Otherwise, you will have two releases on Zenodo for every release on GitHub."

---

## 3. Benefits of the GitHub Actions Approach

### 3.1 PDF Visible on GitHub Release Page

With the current webhook approach, the PDF is uploaded as a GitHub release asset (via `.release-it.ts` `assets` config), but Zenodo never picks it up. The PDF is visible on the GitHub release page but not on Zenodo.

With the GitHub Actions approach:
- The PDF is downloaded from the release and uploaded to Zenodo as a separate file
- Both the source zip AND the PDF appear on the Zenodo record page
- Users can download either file directly from Zenodo

### 3.2 Source Zip + PDF Both Uploaded to Zenodo

The Zenodo webhook only uploads the auto-generated source code zip. With the REST API approach:
- Source code zip: uploaded via the bucket API
- PDF document: uploaded as a separate file
- Checksums: can be uploaded as well
- Any other artifacts: all uploaded

### 3.3 No Dependency on Zenodo's Webhook Timing

The webhook approach has several timing issues:
- Zenodo's agent may take minutes to hours to process the webhook
- The webhook can fail silently (as we've seen)
- No retry mechanism visible to the user
- No way to know if the archiving succeeded

The GitHub Actions approach:
- Runs immediately after the release is published
- Fails visibly in the GitHub Actions tab
- Can be manually re-run
- Provides clear success/failure status

### 3.4 Better Control Over Metadata

The webhook approach:
- Metadata comes from `.zenodo.json` or `CITATION.cff` only
- Cannot dynamically generate metadata based on the release
- Cannot include release-specific information (changelog, etc.)

The GitHub Actions approach:
- Full control over metadata via the REST API
- Can generate metadata dynamically
- Can include `related_identifiers` pointing to the exact release
- Can set `publication_date` to the exact release date
- Can include custom keywords, descriptions, etc.

### 3.5 Pre-reserve DOIs

The REST API supports `prereserve_doi: true` to get a DOI before publishing:
```json
{
  "metadata": {
    "prereserve_doi": true
  }
}
```

This is useful if you want to include the DOI in the source code (e.g., in a CITATION.cff) before publishing.

---

## 4. Configuration Needed

### 4.1 GitHub Actions Secrets

| Secret | Description |
|--------|-------------|
| `ZENODO_TOKEN` | Zenodo personal access token with `deposit:write` and `deposit:actions` scopes |

### 4.2 Files in Repository

- `.zenodo.json` — Metadata file (already exists)
- `CITATION.cff` — Citation metadata (already exists)
- `.github/workflows/zenodo-deposit.yml` — GitHub Actions workflow (to be created)

### 4.3 Zenodo Settings

- Disable the GitHub integration webhook for `omega-pcf/04-mersenne-cr`
- Ensure the Zenodo account has API access enabled

---

## 5. Migration Checklist

- [ ] Generate Zenodo API token at https://zenodo.org/account/settings/applications/
- [ ] Add `ZENODO_TOKEN` as a GitHub repository secret
- [ ] Create `.github/workflows/zenodo-deposit.yml` workflow
- [ ] Test with a patch release (e.g., `v0.2.2`)
- [ ] Verify the Zenodo record contains both source zip and PDF
- [ ] Disable the Zenodo GitHub integration webhook
- [ ] Update README.md with the new Zenodo DOI badge (if DOI changes)

---

## 6. References

- [Zenodo REST API Documentation](https://developers.zenodo.org/)
- [Zenodo-GitHub-Integration Documentation](https://rue-a.github.io/github-zenodo-integration/documentation/)
- [Zenodo Support: Why does my GitHub release fail?](https://support.zenodo.org/help/en-gb/24-github-integration/204-why-does-my-github-release-fail-with-an-error)
- [megasanjay/upload-to-zenodo Action](https://github.com/megasanjay/upload-to-zenodo)
- [zenodo/zenodo#1235: Inclusion of release assets](https://github.com/zenodo/zenodo/issues/1235)
- [zenodo/zenodo#1728: Not depositing additional assets](https://github.com/zenodo/zenodo/issues/1728)
