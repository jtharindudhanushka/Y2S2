# Software Architecture study guides: progress / pickup notes

Build: `python _src/build.py NN` (content in `_src/lessonNN/{meta.json,notes.html,short.html,qs.json}`; template/build copied from AI/DSA).
Sources: `../Lecture Materials/*.pdf` (read with pdftotext; image-only slides rendered via PyMuPDF), `../In-Class Activities`, `../UniMart Full-Stack Monolithic Lab Series`, `../Group Assignment`.
Lecture 01-03 and C4 (13) slide images already viewed (invention vs innovation, four paths of digital change, problem vs solution, systems thinking iceberg, design-thinking mindset, diamond/groan zone, C4 banking examples).

## Plan (revised; lessons 1-5 DONE and pushed)
1 Introduction, 2 Good design + architect + SOLID, 3 Systems/design thinking, 4 Problem to system design (guest slides 1-41), 5 Monolith to microservices (guest slides 42-72): DONE
6 DONE. (was: guest session slides 73-99 (performance, caching, load balancing, scalability, stateless, sequential/parallel, sync/async, reliability and nines, SPOF, outages, timeout/retry/circuit breaker, security: authn/authz, never trust client, TLS/hashing, SQL injection, config/secrets, reuse ladder, library vs framework, SQL vs NoSQL, team agreements). Text already extracted earlier in session; re-run: pdftotext -f 73 -l 99 -layout on lecture 09.
7 DONE. (was: guest slides 100-126 (13-question worksheet, University Registration exercise, Food Delivery at Scale, Ticket Booking, putting it together, 7-question checklist). Read with pdftotext -f 100 -l 126.
8 DONE. (was: C4 model (lecture 13; viewed) + case studies: lecture 04 UniMart workshop (+ In-Class Activity 03 student answers), lecture 10 course registration, lecture 02 Zippo ride-hailing (read all tasks)
9 DONE (UniMart labs). (was: UniMart lab series (10 guides; read all) + Group assignment (7 docs; read all)
Then: SA index page (copy AI index.html pattern; LESSONS list), set notes count in `_tools/build_hub.py` (7 - Software Architecture), run it, commit.
