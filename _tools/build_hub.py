"""Builds the root hub (index.html) and the base 'Study Guides/index.html' page of every subject.

Run from anywhere:   python _tools/build_hub.py
Re-run whenever files are added/removed, or when a subject's lessons become 'ready' (edit NOTES_READY below).

- Root index.html: subject cards, exam countdown, and a file browser/downloader built from a manifest
  of every file in the repo (a static site cannot list folders at run time, so the list is embedded).
- Subject pages: <subject>/Study Guides/index.html (generated, marked <!--generated-->). DSA's page is
  hand written and is never overwritten.
- Files above BIG_MB (and all .mp4) are flagged 'big': the Pages workflow does not publish them, so on
  github.io their links point at the GitHub raw URL instead (relative links are used when opened locally).
"""
import os, re, json, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = "jtharindudhanushka/Y2S2"
BIG_MB = 40
SKIP_DIRS = {".git", ".github", "_tools", "_src", "node_modules"}
SKIP_FILES = {"index.html"}  # only the root one is skipped (checked by path below)

SUBJECTS = [
    # folder, code, name, exams [(label, iso)], notes
    ("1 - DSA", "INTE 22343", "Data Structures & Algorithms", [("Paper", "2026-10-19T09:00")], 8),
    ("2 - Mobile Applications", "INTE 22283", "Mobile Application Development", [("Paper", "2026-10-22T09:00")], 0),
    ("3 - Embedded Systems", "INTE 22263", "Embedded Systems", [("Practical", "2026-10-26T09:00"), ("Paper", "2026-10-27T09:00")], 0),
    ("4 - AI", "INTE 22303", "Artificial Intelligence", [("Paper", "2026-10-30T09:00")], 7),
    ("5 - Distributed Systems", "INTE 22253", "Distributed Systems & Cloud Computing", [("Paper", "2026-11-02T09:00")], 0),
    ("6 - Design Patterns", "INTE 22313", "Design Patterns & Frameworks", [("Paper (open book)", "2026-11-04T09:00")], 0),
    ("7 - Software Architecture", "INTE 22293", "Software Architecture & Process Model", [("Paper", "2026-11-06T13:00")], 0),
]


def manifest():
    out = []
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = sorted(d for d in dn if d not in SKIP_DIRS)
        for f in sorted(fn):
            full = os.path.join(dp, f)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            if rel in ("index.html", ".gitignore") or rel.startswith("."):
                continue
            size = os.path.getsize(full)
            big = f.lower().endswith(".mp4") or size > BIG_MB * 1024 * 1024
            out.append({"p": rel, "s": size, "b": 1 if big else 0})
    return out


# ------------------------------------------------------------------ shared look
CSS = """
  :root{--bg:#fff;--fg:#1f2328;--muted:#656d76;--line:#d8dee4;--soft:#f6f8fa;--accent:#0b5cad;--ok:#1a7f37;color-scheme:light}
  :root[data-theme=dark]{--bg:#14171a;--fg:#e6e8ea;--muted:#9aa3ad;--line:#2d333b;--soft:#1c2128;--accent:#6cb2ff;--ok:#56d364;color-scheme:dark}
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);color:var(--fg);font-family:Inter,"Segoe UI",system-ui,-apple-system,Roboto,Arial,sans-serif;line-height:1.6;font-size:16px}
  .wrap{max-width:980px;margin:0 auto;padding:24px 16px 64px}
  .top{display:flex;justify-content:space-between;align-items:center;gap:12px}
  .crumb{color:var(--muted);font-size:13px;margin:0}
  a{color:var(--accent);text-decoration:none}a:hover{text-decoration:underline}
  h1{font-size:28px;margin:6px 0}
  h2{font-size:19px;margin:34px 0 8px;border-top:1px solid var(--line);padding-top:10px}
  .lead{color:var(--muted);margin:4px 0 18px}
  button,.btn{font:inherit;font-size:13px;background:var(--soft);color:var(--fg);border:1px solid var(--line);border-radius:6px;padding:5px 10px;cursor:pointer;display:inline-block}
  .btn:hover,button:hover{border-color:var(--accent);text-decoration:none}
  .btn.pri{background:var(--accent);color:var(--bg);border-color:var(--accent)}
  input[type=search]{font:inherit;width:100%;padding:9px 12px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--fg)}
  table{border-collapse:collapse;width:100%;font-size:15px}
  th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}
  th{background:var(--soft);font-weight:600}
  td.n{width:48px;color:var(--muted)}
  .tag{font-size:12px;border:1px solid var(--line);border-radius:10px;padding:1px 8px;color:var(--muted);white-space:nowrap}
  .tag.ready{color:var(--accent);border-color:var(--accent)}
  .sm{font-size:14px;color:var(--muted)}
"""
THEME_HEAD = """<script>
(function(){var t=null;try{t=localStorage.getItem('theme')}catch(e){}
if(!t)t=matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';
document.documentElement.dataset.theme=t;})();
</script>"""
THEME_JS = """
const tb=document.getElementById('theme');
function paint(){tb.textContent=document.documentElement.dataset.theme==='dark'?'Light mode':'Dark mode'}
tb.onclick=()=>{const t=document.documentElement.dataset.theme==='dark'?'light':'dark';document.documentElement.dataset.theme=t;try{localStorage.setItem('theme',t)}catch(e){}paint()};
paint();
"""

