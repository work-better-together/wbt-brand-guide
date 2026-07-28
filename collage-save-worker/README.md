# WBT Collage Save — Worker

A tiny Cloudflare Worker that lets **collage-maker.html** save collages into the
brand-guide repo **without ever putting a GitHub token in the public page**.

## Why this exists

`brand.wbt.coach` is a static site (GitHub Pages). A static page can't hold a
write credential safely — anything in client JS is public. So the "Save to Brand
Guide" button used to embed a GitHub personal-access token, which was exposed to
anyone who viewed source. This Worker moves that token server-side: the page
POSTs the rendered collage here, and the Worker (holding the token as a secret)
commits the PNG and updates `manifest.json`. The gallery (`collages.html`) already
reads that manifest over a plain public URL, so nothing changes on the read side.

```
collage-maker.html  ──POST (collage PNG + passphrase)──▶  this Worker  ──commit──▶  wbt-brand-guide repo
                                                              (holds GITHUB_TOKEN)
```

## One-time setup

1. **Create a fine-grained GitHub token** (much narrower than the old one):
   GitHub → Settings → Developer settings → Fine-grained tokens →
   - Repository access: **Only** `work-better-together/wbt-brand-guide` (resource owner: the org)
   - Permissions: **Contents → Read and write** (nothing else)
   - Copy the token (starts with `github_pat_…`).

2. **Pick a shared passphrase** the team will type once in the collage maker
   (any hard-to-guess string).

3. **Deploy the Worker** (from this folder):
   ```sh
   npm install -g wrangler      # if you don't have it
   wrangler login
   wrangler secret put GITHUB_TOKEN     # paste the fine-grained token
   wrangler secret put SHARED_SECRET    # paste the passphrase
   wrangler deploy
   ```
   Wrangler prints the Worker URL, e.g.
   `https://wbt-collage-save.<your-subdomain>.workers.dev`.

4. **Point the page at the Worker.** In `collage-maker.html`, set:
   ```js
   const SAVE_ENDPOINT = 'https://wbt-collage-save.<your-subdomain>.workers.dev';
   ```
   (Or, if you bind the optional route in `wrangler.toml`, use the same-origin
   path `'/collage-api/save'` and CORS is unnecessary.)

5. **Commit + deploy the site.** First time anyone clicks Save, they're prompted
   for the passphrase; it's stored in their browser's localStorage after that.

## Security notes

- **Rotate both old tokens now.** The previously-embedded GitHub PAT
  (`github_pat_11ABIJW…`) and Airtable PAT (`patfBEWJ2b…`) were public — revoke
  them in GitHub and Airtable regardless of this change.
- The Worker only accepts requests carrying the correct `X-Save-Secret`, and only
  from `https://brand.wbt.coach` (CORS). It sanitizes the filename and writes only
  under `assets/Generated Illustrations/`.
- The shared passphrase is a low-friction gate, not strong auth. For stronger
  control, put the Worker behind **Cloudflare Access** (email-based) instead of /
  in addition to the shared secret.

## Files

- `worker.js` — the Worker (no secrets in source).
- `wrangler.toml` — deploy config; secrets set via CLI, not here.
