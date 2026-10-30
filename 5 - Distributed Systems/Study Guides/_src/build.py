"""Builds the self-contained lesson HTML files in the parent folder.

Usage:  python build.py            (builds every lessonNN folder found here)
        python build.py 02         (builds only lesson02)

Each _src/lessonNN/ folder holds:
  meta.json       {"n":2,"title":"...","file":"Lesson 02 - ....html","lead":"...","tabs":[["notes","Lesson"],["qs","Practice questions"],["short","Short note"]]}
  <tabid>.html    content of every tab except "qs"  (e.g. notes.html, short.html)
  qs.json         {"mcq":[{"q":"","o":["",...],"a":0,"e":""}], "written":[{"q":"<html>","a":"<html>"}]}
Shared look and behaviour lives in template.html (copied from Lesson 01).
All lessons are built from here.
"""
import json, os, sys, html

here = os.path.dirname(os.path.abspath(__file__))
out = os.path.dirname(here)
tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()


def build(folder):
    d = os.path.join(here, folder)
    meta = json.load(open(os.path.join(d, "meta.json"), encoding="utf-8"))
    qs = json.load(open(os.path.join(d, "qs.json"), encoding="utf-8"))
    tabs = "\n    ".join(
        '<button role="tab" aria-selected="%s" data-p="%s">%s</button>' % ("true" if i == 0 else "false", t, html.escape(l))
        for i, (t, l) in enumerate(meta["tabs"]))
    panels = []
    for i, (t, l) in enumerate(meta["tabs"]):
        cls = "panel on" if i == 0 else "panel"
        if t == "qs":
            w = "\n".join("<details>\n<summary>W%d. %s</summary>\n%s\n</details>" % (k + 1, x["q"], x["a"]) for k, x in enumerate(qs.get("written", [])))
            body = ('<div class="score">Score: <span id="sc">0</span> / <span id="tot">0</span> &middot; <button class="link" id="reset">Reset</button></div>\n'
                    '<div id="mcq"></div>\n<h2>Written questions</h2>\n' + w)
        else:
            body = open(os.path.join(d, t + ".html"), encoding="utf-8").read()
        panels.append('<section class="%s" id="%s">\n%s\n</section>' % (cls, t, body))
    s = tpl
    s = s.replace("{{TITLE}}", html.escape("DS Lesson %d - %s" % (meta["n"], meta["title"])))
    s = s.replace("{{PART}}", "Lesson %02d" % meta["n"])
    s = s.replace("{{H1}}", html.escape(meta["title"]))
    s = s.replace("{{LEAD}}", meta["lead"])
    s = s.replace("{{TABS}}", tabs)
    s = s.replace("{{PANELS}}", "\n\n".join(panels))
    s = s.replace("{{QJS}}", json.dumps([{"q": x["q"], "o": x["o"], "a": x["a"], "e": x["e"]} for x in qs["mcq"]], ensure_ascii=False))
    open(os.path.join(out, meta["file"]), "w", encoding="utf-8").write(s)
    print("built", meta["file"], len(qs["mcq"]), "mcq")


want = sys.argv[1:]
for f in sorted(os.listdir(here)):
    if f.startswith("lesson") and os.path.isdir(os.path.join(here, f)) and (not want or f[6:] in want):
        build(f)
