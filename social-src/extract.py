"""Pull verbatim beats from WBT case studies (wbt-website repo) and resources (wbt-resources repo) into social-src/beats.json."""
import re, html, json, os
H = os.path.expanduser
def text(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
def label(li):   # "High pressure and fatigue: The cumulative…" -> "High pressure and fatigue"
    m = re.match(r'<(?:strong|b)>(.*?)</(?:strong|b)>', li.strip(), re.S)
    t = text(m.group(1)) if m else text(li)
    return t.rstrip(':').strip()

CASES = sorted(os.path.basename(f)[:-5] for f in __import__('glob').glob(H('~/Projects/wbt-website/case-studies/*.html')) if not os.path.basename(f).startswith('_'))
out = {'cases': [], 'resources': []}
CHALLENGE = r'Challenge|Navigating Complexity'
APPROACH = r'Approach|What We Did|Initial Program|Transformation'
SHIFT = r'Shift|Outcome|Impact|Results|Road Ahead|Demonstrates|Conclusion'
for slug in CASES:
    s = open(H(f'~/Projects/wbt-website/case-studies/{slug}.html')).read()
    main = s[s.index('<main'):s.index('</main>')] if '<main' in s else s
    sect = {}
    for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>(.*?)(?=<h[23]|$)', main, re.S):
        sect[text(m.group(1))] = m.group(2)
    def lis(k):
        body = ''.join(v for kk, v in sect.items() if re.search(k, kk))   # every matching section, in page order
        body = re.sub(r'<blockquote.*?</blockquote>', '', body, flags=re.S)
        steps = [text(x) for x in re.findall(r'<p>\s*<strong>(.*?)<br>\s*</strong>', body, re.S)]   # "Goal #1: …<br>" step heads beat a sub-list
        items = steps if len(steps) >= 2 else [label(x) for x in re.findall(r'<li[^>]*>(.*?)</li>', body, re.S)]
        if not items:   # approach written as steps (h4), accordions, or bold run-in heads instead of a list
            items = [text(x) for x in re.findall(r'<h4[^>]*>(.*?)</h4>', body, re.S)] or \
                    [text(x) for x in re.findall(r'<summary[^>]*>(.*?)</summary>', body, re.S)] or \
                    [text(x) for x in re.findall(r'<p>\s*<strong>(.*?)(?:<br>\s*)?</strong>', body, re.S)]
        return [re.sub(r'\s+([,.:;])', r'\1', x).rstrip(':').strip() for x in items]
    def paras(k):
        body = ''.join(v for kk, v in sect.items() if re.search(k, kk))
        body = re.sub(r'<blockquote.*?</blockquote>|<details.*?</details>', '', body, flags=re.S)
        return [re.sub(r'\s+([,.:;])', r'\1', text(x)) for x in re.findall(r'<p(?:\s[^>]*)?>(.*?)</p>', body, re.S) if len(text(x).split()) >= 8]
    t = text(main)
    service = re.search(r'Service (Leadership Coaching|Team Coaching|Facilitation \+ Training|2:2 Coaching)', t)
    quotes, takeaway = [], ''
    for q in re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', main, re.S):
        if text(q).startswith('Key Takeaway'):
            takeaway = text(q).replace('Key Takeaway', '').strip(); continue
        cite = re.search(r'<cite[^>]*>(.*?)</cite>', q, re.S)
        name = re.search(r'class="cs-name"[^>]*>(.*?)</', q, re.S); role = re.search(r'class="cs-role"[^>]*>(.*?)</', q, re.S)
        body = re.sub(r'<cite.*?</cite>|<[^>]*class="cs-(?:name|role|who|person)[^"]*"[^>]*>.*?</[^>]+>|<img[^>]*>', '', q, flags=re.S)
        quotes.append({'text': text(body).strip('“”" '), 'name': text(name.group(1)) if name else (text(cite.group(1)) if cite else ''),
                       'role': text(role.group(1)) if role else ''})
    client_quotes = quotes
    out['cases'].append({
        'slug': slug, 'title': text(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)),
        'service': service.group(1) if service else '',
        'lede': text(re.search(r'<p[^>]*>(.*?)</p>', main, re.S).group(1)),
        'client': text(m.group(1)) if (m := re.search(r'class="cs-client-logo[^"]*"[^>]*alt="([^"]*)"', main)) else '',
        'challenge': lis(CHALLENGE), 'challenge_p': paras(CHALLENGE),
        'approach': lis(APPROACH), 'approach_p': paras(APPROACH),
        'shifted': lis(SHIFT), 'shifted_p': paras(SHIFT),
        'shift_label': next((k for k in sect if re.search(SHIFT, k)), ''),
        'takeaway': takeaway, 'quotes': client_quotes,
        'sections': list(sect.keys())})

RES = [('leaders/values-and-energy', 'For leaders'), ('teams/after-action-review', 'For teams'), ('teams/role-clarity', 'For teams'),
       ('retreats/retreat-planning-checklist', 'Retreat preparation'), ('career-transitions/career-timeline', 'Career transitions'),
       ('campaign-leaders', 'Campaign leaders')]
for path, cat in RES:
    p = H(f'~/Projects/wbt-resources/site/{path}/index.html')
    s = open(p).read()
    h1 = re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S)
    paras = [text(x) for x in re.findall(r'<p[^>]*>(.*?)</p>', s, re.S)]
    heads = [text(x) for x in re.findall(r'<h[23][^>]*>(.*?)</h[23]>', s, re.S)]
    out['resources'].append({'path': path, 'category': cat, 'title': text(h1.group(1)) if h1 else '',
                             'paras': [x for x in paras if len(x) > 30][:4], 'heads': heads[:8]})
json.dump(out, open(os.path.join(os.path.dirname(__file__), 'beats.json'), 'w'), indent=1, ensure_ascii=False)
print('cases', len(out['cases']), 'resources', len(out['resources']))
