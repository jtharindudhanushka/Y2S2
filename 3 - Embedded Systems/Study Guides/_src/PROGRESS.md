# Embedded Systems study guides: progress / pickup notes

Build: `python _src/build.py NN` (or no argument for all). Content in `_src/lessonNN/{meta.json,notes.html,prac.html,short.html,qs.json}`; template and build copied from Software Architecture (tabs: Lesson, Practice questions, Practical question, Short note).
Sources: `../Lecture Materials/*.pdf` (text via pdftotext; slide images rendered with PyMuPDF), `../Exam Support Materials`, `../Peer Notes/Transcription.md` (40 handwritten pages, verified against the PDF), `../Peer Notes/Last Year Question - Practical.jpeg` (cogni tester).

## STATUS: ALL DONE (lessons 1-10 built, index page written, hub notes count = 10)
1 Intro + microcontrollers | 2 I/O port programming (Ex 1, 2) | 3 Polling and interrupts (Ex 3) | 4 ADC (Ex 4) | 5 Transducers | 6 Timing and counting (Ex 5) | 7 PWM (Ex 6) | 8 Serial (Ex 7) | 9 Practical exam prep + past paper + mock practical paper | 10 Written exam prep + mock written paper.

## Caveats
- Code was checked by hand and with Python arithmetic (delay cycles, timer values, UBRR), not compiled on a board.
- Exercise 1 answer pages: only the byte sizes (920/200/172, 986/260/202) and the 220 ohm answer were taken from the answer key; the code is original.
- Lessons 5, 7, 8 mention datasheet values (BC547, 2N7000, 1N4001, ADXL335, AH1815) taken from the datasheet extracts; Timer1/Timer2 register tables differ from the simplified sheet (noted in lesson 7).
- The lecturer's Exercise 3 answer used a different LED bit mapping from the one in lesson 3; both are valid.
