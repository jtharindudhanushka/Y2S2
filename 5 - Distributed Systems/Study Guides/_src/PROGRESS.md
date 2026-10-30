# Distributed Systems study guides: progress / pickup notes

Build one lesson: `sh ship.sh NN "Lesson NN - Name" render|build|commit` (render = print PDF + page montage; build = from_print.py + extract.py + build.py + index ready flag; commit = hub, git commit, push, Pages deploy).
Per lesson: print source `../../Print Notes/_src/lessonNN.html` (single source of the long text, B&W SVGs); `_src/lessonNN/{meta.json (with "src" line), mcq.json}`. `extract.py` writes qs.json (written = the print notes' "Exam-style questions" section) and short.html (cheat sheet + common mistakes). Lesson 8 also has `lab.html` (Lab 01, cut out of notes.html after the build step).
Sources: 11 unique PDFs (Lectures 01-08 incl. 06.1, Lab 01, Assignment 01); duplicates checked by MD5.

## STATUS: ALL DONE (lessons 1-10)
1 Intro DS (L01) | 2 Cloud computing (L02) | 3 NFV, SDN, Docker, AWS HA/DR (L03) | 4 Consistency, replication, FT, 2PC/3PC (L04) | 5 Infrastructure + virtualization (L05) | 6 Cloud mgmt, Kubernetes, Pods (L06, L06.1) | 7 Storage, GFS/HDFS/S3 (L07) | 8 Server virtualization + Lab 01 (L08) | 9 Assignment topics, not in slides | 10 Exam preparation.

## Caveats
- Lesson 9 is written from standard textbooks (no slides exist for consensus, MAS, search, P2P, MapReduce).
- Sections marked [outline] in Lesson 1 explain topics the slides only name.
- Lab 01 sheet prints "192.1681. X/24"; notes use 192.168.8.X/24 to match gateway 192.168.8.1.
- Worked-example numbers (consolidation, cost, scaling, quorum, gossip, PageRank, Chord) are illustrative calculations, not from slides.
