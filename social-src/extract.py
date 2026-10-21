"""Pull verbatim beats from WBT case studies (wbt-website repo) and resources (wbt-resources repo) into social-src/beats.json."""
import re, html, json, os
H = os.path.expanduser
def text(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s))).strip()
def label(li):   # "High pressure and fatigue: The cumulative…" -> "High pressure and fatigue"
    m = re.match(r'<(?:strong|b)>(.*?)</(?:strong|b)>', li.strip(), re.S)
    t = text(m.group(1)) if m else text(li)
    return t.rstrip(':').strip()

CASES = ['leading-together-under-pressure', 'developing-endurance-and-agency', 'building-conditions-for-results',
         'repairing-a-ruptured-relationship', 'choosing-the-culture-we-build-on-campaigns']
out = {'cases': [], 'resources': []}
for slug in CASES:
    s = open(H(f'~/Projects/wbt-website/case-studies/{slug}.html')).read()
    main = s[s.index('<main'):s.index('</main>')] if '<main' in s else s
    sect = {}
    for m in re.finditer(r'<h[23][^>]*>(.*?)</h[23]>(.*?)(?=<h[23]|$)', main, re.S):
        sect[text(m.group(1))] = m.group(2)
    def lis(k):
        body = next((v for kk, v in sect.items() if re.search(k, kk)), '')
        items = [label(x) for x in re.findall(r'<li[^>]*>(.*?)</li>', body, re.S)]
        if not items:   # approach written as steps (h4) or bold run-in heads instead of a list
            items = [text(x) for x in re.findall(r'<h4[^>]*>(.*?)</h4>', body, re.S)] or \
                    [text(x) for x in re.findall(r'<p>\s*<strong>(.*?)</strong>\s*</p>', body, re.S)]
        return [re.sub(r'\s+([,.:;])', r'\1', x) for x in items]
    t = text(main)
    service = re.search(r'Service (Leadership Coaching|Team Coaching|Facilitation \+ Training|2:2 Coaching)', t)
    quotes = [text(q) for q in re.findall(r'<blockquote[^>]*>(.*?)</blockquote>', main, re.S)]
    takeaway = next((q.replace('Key Takeaway', '').strip() for q in quotes if q.startswith('Key Takeaway')), '')
    client_quotes = [q.strip('“”" ') for q in quotes if not q.startswith('Key Takeaway')]
    out['cases'].append({
        'slug': slug, 'title': text(re.search(r'<h1[^>]*>(.*?)</h1>', s, re.S).group(1)),
        'service': service.group(1) if service else '',
        'lede': text(re.search(r'<p[^>]*>(.*?)</p>', main, re.S).group(1)),
        'challenge': lis('Challenge'), 'approach': lis('Approach'),
        'shifted': lis('Shift|Outcome|Impact'),
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