# ------------------------------------------------------------------ subject base pages
SUBJECT_PAGE = """<!DOCTYPE html>
<!--generated-->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{TITLE}} study guides</title>
""" + THEME_HEAD + """
<style>""" + CSS + """</style>
</head>
<body>
<div class="wrap">
  <div class="top">
    <p class="crumb"><a href="../../index.html">&larr; All subjects</a> &middot; {{CODE}}</p>
    <button id="theme" type="button"></button>
  </div>
  <h1>{{NAME}}</h1>
  <p class="lead">Study notes for this subject are not written yet. The table lists the lectures with their slides so you can open or download them now. Exam: {{EXAM}}.</p>
  <p><a class="btn pri" href="../../index.html#{{HASH}}">Browse and download all files</a></p>
  <input type="search" id="q" placeholder="Filter lessons..." style="margin-top:14px">
  <table style="margin-top:10px">
    <thead><tr><th>#</th><th>Lesson</th><th>Slides and files</th><th>Notes</th></tr></thead>
    <tbody id="rows"></tbody>
  </table>
</div>
<script>
/* To publish a lesson note: put its html file next to this page, set file and ready:true. */
const SUBJECT={{SUBJ}};
const LESSONS={{LESSONS}};
const REPO="{{REPO}}", BASE="../../";
const onPages=/github\\.io$/.test(location.hostname);
const rows=document.getElementById('rows'),q=document.getElementById('q');
function href(f){const enc=f.p.split('/').map(encodeURIComponent).join('/');return (onPages&&f.b)?'https://github.com/'+REPO+'/raw/main/'+enc:BASE+enc}
function draw(){
  const s=q.value.trim().toLowerCase();rows.innerHTML='';
  LESSONS.filter(l=>!s||l.title.toLowerCase().includes(s)).forEach(l=>{
    const tr=document.createElement('tr');
    const n=document.createElement('td');n.className='n';n.textContent=l.n;
    const t=document.createElement('td');
    if(l.ready){const a=document.createElement('a');a.href=encodeURI(l.file);a.textContent=l.title;a.style.fontWeight='600';t.appendChild(a)}else t.textContent=l.title;
    const f=document.createElement('td');
    l.files.forEach((x,i)=>{if(i)f.append(' ');const a=document.createElement('a');a.className='btn';a.href=href(x);a.target='_blank';a.rel='noopener';a.textContent=x.p.split('.').pop().toUpperCase();a.title=x.p.split('/').pop();f.appendChild(a)});
    const st=document.createElement('td');const g=document.createElement('span');g.className='tag'+(l.ready?' ready':'');g.textContent=l.ready?'Ready':'Coming soon';st.appendChild(g);
    tr.append(n,t,f,st);rows.appendChild(tr);
  });
}
q.oninput=draw;draw();
""" + THEME_JS + """
</script>
</body>
</html>
"""


