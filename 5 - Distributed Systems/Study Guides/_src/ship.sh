#!/bin/sh
# Usage: sh ship.sh NN "Lesson NN - Name" [render|build|commit]
# render: print PDF + page montage; build: study guide + index ready flag; commit: git commit, push, deploy
set -e
N=$1; NAME=$2; STEP=$3
DS="/c/Users/jthar/OneDrive/Documents/UOK/Exams/Y2S2/5 - Distributed Systems"
S="/c/Users/jthar/AppData/Local/Temp/claude/C--Users-jthar-OneDrive-Documents-UOK-Exams-Y2S2/5ab2a52c-e483-464d-861e-b83f35c17818/scratchpad"
if [ "$STEP" = render ]; then
  cd "$DS/Print Notes/_src" && powershell -NoProfile -File render.ps1 lesson$N "$NAME" >/dev/null
  rm -f "$S"/mont/*; python "$S/mont.py" "../$NAME.pdf" P$N 1-99 4 400 "$S/mont"
fi
if [ "$STEP" = build ]; then
  cd "$DS/Study Guides/_src"
  python from_print.py "../../Print Notes/_src/lesson$N.html" lesson$N/notes.html "$(python -c "import json;print(json.load(open('lesson$N/meta.json',encoding='utf-8'))['src'])")"
  python extract.py $N && python build.py $N
  python - "$NAME" <<'PY'
import sys,re
p="../index.html"; s=open(p,encoding="utf-8").read()
f=sys.argv[1]+".html"
s=re.sub(r'(file:"'+re.escape(f)+r'",ready:)false',r'\1true',s)
open(p,"w",encoding="utf-8").write(s); print("ready" , f in s)
PY
fi
if [ "$STEP" = commit ]; then
  cd "$DS/.." && python _tools/build_hub.py >/dev/null 2>&1 || true
  git checkout -- "2 - Mobile Applications/Study Guides/index.html" 2>/dev/null || true
  git add "5 - Distributed Systems" ":(exclude)5 - Distributed Systems/Collected Notes/lec notes/__MACOSX" index.html
  git commit -q -m "Distributed Systems: $NAME (print notes PDF, study guide)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
  git push -q && gh workflow run pages.yml --repo jtharindudhanushka/Y2S2 --ref main && git log --oneline -1
fi
