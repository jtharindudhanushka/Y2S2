I have the Distributed Systems & Cloud Computing (INTE 22253, University of Kelaniya) theory exam on 02.11.2026. I know almost nothing about the subject. Build me complete study materials, the same way we did for Embedded Systems.

Working folder: "C:\Users\jthar\OneDrive\Documents\UOK\Exams\Y2S2\5 - Distributed Systems"
Repo: the Y2S2 folder is the git repo jtharindudhanushka/Y2S2. Pages deploy: `gh workflow run pages.yml --repo jtharindudhanushka/Y2S2 --ref main`.

## Step 1: analyse ALL the materials first (do not build anything yet)
- Read every PDF in full: `Lecture Materials/`, `Collected Notes/lec notes/` (including the `Cloud and distributed/` subfolder), and `Assignments & Quizzes/`.
- Many files are duplicates (same size). Check with a hash, read each unique file once, and tell me which ones are duplicates.
  - The peer/eKel set adds Lecture 02, 04, 07 and 08, plus Assignment 01, which are NOT in `Lecture Materials/`.
  - There is also Lab 01. Ignore `__MACOSX`.
- Read text with PyMuPDF (`fitz`). also read all slides as image slides that are mostly diagrams, render pages to PNG and look at them. Use montages to save tokens. Do not skip image-only slides.
- Then report back to me:
  1. the unique file list;
  2. per lecture, every topic and subtopic (nothing missed), in lecture order;
  3. what the lab and assignment ask;
  4. topics in `Overview.md` that no file covers;
  5. a proposed lesson split.
- Wait for my OK before building.

## Step 3: printable notes (black and white, A4 PDF)
- One PDF per lesson in `5 - Distributed Systems/Print Notes/`, sources in `Print Notes/_src/`.
- Reuse the Embedded Systems pipeline: copy `3 - Embedded Systems/Print Notes/_src/print.css` and `render.ps1` (Edge headless print to PDF).
- Write for a complete beginner, with full theory: explain every term the slides only name, why things exist, how they work step by step, comparisons and trade-offs.
- Include B&W inline SVG diagrams (architectures, client-server/P2P, RPC/RMI flow, clocks and ordering, replication/consistency, virtualization layers, IaaS/PaaS/SaaS stack, deployment models, etc., whatever the slides cover).
- Each lesson also needs:
  - worked examples where there is calculation or algorithm tracing (e.g. Lamport/vector clocks, Berkeley/Cristian, elections, mutual exclusion, if covered);
  - comparison tables;
  - exam-style questions with model answers;
  - a "Common mistakes" table;
  - a 1-page cheat sheet at the end.
- No padding, but explain line by line where needed.
- Render each PDF, then check the pages as PNG montages: fix overlapping or cut-off figures and bad page breaks.

## Step 2: HTML study guides (beginner-friendly)
- In `5 - Distributed Systems/Study Guides/`, using the same system as `3 - Embedded Systems/Study Guides/_src/`: `template.html`, `build.py`, and per-lesson `meta.json`, `notes.html`, `qs.json` (mcq + written), `short.html`.
- Use the same tabs: Lesson / Practice questions / Short note (plus a Lab/Assignment tab if useful), with light/dark theme and theme-aware SVGs (`from_print.py` converts the print notes).
- Overwrite the current placeholder `Study Guides/index.html` and add the hub links (`_tools/build_hub.py`).
- Add final "Exam preparation" pages: likely questions per lesson, and definitions to memorise.

## Rules
- Do one lesson at a time. After each lesson, show me the PDF and ask for a green light before the next. Work fast and don't waste tokens.
- Everything must come from the materials. Where you add outside explanation for beginners, keep it correct and standard (Coulouris / Tanenbaum level), and don't contradict the slides.
- Commit after each lesson, then push and run the deploy. after rwading html one shoud be able to udnertsand everything evem n he didnt went for lectures asnd print notes the same 
