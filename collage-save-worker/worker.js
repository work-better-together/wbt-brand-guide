/**
 * WBT Collage Save — Cloudflare Worker
 *
 * Holds the GitHub write token server-side so it is NEVER exposed in the
 * public collage-maker.html page. The page POSTs a rendered collage here;
 * this Worker commits the PNG and updates manifest.json in the brand-guide repo.
 *
 * Secrets (set with `wrangler secret put`, NEVER commit these):
 *   GITHUB_TOKEN   — a fine-grained GitHub PAT with "Contents: Read and write"
 *                    on ONLY the deroyperaza/wbt-brand-guide repo.
 *   SHARED_SECRET  — a passphrase the team enters once in the collage maker.
 *                    Gates writes so the endpoint isn't open to the internet.
 *
 * Request  (POST, JSON):
 *   {
 *     "filename": "WBT-collage-clarity-20260709.png",
 *     "contentBase64": "<base64 PNG, no data: prefix>",
 *     "entry": { filename, title, concept, bgColorId, bgHex, savedAt }
 *   }
 *   Header: X-Save-Secret: <SHARED_SECRET>
 *
 * Response: 200 { ok: true, path } | 401 | 400 | 502
 */

const REPO         = 'deroyperaza/wbt-brand-guide';
const BRANCH       = 'main';
const IMG_DIR      = 'assets/Generated Illustrations';
const MANIFEST     = 'assets/Generated Illustrations/manifest.json';
const ALLOW_ORIGIN = 'https://brand.wbt.coach';

function withCors(resp) {
  resp.headers.set('Access-Control-Allow-Origin', ALLOW_ORIGIN);
  resp.headers.set('Access-Control-Allow-Methods', 'POST, OPTIONS');
  resp.headers.set('Access-Control-Allow-Headers', 'Content-Type, X-Save-Secret');
  resp.headers.set('Vary', 'Origin');
  return resp;
}

function json(obj, status = 200) {
  return withCors(new Response(JSON.stringify(obj), {
    status,
    headers: { 'Content-Type': 'application/json' },
  }));
}

// Encode a repo path segment-by-segment (spaces in "Generated Illustrations" → %20).
function ghUrl(path) {
  const encoded = path.split('/').map(encodeURIComponent).join('/');
  return `https://api.github.com/repos/${REPO}/contents/${encoded}`;
}

async function ghFetch(env, path, method, payload) {
  return fetch(ghUrl(path), {
    method,
    headers: {
      'Authorization': `token ${env.GITHUB_TOKEN}`,
      'Accept': 'application/vnd.github+json',
      'User-Agent': 'wbt-collage-save-worker',
      ...(payload ? { 'Content-Type': 'application/json' } : {}),
    },
    body: payload ? JSON.stringify(payload) : undefined,
  });
}

export default {
  async fetch(request, env) {
    if (request.method === 'OPTIONS') {
      return withCors(new Response(null, { status: 204 }));
    }
    if (request.method !== 'POST') {
      return withCors(new Response('Method not allowed', { status: 405 }));
    }

    // --- Auth: constant-ish comparison against the shared secret ---
    const provided = request.headers.get('X-Save-Secret') || '';
    if (!env.SHARED_SECRET || provided !== env.SHARED_SECRET) {
      return withCors(new Response('Unauthorized', { status: 401 }));
    }

    let body;
    try {
      body = await request.json();
    } catch {
      return withCors(new Response('Bad JSON', { status: 400 }));
    }

    const { filename, contentBase64, entry } = body || {};
    if (!filename || !contentBase64) {
      return withCors(new Response('Missing filename or contentBase64', { status: 400 }));
    }

    // Sanitize filename — allow only safe chars, force a single .png
    const safe = String(filename).replace(/[^A-Za-z0-9._-]/g, '-');
    if (!/\.png$/i.test(safe)) {
      return withCors(new Response('filename must end in .png', { status: 400 }));
    }
    const imgPath = `${IMG_DIR}/${safe}`;

    // --- 1. Commit the PNG (fetch existing sha to allow overwrite) ---
    let imgSha;
    const imgGet = await ghFetch(env, imgPath, 'GET');
    if (imgGet.status === 200) imgSha = (await imgGet.json()).sha;

    const putImg = await ghFetch(env, imgPath, 'PUT', {
      message: `Add generated collage: ${(entry && entry.title) || safe}`,
      content: contentBase64,
      branch: BRANCH,
      ...(imgSha ? { sha: imgSha } : {}),
    });
    if (!putImg.ok) {
      return json({ ok: false, step: 'image', status: putImg.status, detail: await putImg.text() }, 502);
    }

    // --- 2. Read + update manifest.json ---
    let manifestList = [];
    let manifestSha;
    const mGet = await ghFetch(env, MANIFEST, 'GET');
    if (mGet.status === 200) {
      const mj = await mGet.json();
      manifestSha = mj.sha;
      try {
        manifestList = JSON.parse(atob(mj.content.replace(/\n/g, '')));
        if (!Array.isArray(manifestList)) manifestList = [];
      } catch {
        manifestList = [];
      }
    }

    // Keep the exact schema the gallery already reads.
    const manifestEntry = (entry && typeof entry === 'object')
      ? entry
      : { filename: safe, title: safe, concept: null, bgColorId: null, bgHex: null, savedAt: null };
    manifestEntry.filename = safe; // never trust client filename drift
    manifestList.unshift(manifestEntry);

    const manifestB64 = btoa(unescape(encodeURIComponent(JSON.stringify(manifestList, null, 2))));
    const putM = await ghFetch(env, MANIFEST, 'PUT', {
      message: `Update collage manifest: ${manifestEntry.title || safe}`,
      content: manifestB64,
      branch: BRANCH,
      ...(manifestSha ? { sha: manifestSha } : {}),
    });
    if (!putM.ok) {
      return json({ ok: false, step: 'manifest', status: putM.status, detail: await putM.text() }, 502);
    }

    return json({ ok: true, path: imgPath });
  },
};
