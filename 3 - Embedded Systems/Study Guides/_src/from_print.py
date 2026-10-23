"""Converts a Print Notes lesson (black-and-white A4 HTML) into a study-guide notes.html tab.

Usage:  python from_print.py <print_lesson.html> <out_notes.html> <sources line>
The print notes are the single source of the long-form lesson text; this keeps the
study guide in sync and makes the drawings follow the light/dark theme.
"""
import re, sys

src, out, sources = sys.argv[1], sys.argv[2], sys.argv[3]
old = open(sys.argv[4], encoding="utf-8").read() if len(sys.argv) > 4 else ""
s = open(src, encoding="utf-8").read()
body = s[s.index("<body>") + 6:s.index("</body>")]

# drop the page title block (the study guide has its own header) and the end cheat sheet (the Short note tab covers it)
body = re.sub(r"<h1>.*?</h1>\s*<p class=\"small\">.*?</p>", "", body, count=1, flags=re.S)
cut = re.search(r"<h2[^>]*>Cheat sheet", body)
if cut:
    body = body[:cut.start()]
body = re.sub(r"<!--.*?-->", "", body, flags=re.S)

# theme-aware drawings
soft = 'style="fill:var(--soft)"'
for c in ("#ddd", "#bbb", "#e4e4e4", "#f3f3f3", "#f0f0f0", "#f6f6f6", "#ccc", "#E2DAC7"):
    body = body.replace('fill="%s"' % c, soft)
body = body.replace('fill="#fff"', 'style="fill:var(--bg)"')
body = body.replace('fill="#000"', 'fill="currentColor"').replace('stroke="#000"', 'stroke="currentColor"')
body = body.replace('fill="#555"', 'fill="currentColor" fill-opacity="0.6"').replace('stroke="#888"', 'stroke="currentColor" stroke-opacity="0.5"')
body = re.sub(r'(<[a-z]+[^>]*?) style="fill:var\(--[a-z]+\)"([^>]*?) style="([^"]*)"', r'\1\2 style="\3"', body)

css = """<style>
.fig{margin:14px 0;text-align:center}.fig svg{width:100%;height:auto;max-width:680px;color:var(--fg)}.fig svg text{fill:currentColor}
.cap{font-size:13px;color:var(--muted);text-align:center;margin-top:2px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(max-width:640px){.two{grid-template-columns:1fr}}
.two>div{min-width:0}
.key{background:var(--soft);border:1px solid var(--line);border-left:3px solid var(--accent);padding:10px 14px;margin:14px 0;border-radius:0 6px 6px 0}
b.t{display:block;text-transform:uppercase;font-size:12px;letter-spacing:.4px;margin-bottom:4px;color:var(--accent)}
.small{font-size:14px}.note{font-size:14px}
.bitgrp{border:1px solid var(--line);border-radius:6px;padding:8px 12px;margin:10px 0}.bitgrp .title{font-weight:600;margin-bottom:4px}
.bits{display:flex;align-items:center;flex-wrap:wrap;margin:3px 0;font-family:ui-monospace,Consolas,monospace}
.bits .lbl{width:190px;font-family:system-ui,sans-serif;font-size:14px}
.bits span.b{width:26px;height:24px;border:1px solid var(--fg);text-align:center;line-height:24px;margin-right:-1px}
.bits span.h{background:var(--soft);font-weight:700;color:var(--accent)}
.bits .note{margin-left:10px;font-size:13px;color:var(--muted);font-family:system-ui,sans-serif}
.pos .bits span.b{border:none;height:18px;line-height:18px;font-size:12px;color:var(--muted)}
table.code td:first-child{font-family:ui-monospace,Consolas,monospace;font-size:13px;white-space:pre;background:var(--soft)}
.led{display:inline-block;width:14px;height:14px;border:1px solid var(--fg);border-radius:50%;margin:0 2px;vertical-align:middle}.led.on{background:var(--fg)}
</style>
"""
head = '<p class="sm" style="color:var(--muted)">%s</p>\n' % sources
if old:
    # Part 1 = the original notes from this year's slides and peer notes, kept unchanged.
    # Part 2 = added beginner explanations, diagrams and the lecture-recording notes.
    old = ('<h2 style="border-bottom:2px solid var(--accent)">Part 1: Lesson notes (this year\'s slides and peer notes)</h2>\n'
           + old)
    head = ('\n<h2 style="border-bottom:2px solid var(--accent);margin-top:40px">Part 2: Beginner explanations, diagrams and lecture-recording notes (added)</h2>\n'
            '<div class="warn" style="color:var(--bad);font-weight:600"><b>About Part 2:</b> the numbered sections re-explain this year\'s slides and exercises from zero for beginners. '
            '<b>Section L</b> near the end is derived from the <b>2020 lecture recordings</b>, so it may not match this year exactly: study it with caution and follow Part 1 / this year\'s slides where they disagree.</div>\n' + head)
if old:
    split = """<style>
.splitbar{position:sticky;top:0;z-index:5;background:var(--bg);padding:6px 0;margin:4px 0 10px;border-bottom:1px solid var(--line);display:flex;gap:6px;flex-wrap:wrap}
.splitbar button{font:inherit;font-size:13px;background:var(--soft);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:5px 10px;cursor:pointer}
.splitbar button[aria-pressed=true]{background:var(--accent);color:var(--bg);border-color:var(--accent)}
.parts.m-p1 .p2,.parts.m-p2 .p1{display:none}
.parts.m-split{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.parts.m-split>div{max-height:82vh;overflow:auto;border:1px solid var(--line);border-radius:6px;padding:0 12px}
body.splitwide .wrap{max-width:1500px}
@media(max-width:900px){.splitbar .sb-split{display:none}.parts.m-split{display:block}.parts.m-split>div{max-height:none;overflow:visible;border:0;padding:0}}
</style>
<div class="splitbar" role="group" aria-label="Choose what to show">
<button type="button" data-m="both">Part 1 + Part 2</button>
<button type="button" data-m="p1">Part 1 only (this year)</button>
<button type="button" data-m="p2">Part 2 only (added)</button>
<button type="button" data-m="split" class="sb-split">Side by side</button>
</div>
"""
    js = """<script>
(function(){var p=document.getElementById('parts'),bs=document.querySelectorAll('.splitbar button');
function set(m){p.className='parts m-'+m;document.body.classList.toggle('splitwide',m==='split');
for(var i=0;i<bs.length;i++)bs[i].setAttribute('aria-pressed',bs[i].getAttribute('data-m')===m?'true':'false');
try{localStorage.setItem('es-parts',m)}catch(e){}}
for(var i=0;i<bs.length;i++)bs[i].addEventListener('click',function(){set(this.getAttribute('data-m'))});
var v='both';try{v=localStorage.getItem('es-parts')||'both'}catch(e){}set(v);})();
</script>
"""
    page = (css + split + '<div class="parts m-both" id="parts"><div class="p1">' + old + '</div><div class="p2">'
            + head + body.strip() + '</div></div>\n' + js)
else:
    page = css + head + body.strip() + "\n"
open(out, "w", encoding="utf-8").write(page)
print("wrote", out, len(body), "chars")
