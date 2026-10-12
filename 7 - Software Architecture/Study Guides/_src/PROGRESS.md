# Software Architecture study guides: progress / pickup notes

Build: `python _src/build.py NN` (content in `_src/lessonNN/{meta.json,notes.html,short.html,qs.json}`; template/build copied from AI/DSA).
Sources: `../Lecture Materials/*.pdf` (read with pdftotext; image-only slides rendered via PyMuPDF), `../In-Class Activities`, `../UniMart Full-Stack Monolithic Lab Series`, `../Group Assignment`.
Lecture 01-03 and C4 (13) slide images already viewed (invention vs innovation, four paths of digital change, problem vs solution, systems thinking iceberg, design-thinking mindset, diamond/groan zone, C4 banking examples).

## Plan (6 lessons + practical)
1 Introduction (DONE)
2 Good design: lecture 02 (cohesion, coupling, architecture vs design vs patterns, architect role table, quality attributes, ATAM, pattern list) + SOLID (lecture 03 slides 12-19)
3 Systems thinking and design thinking (lecture 03 slides 1-11; images viewed: iceberg, mindsets, groan zone, double diamond)
4 Requirements to architecture: guest session 09 slides 1-41 (+ domain->components, FR/NFR, drivers, SOLID real-world, over-engineering)
5 Monolith vs microservices + quality attributes: guest session slides 42-126 (Conway, REST, patterns, performance, scalability, reliability, security, SQL/NoSQL, worked exercises)
6 C4 model + case studies: lecture 13 C4, lecture 04 UniMart workshop (+ In-Class Activity 03 student answers), lecture 10 course registration, lecture 02 Zippo ride-hailing (read all tasks)
7 Practical: UniMart lab series (10 guides; read all) + Group assignment (7 docs; read all) + index page
Then: SA index page (copy AI index.html pattern, LESSONS list), set notes count in `_tools/build_hub.py` (7 - Software Architecture), run it, commit.
