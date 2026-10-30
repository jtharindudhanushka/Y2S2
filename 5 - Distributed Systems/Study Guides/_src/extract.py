"""Builds qs.json (written part) and short.html for a lesson from its print notes.

Usage:  python extract.py NN
Reads ../../Print Notes/_src/lessonNN.html and _src/lessonNN/mcq.json (a list of {"q","o","a","e"}).
Written questions = the "Exam-style questions" section (each <p><b>Qn. ...</b><br> answer</p>).
Short note = the "Cheat sheet" section plus the "Common mistakes" table.
"""
import json, re, sys, os
n = sys.argv[1]
here = os.path.dirname(os.path.abspath(__file__))
d = os.path.join(here, "lesson" + n)
s = open(os.path.join(here, "..", "..", "Print Notes", "_src", "lesson%s.html" % n), encoding="utf-8").read()
ex = s[s.index("Exam-style questions"):]
ex = ex[:re.search(r"<h2", ex).start()]
written = []
for m in re.finditer(r"<p><b>Q\d+\.\s*(.*?)</b><br>\s*(.*?)</p>", ex, re.S):
    written.append({"q": m.group(1).strip(), "a": "<p>" + m.group(2).strip() + "</p>"})
mcq = json.load(open(os.path.join(d, "mcq.json"), encoding="utf-8"))
json.dump({"mcq": mcq, "written": written}, open(os.path.join(d, "qs.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
cs = s[re.search(r"<h2[^>]*>Cheat sheet", s).end():s.index("</body>")]
cm = re.search(r"<h2[^>]*>\d+\. Common mistakes</h2>(.*?)(?=<h2)", s, re.S)
short = ('<style>.two{display:grid;grid-template-columns:1fr 1fr;gap:14px}@media(max-width:700px){.two{grid-template-columns:1fr}}.two>div{min-width:0}td:first-child{white-space:normal}</style>\n'
         '<h2>Short note: revision sheet</h2>\n' + cs.strip() + '\n<h2>Common mistakes</h2>\n' + (cm.group(1).strip() if cm else ""))
open(os.path.join(d, "short.html"), "w", encoding="utf-8").write(short)
print("lesson", n, len(mcq), "mcq", len(written), "written")