def lessons_for(folder, files):
    """Group Lecture Materials by leading number -> lessons with their slide files."""
    groups = {}
    pat = re.compile(r"^(?:Lecture |Cloud_Computing_Lecture\s*)?0*(\d+)(?:\.\d+)?\s*(?:-\s*)?(.*)$")
    for f in files:
        rel = f["p"]
        if not rel.startswith(folder + "/Lecture Materials/"):
            continue
        name = os.path.splitext(rel.split("/")[-1])[0]
        ext = rel.rsplit(".", 1)[-1].lower()
        if ext not in ("pdf", "pptx", "ppt", "docx", "md", "xlsx", "zip", "ipynb", "html"):
            continue
        m = pat.match(name)
        if not m or name.startswith("INTE"):
            key, title = 99, name
        else:
            key = int(m.group(1))
            title = m.group(2).strip() or "Lecture %d" % key
            if name.lower().startswith(("lecture", "cloud")):
                title = "Lecture %d" % key
        g = groups.setdefault(key, {"title": title, "files": []})
        if len(title) < len(g["title"]) and title:
            g["title"] = title
        g["files"].append({"p": rel, "b": f["b"]})
    out = []
    for key in sorted(groups):
        g = groups[key]
        title = re.sub(r"\s*\((?:New|Old|Last Year|This Year|Previous|Generated|Original|AI Generated|Detailed|Support Notes)\)\s*$", "", g["title"]).strip()
        out.append({"n": "%02d" % key if key != 99 else "&ndash;", "title": title, "files": g["files"], "file": "", "ready": False})
    return out


def exam_text(exams):
    nice = []
    for lab, iso in exams:
        d, t = iso.split("T")
        y, m, dd = d.split("-")
        nice.append("%s %s.%s.%s %s" % (lab, dd, m, y, t))
    return "; ".join(nice)


def build_subject_pages(files):
    made = []
    for folder, code, name, exams, notes in SUBJECTS:
        sg = os.path.join(ROOT, folder, "Study Guides")
        idx = os.path.join(sg, "index.html")
        if notes:  # hand written (DSA)
            continue
        if os.path.exists(idx) and "<!--generated-->" not in open(idx, encoding="utf-8").read():
            continue
        os.makedirs(sg, exist_ok=True)
        ls = lessons_for(folder, files)
        s = SUBJECT_PAGE
        s = s.replace("{{TITLE}}", html.escape(name)).replace("{{CODE}}", code).replace("{{NAME}}", html.escape(name))
        s = s.replace("{{EXAM}}", exam_text(exams)).replace("{{HASH}}", folder.replace(" ", "%20") + "/Lecture%20Materials")
        s = s.replace("{{SUBJ}}", json.dumps({"code": code, "name": name, "folder": folder}))
        s = s.replace("{{LESSONS}}", json.dumps(ls, ensure_ascii=False)).replace("{{REPO}}", REPO)
        open(idx, "w", encoding="utf-8").write(s)
        made.append(folder)
    return made


# ------------------------------------------------------------------ root hub
HUB = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Y2S2 Study Hub</title>
""" + THEME_HEAD + """
<style>""" + CSS + """
  .grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:12px;margin-top:8px}
  .card{border:1px solid var(--line);border-radius:8px;padding:14px 16px;background:var(--bg)}
  .card h3{margin:0 0 2px;font-size:17px}
  .card .code{color:var(--muted);font-size:13px}
  .card .exam{font-size:14px;margin:8px 0}
  .card .acts{display:flex;gap:6px;flex-wrap:wrap;margin-top:10px}
  .days{font-weight:600}
  .bar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:10px 0}
  .bar input{flex:1;min-width:200px}
  .chip.on{background:var(--accent);color:var(--bg);border-color:var(--accent)}
  .path{font-size:14px;margin:10px 0;color:var(--muted)}
  td.sz,td.ty{white-space:nowrap;color:var(--muted)}
  td.act{white-space:nowrap}
  tr.dir td:first-child a{font-weight:600}
  .note{background:var(--soft);border-left:3px solid var(--accent);padding:8px 12px;border-radius:0 6px 6px 0;font-size:14px;margin:12px 0}
