/* ─────────────────────────────────────────────────────────────────────────
   Shared "copy / download" action buttons for the brand guide.
   One component, used on every asset page (colors, clients, logos, elements,
   collages, photos) so the UI is identical everywhere.

   Usage in markup:
     <button class="ga-btn" onclick="gaCopyHex('#CD9F36', this)">Copy</button>
     <button class="ga-btn" onclick="gaCopyImg('path/to.png', this)">Copy</button>
     <button class="ga-btn" onclick="gaDownload('path/to.png', this)">Download</button>
   Wrap a pair in <div class="ga-actions">…</div>. Add class "ga-on-dark" to an
   ancestor for light buttons on dark surfaces.
   ───────────────────────────────────────────────────────────────────────── */
(function () {
  var css =
    '.ga-actions{display:inline-flex;gap:6px;align-items:center;}' +
    '.ga-btn{font-family:var(--font-mono,"Inconsolata",monospace);font-weight:500;font-size:11px;' +
      'letter-spacing:0.08em;text-transform:uppercase;color:#1F1E1E;background:transparent;' +
      'border:1px solid rgba(31,30,30,0.22);border-radius:4px;padding:6px 11px;cursor:pointer;' +
      'line-height:1;white-space:nowrap;transition:background .15s,border-color .15s,color .15s;}' +
    '.ga-btn:hover{border-color:#2531A5;color:#2531A5;}' +
    '.ga-btn:focus-visible{outline:2px solid #2531A5;outline-offset:2px;}' +
    '.ga-btn.ga-done{border-color:#1E4D5C;color:#1E4D5C;}' +
    '.ga-on-dark .ga-btn{color:#F9F8F2;border-color:rgba(249,248,242,0.38);}' +
    '.ga-on-dark .ga-btn:hover{border-color:#ACCDD9;color:#ACCDD9;}' +
    '.ga-on-dark .ga-btn.ga-done{border-color:#ACCDD9;color:#ACCDD9;}' +
    '.ga-titlebar{display:flex;align-items:center;justify-content:space-between;gap:14px;}' +
    '.ga-titlebar .ga-titlemeta{min-width:0;}' +
    '.ga-titlebar .ga-actions{flex:0 0 auto;}' +
    '.ga-ov-host{position:relative;}' +
    '.ga-ov{position:absolute;left:0;right:0;bottom:0;display:flex;gap:6px;justify-content:center;' +
      'padding:10px 8px;background:linear-gradient(0deg,rgba(249,248,242,0.97) 30%,rgba(249,248,242,0));' +
      'opacity:0;transition:opacity .15s;pointer-events:none;z-index:3;}' +
    '.ga-ov-host:hover .ga-ov,.ga-ov:focus-within{opacity:1;pointer-events:auto;}' +
    '.ga-ov .ga-btn{background:rgba(249,248,242,0.9);}';
  var s = document.createElement('style');
  s.textContent = css;
  document.head.appendChild(s);

  function feedback(btn, txt) {
    if (!btn) return;
    if (!btn._orig) btn._orig = btn.innerHTML;
    btn.textContent = txt;
    btn.classList.add('ga-done');
    clearTimeout(btn._t);
    btn._t = setTimeout(function () {
      btn.innerHTML = btn._orig;
      btn.classList.remove('ga-done');
    }, 1200);
  }

  function stop(e) { if (e) { e.stopPropagation(); e.preventDefault(); } }

  window.gaCopyHex = function (hex, btn, e) {
    stop(e);
    navigator.clipboard.writeText(hex).then(function () { feedback(btn, 'Copied'); })
      .catch(function () { feedback(btn, 'Copy failed'); });
  };

  window.gaCopyText = function (t, btn, e) {
    stop(e);
    navigator.clipboard.writeText(t).then(function () { feedback(btn, 'Copied'); });
  };

  window.gaDownload = function (src, btn, e) {
    stop(e);
    var a = document.createElement('a');
    a.href = src;
    a.download = decodeURIComponent(src.split('/').pop());
    document.body.appendChild(a);
    a.click();
    a.remove();
    feedback(btn, 'Saved');
  };

  /* Wire a set of asset tiles with a consistent Copy/Download action row.
     opts = { cards, img, bar, wrap:bool, actions:[{label, fn}] }
     - cards: selector for each item container
     - img:   selector (within card) for the <img> whose src is the asset
     - bar:   selector (within card) to receive the actions (default: the card)
     - wrap:  if true, existing bar children are grouped left and actions right
     - actions: buttons; each fn is called (src, btn, event) */
  window.gaWireTiles = function (opts) {
    document.querySelectorAll(opts.cards).forEach(function (card) {
      var img = card.querySelector(opts.img);
      if (!img) return;
      var src = img.getAttribute('src');
      var bar = opts.bar ? card.querySelector(opts.bar) : card;
      if (!bar || bar.querySelector('.ga-actions')) return;
      var acts = document.createElement('div');
      acts.className = 'ga-actions';
      (opts.actions || []).forEach(function (a) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'ga-btn';
        b.textContent = a.label;
        b.addEventListener('click', function (ev) { a.fn(img.getAttribute('src'), b, ev); });
        acts.appendChild(b);
      });
      if (opts.wrap) {
        var left = document.createElement('div');
        left.className = 'ga-titlemeta';
        while (bar.firstChild) left.appendChild(bar.firstChild);
        bar.appendChild(left);
        bar.appendChild(acts);
        bar.classList.add('ga-titlebar');
      } else {
        bar.appendChild(acts);
      }
    });
  };

  /* Hover overlay of action buttons for dense image tiles (spots, scribbles,
     illustrations, photos, collages). opts = { cards, img, actions:[{label,fn}] } */
  window.gaWireOverlay = function (opts) {
    document.querySelectorAll(opts.cards).forEach(function (card) {
      var img = card.querySelector(opts.img);
      if (!img || card.querySelector('.ga-ov')) return;
      var src = img.getAttribute('src');
      card.classList.add('ga-ov-host');
      if (getComputedStyle(card).position === 'static') card.style.position = 'relative';
      var ov = document.createElement('div');
      ov.className = 'ga-ov';
      (opts.actions || []).forEach(function (a) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'ga-btn';
        b.textContent = a.label;
        b.addEventListener('click', function (ev) { a.fn(img.getAttribute('src'), b, ev); });
        ov.appendChild(b);
      });
      card.appendChild(ov);
    });
  };

  window.gaCopyImg = async function (src, btn, e) {
    stop(e);
    try {
      var resp = await fetch(src);
      var blob = await resp.blob();
      if (blob.type !== 'image/png') {
        var bmp = await createImageBitmap(blob);
        var c = document.createElement('canvas');
        c.width = bmp.width; c.height = bmp.height;
        c.getContext('2d').drawImage(bmp, 0, 0);
        blob = await new Promise(function (res) { c.toBlob(res, 'image/png'); });
      }
      await navigator.clipboard.write([new ClipboardItem({ 'image/png': blob })]);
      feedback(btn, 'Copied');
    } catch (err) {
      // clipboard-image unsupported (or blocked) → fall back to a download
      window.gaDownload(src, btn);
    }
  };
})();
