# Regenerates the Lesson tabs that combine Part 1 (orig/, this year's notes) and Part 2 (Print Notes), then builds.
# Usage: bash regen.sh
set -e
cd "$(dirname "$0")"
P="../../Print Notes/_src"
python -I from_print.py "$P/lesson03.html" lesson02/notes.html "Sources: lecture 03 slides, the six I/O-port lecture recordings from 2020 (section L), Exercises 1 and 2 with answers, and the peer notes. Printable as <code>Print Notes/Lesson 03 - IO Port Programming.pdf</code>." orig/lesson02_notes.html
python -I from_print.py "$P/lesson04.html" lesson03/notes.html "Sources: lecture 04 slides, the four polling and interrupt lecture recordings from 2020 (section L), Exercise 3 and the peer notes. Printable as <code>Print Notes/Lesson 04 - Polling and Interrupts.pdf</code>." orig/lesson03_notes.html
python -I from_print.py "$P/lesson05.html" lesson04/notes.html "Sources: lecture 05 slides, the five ADC lecture recordings from 2020 (section L), Exercise 4, the 1023-or-1024 note, the LM35 and LDR datasheets. Printable as <code>Print Notes/Lesson 05 - Analog to Digital Conversion.pdf</code>." orig/lesson04_notes.html
if [ -f orig/lesson05_notes.html ]; then
python -I from_print.py "$P/lesson06.html" lesson05/notes.html "Sources: lecture 06 slides, the two transducer lecture recordings from 2020 (section L), and the AH1815, ADXL335, BC547, 2N7000 and 1N4001 datasheets. Printable as <code>Print Notes/Lesson 06 - Transducers.pdf</code>." orig/lesson05_notes.html
fi
python -I from_print.py "$P/lesson07.html" lesson06/notes.html "Sources: lecture 07 slides (Systems 10&ndash;13), Exercise 5, and the two timing-and-counting lecture recordings from 2020 (section L). Printable as <code>Print Notes/Lesson 07 - Timing and Counting.pdf</code>." orig/lesson06_notes.html
python -I from_print.py "$P/lesson08.html" lesson07/notes.html "Sources: lecture 08 slides (System 15), Exercise 6, and the three PWM lecture recordings from 2020 (section L). Printable as <code>Print Notes/Lesson 08 - Pulse Width Modulation.pdf</code>." orig/lesson07_notes.html
python -I build.py