</style>
</head>
<body>
<div class="wrap">
  <div class="top">
    <p class="crumb">University of Kelaniya &middot; Department of Industrial Management &middot; Level 2 Semester 2</p>
    <button id="theme" type="button"></button>
  </div>
  <h1>Y2S2 Study Hub</h1>
  <p class="lead">Study notes for each subject, plus every lecture slide, lab, reference and past paper in one place. Open anything or download it.</p>

  <h2 style="border-top:0;margin-top:20px">Subjects</h2>
  <div class="grid" id="cards"></div>

  <h2>File browser</h2>
  <div class="bar">
    <input type="search" id="q" placeholder="Search all files by name...">
    <span id="chips"></span>
  </div>
  <div class="path" id="path"></div>
  <table>
    <thead><tr><th>Name</th><th>Type</th><th>Size</th><th></th></tr></thead>
    <tbody id="list"></tbody>
  </table>
  <p class="note" id="bignote" hidden>Large files (videos and files over {{BIG}} MB) are not part of the website. When you use the hosted site their buttons go to the file on GitHub, where you can download it.</p>
  <p class="sm">Download buttons save a copy to your device. Slides open as PDF or PowerPoint; videos open in a new tab.</p>
</div>

<script>
const REPO="{{REPO}}";
const SUBJECTS={{SUBJECTS}};
const FILES={{FILES}};
const onPages=/github\\.io$/.test(location.hostname);
const enc=p=>p.split('/').map(encodeURIComponent).join('/');
const fileHref=f=>(onPages&&f.b)?'https://github.com/'+REPO+'/raw/main/'+enc(f.p):enc(f.p);
function size(b){return b>=1048576?(b/1048576).toFixed(1)+' MB':b>=1024?Math.round(b/1024)+' KB':b+' B'}
const TYPES={pdf:'PDF',pptx:'Slides',ppt:'Slides',docx:'Word',doc:'Word',xlsx:'Excel',md:'Notes',html:'Web page',mp4:'Video',json:'Data',py:'Code',ipynb:'Notebook',zip:'Zip',png:'Image',jpg:'Image'};
const ext=p=>(p.split('.').pop()||'').toLowerCase();
const kind=p=>TYPES[ext(p)]||ext(p).toUpperCase();

/* ---------- subject cards ---------- */
function daysTo(iso){return Math.ceil((new Date(iso)-new Date())/86400000)}
const cards=document.getElementById('cards');
SUBJECTS.forEach(s=>{
  const c=document.createElement('div');c.className='card';
  const next=s.exams.map(e=>({l:e[0],iso:e[1],d:daysTo(e[1])})).filter(e=>e.d>=0)[0];
  const examTxt=s.exams.map(e=>e[0]+' '+e[1].slice(8,10)+'.'+e[1].slice(5,7)).join(' &middot; ');
  const cd=next?(next.d===0?'<span class="days">today</span>':'in <span class="days">'+next.d+'</span> day'+(next.d===1?'':'s')):'finished';
  c.innerHTML='<h3></h3><div class="code"></div><div class="exam">Exam: '+examTxt+' ('+cd+')</div>';
  c.querySelector('h3').textContent=s.name;c.querySelector('.code').textContent=s.code;
  const acts=document.createElement('div');acts.className='acts';
  const n=document.createElement('a');n.className='btn pri';n.href=enc(s.folder)+'/Study%20Guides/index.html';
  n.textContent=s.notes?'Study notes ('+s.notes+' lessons)':'Lessons and slides';acts.appendChild(n);
  const b=document.createElement('a');b.className='btn';b.href='#'+enc(s.folder);b.textContent='Browse files';
  b.onclick=()=>{setTimeout(()=>document.getElementById('path').scrollIntoView({behavior:'smooth'}),30)};acts.appendChild(b);
  if(!s.notes){const t=document.createElement('span');t.className='tag';t.textContent='notes coming soon';acts.appendChild(t)}
  c.appendChild(acts);cards.appendChild(c);
});

