/**
 * Export Spring-Retreat-2026.html → Spring-Retreat-2026.pptx
 * Requires: puppeteer, pptxgenjs (auto-installed via npx if needed)
 * Run: node export-pptx.mjs
 */

import { execSync } from 'child_process';
import { existsSync } from 'fs';
import { createRequire } from 'module';
import path from 'path';
import { fileURLToPath } from 'url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const pkgDir = path.join(__dirname, '_export_deps');

// Install deps into a local folder if needed
if (!existsSync(path.join(pkgDir, 'node_modules', 'puppeteer'))) {
  console.log('Installing puppeteer + pptxgenjs (first run only)…');
  execSync(`mkdir -p "${pkgDir}" && cd "${pkgDir}" && npm init -y && npm install puppeteer pptxgenjs --save`, { stdio: 'inherit' });
}

const require = createRequire(import.meta.url);
const puppeteer = await import(path.join(pkgDir, 'node_modules', 'puppeteer', 'lib', 'esm', 'puppeteer', 'puppeteer.js')).catch(() => {
  // fallback CJS path
  return { default: require(path.join(pkgDir, 'node_modules', 'puppeteer')) };
});
const pptxgenjs = await import(path.join(pkgDir, 'node_modules', 'pptxgenjs', 'libs', 'pptxgen.es.js')).catch(() => {
  return { default: require(path.join(pkgDir, 'node_modules', 'pptxgenjs')) };
});

const PptxGenJS = pptxgenjs.default?.default ?? pptxgenjs.default;
const puppeteerLib = puppeteer.default?.default ?? puppeteer.default;

const SLIDE_COUNT = 13;
const DECK_URL = 'http://localhost:7777/Plans/Spring-Retreat-2026.html';
const OUTPUT = path.join(__dirname, 'Spring-Retreat-2026.pptx');

console.log('Launching browser…');
const browser = await puppeteerLib.launch({
  headless: 'new',
  args: ['--no-sandbox', '--disable-setuid-sandbox'],
  defaultViewport: { width: 1920, height: 1080 }
});

const page = await browser.newPage();
await page.goto(DECK_URL, { waitUntil: 'networkidle0' });

// Wait for deck-stage to be ready
await page.waitForFunction(() => !!document.querySelector('deck-stage'), { timeout: 10000 });
await new Promise(r => setTimeout(r, 1500)); // fonts + watercolor settle

const screenshots = [];

for (let i = 0; i < SLIDE_COUNT; i++) {
  await page.evaluate((idx) => {
    const stage = document.querySelector('deck-stage');
    if (stage) stage.goTo(idx);
  }, i);

  // Let slide transition settle
  await new Promise(r => setTimeout(r, 600));

  const buf = await page.screenshot({ type: 'jpeg', quality: 95 });
  screenshots.push(buf);
  console.log(`  Captured slide ${i + 1}/${SLIDE_COUNT}`);
}

await browser.close();
console.log('Browser closed. Building PPTX…');

const pptx = new PptxGenJS();
pptx.layout = 'LAYOUT_WIDE'; // 13.33" × 7.5" (16:9)

for (const img of screenshots) {
  const slide = pptx.addSlide();
  const b64 = img.toString('base64');
  slide.addImage({
    data: `data:image/jpeg;base64,${b64}`,
    x: 0, y: 0, w: '100%', h: '100%'
  });
}

await pptx.writeFile({ fileName: OUTPUT });
console.log(`\n✅ Exported: ${OUTPUT}`);
