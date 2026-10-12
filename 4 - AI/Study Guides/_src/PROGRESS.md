# AI study guides: progress / pickup notes

Build: `python _src/build.py NN` (same system as DSA; content in `_src/lessonNN/{meta.json,notes.html,short.html,qs.json}`; template copied from DSA).
Alignment of sources: `../Peer Notes/Lesson Alignment.md` (guide numbers 1-14 vs plan weeks vs peer notes).
Converted peer notes (read these, not the raw PDFs): `../Peer Notes/Notes - Yasiru (converted).md`, `Notes - Geethma (transcribed).md`, `Peer Made Notes 1 (converted).md`.

## Done
- Peer note conversions (all three sets) + alignment doc.
- Lessons 01-05 (built, pushed); AI index page done (set ready:true per lesson in index.html and bump the notes count in _tools/build_hub.py).

## To do (in order), each: read slides (pdftotext) + peer-made tab text + Yasiru + Geethma, then write guide
3 DONE. (was: slides `07 - Introduction to Google ADK.pdf`, n8n assignment/lab files, `Web Resources & Videos/02 - Building AI Agents.md`, peer-made L1 tab 7)
4 DONE. (was: peer-made L3; Yasiru 3; Geethma AI 3; `Web Resources & Videos/04 *.md` UCS and A*)
5 DONE (ML + regression combined; lesson 6 = neural nets only). (was: peer-made L5, L6; Yasiru 5, 6; Geethma AI 4 pp.8-12, AI 5, AI 6)
6 DONE. (was: peer-made L7; Yasiru 7; Geethma AI 6 p3-4, AI 7). Note: guide-building helper scripts live outside the repo; SVGs are inline in notes.html.
7 DONE (RNN, vanishing gradient, LSTM, CNN, U-Net; sources: slides 09 (images, read as PNG), peer-made L8 + L10).
8 DONE. No slides exist; course facts (discriminative vs generative, next-word prediction, AI map, 3-stage training) are marked; attention/transformer-block sections are labelled Background (not from course).
9 DONE. Course parts: image-generation slide + colourisation assignment notebook (U-Net code, read fully). Diffusion/GAN/VAE section labelled Background (no source).
10 Reinforcement Learning (peer-made L12; Geethma AI 4 p11-12, AI 5 p1-2)
11 Genetic Algorithms (slides 05; peer-made L4; Yasiru 4; Geethma AI 4 pp1-7; fix the roulette % error in Geethma)
12 Swarm Intelligence (NO source material: placeholder)
13 Fuzzy Logic (slides 10; peer-made L9)
14 XAI and Ethics (slides 11; peer-made L11; EU case assignment md)
Then: AI index page (copy DSA index.html pattern; LESSONS list), set SUBJECTS notes count in `_tools/build_hub.py`, run it, commit.