/* ---------- file browser ---------- */
let filter='All';
const FILTERS=['All','PDF','Slides','Video','Notes','Other'];
const chips=document.getElementById('chips');
FILTERS.forEach(f=>{const b=document.createElement('button');b.className='chip'+(f==='All'?' on':'');b.textContent=f;b.onclick=()=>{filter=f;[...chips.children].forEach(x=>x.classList.toggle('on',x===b));draw()};chips.appendChild(b);chips.append(' ')});
const okType=p=>{if(filter==='All')return true;const k=kind(p);if(filter==='Other')return !['PDF','Slides','Video','Notes'].includes(k);return k===filter};
function cwd(){let h=decodeURIComponent(location.hash.slice(1));return h.replace(/^\\/+|\\/+$/g,'')}
const q=document.getElementById('q'),list=document.getElementById('list'),pathEl=document.getElementById('path');
function row(cells){const tr=document.createElement('tr');cells.forEach(c=>{const td=document.createElement('td');if(c.cls)td.className=c.cls;if(c.node)td.appendChild(c.node);else td.textContent=c.text||'';tr.appendChild(td)});return tr}
function link(text,href,cls){const a=document.createElement('a');a.textContent=text;a.href=href;if(cls)a.className=cls;return a}
function draw(){
  list.innerHTML='';const term=q.value.trim().toLowerCase();const dir=cwd();
  let anyBig=false;
  if(term){
    pathEl.textContent='Search results for "'+q.value.trim()+'"';
    FILES.filter(f=>f.p.toLowerCase().includes(term)&&okType(f.p)).slice(0,200).forEach(f=>{
      if(f.b)anyBig=true;
      const nm=document.createElement('span');nm.appendChild(link(f.p.split('/').pop(),fileHref(f)));
      const sub=document.createElement('div');sub.className='sm';sub.textContent=f.p.split('/').slice(0,-1).join(' / ');nm.appendChild(sub);
      list.appendChild(row([{node:nm},{text:kind(f.p),cls:'ty'},{text:size(f.s),cls:'sz'},{node:actions(f),cls:'act'}]));
    });
  }else{
    const parts=dir?dir.split('/'):[];
    const crumbs=document.createElement('span');crumbs.appendChild(link('All subjects','#'));
    parts.forEach((p,i)=>{crumbs.append(' / ');crumbs.appendChild(link(p,'#'+enc(parts.slice(0,i+1).join('/'))))});
    pathEl.innerHTML='';pathEl.appendChild(crumbs);
    const dirs=new Map(),files=[];
    const pre=dir?dir+'/':'';
    FILES.forEach(f=>{if(!f.p.startsWith(pre))return;const rest=f.p.slice(pre.length);const i=rest.indexOf('/');
      if(i<0){files.push(f)}else{const d=rest.slice(0,i);const o=dirs.get(d)||{n:0,s:0};o.n++;o.s+=f.s;dirs.set(d,o)}});
    if(parts.length){const up=link('..','#'+enc(parts.slice(0,-1).join('/')));list.appendChild(row([{node:up},{text:'Folder',cls:'ty'},{text:''},{text:''}]))}
    [...dirs.keys()].sort().forEach(d=>{const o=dirs.get(d);const tr=row([{node:link(d+'/','#'+enc(pre+d))},{text:'Folder',cls:'ty'},{text:o.n+' files, '+size(o.s),cls:'sz'},{text:''}]);tr.className='dir';list.appendChild(tr)});
    files.filter(f=>okType(f.p)).forEach(f=>{if(f.b)anyBig=true;
      list.appendChild(row([{node:link(f.p.split('/').pop(),fileHref(f))},{text:kind(f.p),cls:'ty'},{text:size(f.s),cls:'sz'},{node:actions(f),cls:'act'}]))});
    if(!dirs.size&&!files.length)list.appendChild(row([{text:'Nothing here.'},{text:''},{text:''},{text:''}]));
  }
  document.getElementById('bignote').hidden=!(onPages&&anyBig);
}
function actions(f){
  const s=document.createElement('span');
  const o=link('Open',fileHref(f));o.className='btn';o.target='_blank';o.rel='noopener';s.appendChild(o);s.append(' ');
  const d=link('Download',fileHref(f));d.className='btn';d.setAttribute('download',f.p.split('/').pop());s.appendChild(d);
  return s;
}
window.addEventListener('hashchange',()=>{q.value='';draw()});
q.oninput=draw;draw();
""" + THEME_JS + """
</script>
</body>
</html>
"""


def build_hub(files):
    subj = [{"folder": f, "code": c, "name": n, "exams": e, "notes": k} for f, c, n, e, k in SUBJECTS]
    s = HUB.replace("{{REPO}}", REPO).replace("{{BIG}}", str(BIG_MB))
    s = s.replace("{{SUBJECTS}}", json.dumps(subj, ensure_ascii=False))
    s = s.replace("{{FILES}}", json.dumps(files, ensure_ascii=False, separators=(",", ":")))
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    files = manifest()
    made = build_subject_pages(files)
    files = manifest()  # include the newly written subject pages
    build_hub(files)
    big = [f for f in files if f["b"]]
    print("files:", len(files), "| big (not published):", len(big), "| subject pages:", made)
