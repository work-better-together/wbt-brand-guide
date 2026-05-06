(function () {
  const ORDER = [
    { file: 'voice.html',           title: 'Voice',           num: '01' },
    { file: 'logo.html',            title: 'Logo',            num: '02' },
    { file: 'type.html',          title: 'Type',            num: '03' },
    { file: 'color.html',         title: 'Color',           num: '04' },
    { file: 'elements.html',      title: 'Elements',        num: '05' },
    { file: 'collages.html',     title: 'Collages',        num: '06' },
    { file: 'collage-maker.html',      title: 'Collage Maker',   num: '07' },
    { file: 'photos.html', title: 'Photos',          num: '08' },
    { file: 'deck-template/index.html',  title: 'Deck Template',   num: '09' },
    { file: 'swag.html',          title: 'Swag',            num: '10' },
    { file: 'clients.html',         title: 'Clients',         num: '11' },
    { file: 'motion.html',               title: 'Motion',          num: '12' },
    { file: 'newsletter.html',  title: 'Newsletter',      num: '13' },
    { file: 'social-maker.html',               title: 'Social Maker',    num: '14' },
    { file: 'tokens.html',               title: 'Tokens',          num: '15' },
    { file: 'components.html',           title: 'Components',      num: '15' },
    { file: 'iconography.html',          title: 'Iconography',     num: '16' },
    { file: 'data-viz.html',             title: 'Data Viz',        num: '17' },
    { file: 'microcopy.html',            title: 'Microcopy',       num: '18' }
  ];

  const here = decodeURIComponent((location.pathname.split('/').pop() || '')).replace(/\.html$/i, '').toLowerCase();
  const idx = ORDER.findIndex(p => p.file.replace(/\.html$/i, '').toLowerCase() === here);
  // Pages outside the numbered guide order (e.g. tools like Collage Builder)
  // still get the back-link + monogram nav, just without the pager.
  const isGuidePage = idx !== -1;
  const cur  = isGuidePage ? ORDER[idx] : { title: document.title.split('—')[0].trim(), num: null };
  const prev = isGuidePage && idx > 0 ? ORDER[idx - 1] : null;
  const next = isGuidePage && idx < ORDER.length - 1 ? ORDER[idx + 1] : null;

  const css = `
    .wbt-nav {
      position: sticky; top: 0; z-index: 100;
      background: #1F1E1E;
      border-bottom: 1px solid rgba(249, 248, 242, 0.10);
      padding: 12px 32px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 20px;
      font-family: 'Inconsolata', monospace;
      font-size: 11px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: rgba(249, 248, 242, 0.65);
    }
    .wbt-nav a {
      color: #F9F8F2;
      text-decoration: none;
      transition: opacity 0.15s ease;
    }
    .wbt-nav a:hover { opacity: 0.6; }
    .wbt-nav-home {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      transition: color 0.15s ease;
    }
    .wbt-nav a.wbt-nav-home { color: #F9F8F2; }
    .wbt-nav a.wbt-nav-home:hover { color: #CD9F36; opacity: 1; }
    .wbt-nav-left,
    .wbt-nav-right { display: flex; align-items: center; gap: 18px; flex-wrap: wrap; }
    .wbt-nav-right { gap: 14px; }
    .wbt-nav-divider {
      width: 1px;
      height: 14px;
      background: rgba(249, 248, 242, 0.20);
      flex-shrink: 0;
    }
    .wbt-nav-crumb {
      color: #CD9F36;
      letter-spacing: 0.1em;
    }
    .wbt-nav-pager {
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .wbt-nav-pager .pager-label {
      color: #F9F8F2;
      font-weight: 500;
      max-width: 180px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .wbt-nav-pager-disabled {
      opacity: 0.25;
      pointer-events: none;
    }
    .wbt-nav-monogram-mark {
      display: block;
      height: 32px;
      width: auto;
      margin: -2px 0;
      color: currentColor;
      transition: color 0.15s ease;
    }
    .wbt-nav-monogram-mark path { fill: currentColor; }

    @media (max-width: 820px) {
      .wbt-nav { padding: 10px 20px; }
      .wbt-nav-pager .pager-label { max-width: 110px; }
    }
    @media (max-width: 620px) {
      .wbt-nav-pager .pager-label { display: none; }
    }

    /* ── Footer page nav ── */
    .wbt-page-footer {
      max-width: 960px;
      margin: 0 auto;
      padding: 32px 40px 80px;
      display: grid;
      grid-template-columns: 1fr auto 1fr;
      gap: 20px;
      border-top: 1px solid #e4e2de;
    }
    .wbt-page-footer-col { display: flex; flex-direction: column; }
    .wbt-page-footer-prev { align-items: flex-start; }
    .wbt-page-footer-next { align-items: flex-end; }
    .wbt-page-footer-center { align-items: center; }
    .wbt-page-footer a {
      text-decoration: none;
      display: flex;
      flex-direction: column;
      gap: 6px;
      transition: opacity 0.15s;
    }
    .wbt-page-footer a:hover { opacity: 0.6; }
    .wbt-page-footer-label {
      font-family: 'Inconsolata', monospace;
      font-weight: 500;
      font-size: 10px;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #6b6b6b;
    }
    .wbt-page-footer-title {
      font-family: 'League Spartan', sans-serif;
      font-weight: 700;
      font-size: 20px;
      line-height: 1.05;
      letter-spacing: -0.01em;
      color: #1a1a1a;
    }
    @media (max-width: 520px) {
      .wbt-page-footer { padding: 24px 20px 60px; }
      .wbt-page-footer-title { font-size: 16px; }
      .wbt-page-footer-label { font-size: 9px; }
    }
    .wbt-page-footer-up {
      font-size: 16px;
      color: #6b6b6b;
      line-height: 1;
    }
    .wbt-nav-menu-btn {
      background: none; border: none; cursor: pointer; padding: 4px 2px;
      color: #F9F8F2; font-size: 18px; line-height: 1; display: flex; align-items: center;
    }
    .wbt-nav-menu-btn:hover { opacity: 0.7; }
    .wbt-nav-overlay {
      display: none; position: fixed; inset: 0; z-index: 150;
      background: rgba(0,0,0,0.5);
    }
    .wbt-nav-overlay.open { display: block; }
    .wbt-nav-drawer {
      position: fixed; top: 0; right: 0; bottom: 0; width: 280px;
      background: #1F1E1E; z-index: 200; padding: 24px 0;
      display: flex; flex-direction: column;
      border-left: 1px solid rgba(249,248,242,0.10);
      transform: translateX(100%); transition: transform 0.2s ease;
    }
    .wbt-nav-drawer.open { transform: translateX(0); }
    .wbt-nav-drawer-close {
      position: absolute; top: 16px; right: 20px;
      background: none; border: none; cursor: pointer;
      color: rgba(249,248,242,0.5); font-size: 20px; line-height: 1;
    }
    .wbt-nav-drawer-close:hover { color: #F9F8F2; }
    .wbt-nav-drawer-list { list-style: none; padding: 32px 0 0; overflow-y: auto; flex: 1; }
    .wbt-nav-drawer-group-label {
      padding: 16px 32px 6px; font-family: 'League Spartan', sans-serif;
      font-weight: 500; font-size: 10px; letter-spacing: 0.16em; text-transform: uppercase;
      color: rgba(249,248,242,0.35); border-bottom: 1px solid rgba(249,248,242,0.08);
      margin-bottom: 2px;
    }
    .wbt-nav-drawer-group-label:first-child { padding-top: 0; }
    .wbt-nav-drawer-list a {
      display: block; padding: 6px 32px;
      font-family: 'League Spartan', sans-serif; font-weight: 500; font-size: 13px;
      letter-spacing: 0.04em; text-transform: uppercase;
      color: rgba(249,248,242,0.75); text-decoration: none;
      transition: color 0.15s;
    }
    .wbt-nav-drawer-list a:hover { color: #F9F8F2; }
    .wbt-nav-drawer-list a.active { color: #CD9F36; }
    .wbt-nav-wip {
      display: inline-block;
      font-family: 'Inconsolata', monospace;
      font-size: 9px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #CD9F36;
      border: 1px solid rgba(205,159,54,0.5);
      padding: 1px 5px;
      border-radius: 3px;
      vertical-align: middle;
      margin-left: 6px;
      position: relative;
      top: -1px;
    }
  `;

  const style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // Derive the Brand Guide root from nav.js's own URL — works for both file:// and http://
  const _src = (document.currentScript || {}).src || '';
  const base = _src ? _src.replace(/\/nav\.js(\?.*)?$/, '/') : '';
  const idxHref = base + 'index.html';
  const monogramSVG = `<svg class="wbt-nav-monogram-mark" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 341.64 409.21" role="img" aria-label="WBT Monogram"><path d="M339.54,188.36c-2.66-44.12-15.24-90.73-27.08-114.95C294,32.09,247.69,5.65,187.5,1.47c-5.57-.39-12.55-.58-17.1-.58s-11.77.2-17.45.6C92.92,5.76,46.75,32.17,28.34,73.41,16.49,97.62,3.92,144.21,1.26,188.32c-.33,5.52-.51,14.41-.51,16.42s.18,10.92.51,16.45c2.66,44.1,15.24,90.68,27.08,114.89,18.43,41.26,64.65,67.69,124.74,71.92,5.64.4,14.78.6,17.27.6s11.61-.2,17.19-.59c60.18-4.19,106.46-30.63,124.91-71.93,11.84-24.21,24.41-70.78,27.08-114.88.33-5.54.51-12.58.51-16.44s-.18-10.89-.51-16.41ZM318.46,220.22c-2.33,41.46-13.34,85.24-23.7,108-16.15,38.83-56.67,63.68-109.35,67.62-4.89.37-12.88.55-15.05.55s-10.18-.19-15.12-.56c-52.61-3.98-93.07-28.82-109.2-67.61-10.36-22.76-21.37-66.55-23.7-108.01-.29-5.2-.45-13.57-.45-15.47s.16-10.25.45-15.44c2.33-41.47,13.34-85.26,23.7-108.03C62.16,42.51,102.57,17.67,155.12,13.67c4.97-.38,11.29-.57,15.27-.57s10.09.18,14.97.55c52.7,3.93,93.24,28.79,109.39,67.63,10.37,22.77,21.38,66.59,23.71,108.07.29,5.18.45,11.79.45,15.42s-.16,10.25-.45,15.46Z"/><path d="M245.75,148.05c11.46-3.57,18.92-12.87,18.92-24.84,0-15.53-12.39-25.73-31.44-25.73-4.8,0-12.92.51-21.45.51-5.71.04-23.36.04-27.26,0-7.06,0-13.19-.51-14.66-.51-1.6,0-2.53.76-2.53,2.16,0,1.27.8,2.3,2.53,2.55,7.6,1.15,10.66,3.44,9.06,9.56l-18.12,70.68c-.27,1.03-.53,1.15-.93,0l-22.12-72.22c-1.6-5.09.93-6.75,8.93-8.02,1.6-.25,2.13-1.28,2.13-2.42,0-1.4-.8-2.3-2.53-2.3-2.13,0-9.86.64-17.45.64-10.53,0-14.2-.64-16.87-.64-1.33,0-2.26.76-2.26,2.16s.67,2.16,2.4,2.55c5.06,1.15,5.81,2.67,7.27,7.26l11.33,35.03c.4,1.27.4,2.55-.13,4.21l-12.26,35.92c-.4,1.02-.66,1.14-1.06,0l-25.58-74.4c-1.74-5.22-2.26-6.87,5.73-8.02,1.6-.25,2.4-.9,2.4-2.42,0-1.4-.8-2.3-2.53-2.3-2.14,0-7.73.64-16.26.64-7.32,0-15.05-.64-17.05-.64-1.46,0-2.4.76-2.4,2.16s.8,2.16,2.53,2.55c5.33,1.27,7.2,2.67,8.93,7.26l33.71,93.24c1.07,3.06,3.2,4.33,6.53,4.33s4.93-1.27,5.99-4.33l15.32-43.31c.4-1.02.67-1.02,1.07.13l13.99,43.18c.94,3.06,3.07,4.33,6.4,4.33s5.06-1.27,5.86-4.33l24.92-91.84c1.13-4.13,3.47-5.92,7.11-7.19,1.85-.59,4.52-.25,5.2.19,1.35.88,2.31,2.11,2.31,3.94v88.91c0,4.08-4.67,5.35-8.13,5.99-2.13.39-2.53,1.27-2.53,2.29,0,.9.53,2.04,2.67,2.04,3.06,0,9.72-.25,18.38-.25l22.51.25c21.19,0,34.91-12.09,34.91-30.7,0-14.01-9.46-24.96-23.45-28.28ZM218.7,108.44c0-4.72,2.53-5.87,8.66-5.87,11.72,0,18.65,7.9,18.65,21.41s-8.39,22.67-21.45,22.67c-4.53,0-5.86-1.15-5.86-4.71v-33.5ZM230.42,201.93c-7.86,0-11.72-2.67-11.72-9.55v-35.67c0-4.2,1.33-4.97,6.92-4.97,15.06,0,24.92,9.94,24.92,25.1s-7.73,25.1-20.12,25.1Z"/><path d="M243.55,231.12c0-2.81-1.6-3.82-4.93-3.82-6.4,0-49.52,3.26-66.04,3.26h-.04c-16.52,0-59.59-3.26-65.99-3.26-3.33,0-4.93,1.02-4.93,3.82l.27,10.2-.13,9.54c0,1.4.8,2.16,2.13,2.16s1.54-.74,2.93-3.18c9.33-18,51.19-13.3,51.19-13.3,4.13,0,5.86,2.04,5.86,5.73v83.44c0,6.63-4.66,7.9-8.39,8.66-1.73.39-2.13,1.15-2.13,2.16,0,.9.53,2.04,2.26,2.04,1.46,0,9.33-.76,16.92-.76h0s.01,0,.02,0h.02s0,0,0,0c7.6,0,15.46.76,16.92.76,1.73,0,2.26-1.15,2.26-2.04,0-1.02-.4-1.78-2.13-2.16-3.73-.76-8.39-2.03-8.39-8.66v-83.44c0-3.69,1.73-5.73,5.86-5.73,0,0,41.92-4.71,51.25,13.3,1.39,2.44,1.6,3.18,2.93,3.18s2.13-.76,2.13-2.16l-.13-9.54.27-10.2Z"/></svg>`;

  const nav = document.createElement('nav');
  nav.className = 'wbt-nav';
  nav.setAttribute('aria-label', 'Brand guide navigation');
  const crumbHTML = cur.title;

  const pagerHTML = isGuidePage
    ? `${
        prev
          ? `<a class="wbt-nav-pager" href="${base}${encodeURI(prev.file)}" title="Previous: ${prev.title}">&larr; <span class="pager-label">${prev.title}</span></a>`
          : `<span class="wbt-nav-pager wbt-nav-pager-disabled">&larr; <span class="pager-label">Start</span></span>`
      }
      ${
        next
          ? `<a class="wbt-nav-pager" href="${base}${encodeURI(next.file)}" title="Next: ${next.title}"><span class="pager-label">${next.title}</span> &rarr;</a>`
          : `<span class="wbt-nav-pager wbt-nav-pager-disabled"><span class="pager-label">End</span> &rarr;</span>`
      }`
    : '';

  nav.innerHTML = `
    <div class="wbt-nav-left">
      <a class="wbt-nav-home" href="${idxHref}" title="Brand Guide Index" aria-label="Brand Guide Index">
        ${monogramSVG}
        <span>Brand Guide</span>
      </a>
      <span class="wbt-nav-divider" aria-hidden="true"></span>
      <span class="wbt-nav-crumb">${crumbHTML}</span>
    </div>
    <div class="wbt-nav-right">
    </div>
  `;

  document.body.insertBefore(nav, document.body.firstChild);

  // ── Hamburger drawer ──
  const overlay = document.createElement('div');
  overlay.className = 'wbt-nav-overlay';

  const drawer = document.createElement('div');
  drawer.className = 'wbt-nav-drawer';

  const closeBtn = document.createElement('button');
  closeBtn.className = 'wbt-nav-drawer-close';
  closeBtn.setAttribute('aria-label', 'Close menu');
  closeBtn.textContent = '×';

  const list = document.createElement('ul');
  list.className = 'wbt-nav-drawer-list';

  const homeLi = document.createElement('li');
  const homeA = document.createElement('a');
  homeA.href = idxHref;
  homeA.textContent = 'Home';
  homeLi.appendChild(homeA);
  list.appendChild(homeLi);

  const GROUPS = [
    { label: 'Guidelines', pages: [
      { file: 'voice.html',           title: 'Voice' },
      { file: 'logo.html',            title: 'Logo' },
      { file: 'type.html',          title: 'Type' },
      { file: 'color.html',         title: 'Color' },
      { file: 'elements.html',      title: 'Elements' },
      { file: 'collages.html',     title: 'Collages' },
      { file: 'photos.html', title: 'Photos' },
      { file: 'swag.html',          title: 'Swag' },
      { file: 'clients.html',         title: 'Clients' },
      { file: 'motion.html',          title: 'Motion' },
    ]},
    { label: 'Tools', pages: [
      { file: 'collage-maker.html',      title: 'Collage Maker' },
      { file: 'deck-template/index.html',  title: 'Deck Template' },
      { file: 'newsletter.html',  title: 'Newsletter' },
      { file: 'social-maker.html',               title: 'Social Maker', wip: true },
    ]},
    { label: 'Design System', pages: [
      { file: 'tokens.html',      title: 'Tokens' },
      { file: 'components.html',  title: 'Components' },
      { file: 'iconography.html', title: 'Iconography' },
      { file: 'data-viz.html',    title: 'Data Viz' },
      { file: 'microcopy.html',   title: 'Microcopy' },
    ]},
  ];

  GROUPS.forEach(group => {
    const groupLi = document.createElement('li');
    groupLi.className = 'wbt-nav-drawer-group-label';
    groupLi.textContent = group.label;
    list.appendChild(groupLi);

    group.pages.forEach(page => {
      const li = document.createElement('li');
      const a = document.createElement('a');
      a.href = base + encodeURI(page.file);
      a.innerHTML = page.title + (page.wip ? ' <span class="wbt-nav-wip">WIP</span>' : '');
      if (page.file.replace(/\.html$/i, '').toLowerCase() === here) {
        a.classList.add('active');
      }
      li.appendChild(a);
      list.appendChild(li);
    });
  });

  drawer.appendChild(closeBtn);
  drawer.appendChild(list);

  function openDrawer() {
    overlay.classList.add('open');
    drawer.classList.add('open');
  }
  function closeDrawer() {
    overlay.classList.remove('open');
    drawer.classList.remove('open');
  }

  closeBtn.addEventListener('click', closeDrawer);
  overlay.addEventListener('click', closeDrawer);
  document.addEventListener('keydown', e => { if (e.key === 'Escape') closeDrawer(); });

  document.body.appendChild(overlay);
  document.body.appendChild(drawer);

  const menuBtn = document.createElement('button');
  menuBtn.className = 'wbt-nav-menu-btn';
  menuBtn.setAttribute('aria-label', 'Open guide menu');
  menuBtn.textContent = '☰';
  menuBtn.addEventListener('click', openDrawer);

  nav.querySelector('.wbt-nav-right').appendChild(menuBtn);

  // ── Footer page nav ──
  if (isGuidePage && here !== 'collage-maker' && here !== 'newsletter' && here !== 'social-maker') {
    const footer = document.createElement('div');
    footer.className = 'wbt-page-footer';

    const prevCol = document.createElement('div');
    prevCol.className = 'wbt-page-footer-col wbt-page-footer-prev';
    if (prev) {
      prevCol.innerHTML = `<a href="${base}${encodeURI(prev.file)}">
        <span class="wbt-page-footer-label">← Previous</span>
        <span class="wbt-page-footer-title">${prev.title}</span>
      </a>`;
    }

    const centerCol = document.createElement('div');
    centerCol.className = 'wbt-page-footer-col wbt-page-footer-center';
    centerCol.innerHTML = `<a href="${idxHref}">
      <span class="wbt-page-footer-up">↑</span>
      <span class="wbt-page-footer-title">Index</span>
    </a>`;

    const nextCol = document.createElement('div');
    nextCol.className = 'wbt-page-footer-col wbt-page-footer-next';
    if (next) {
      nextCol.innerHTML = `<a href="${base}${encodeURI(next.file)}">
        <span class="wbt-page-footer-label">Next →</span>
        <span class="wbt-page-footer-title">${next.title}</span>
      </a>`;
    }

    footer.appendChild(prevCol);
    footer.appendChild(centerCol);
    footer.appendChild(nextCol);
    document.body.appendChild(footer);
  }
})();
