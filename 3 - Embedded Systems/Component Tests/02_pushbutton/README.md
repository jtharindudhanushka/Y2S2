# 02 Pushbutton (micro switch)

**Parts:** 1 micro switch (test both), 2 jumpers.

## Wiring
```
D2 ---- switch leg A        switch leg B (diagonally opposite) ---- GND
```
A micro switch has 4 legs. The legs on the same side are always joined inside, and the two sides connect only when pressed. Straddle the breadboard centre gap, and use two legs that are diagonally opposite each other.

## How to run
1. Unplug USB, build, plug in.
2. Upload `02_pushbutton.ino`, open Serial Monitor at 9600.

## Pass
- Released: the monitor prints `1`.
- Pressed: it prints `0` and the on-board LED (pin 13) lights.

## Repeat
Do the second switch the same way.

## Fail
- Always `0`: the two legs you used are on the same side. Rotate the switch 90 degrees.
- Always `1`: not connected to GND, or a dead switch.
- No pull-up resistor is needed. The sketch turns on the Uno's internal one. This is the same trick as `PORTD |= 0b00000100` in the lecture.
