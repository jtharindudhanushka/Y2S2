# 07 BC547 transistor

**Parts:** BC547 (test both), 1 LED, 1 x 220 ohm, 1 x 1k ohm (brown, black, red), jumpers.

## Pinout
Flat face towards you, legs down. Left to right: **C (collector), B (base), E (emitter)**. Confirm against `Lecture Materials/06 - BC54X Series NPN Transistor Datasheet.pdf` page 1.

## Wiring
```
D9 ----[1k]---- B
5V ----[220]----LED(+ to -)---- C
E ---- GND
```
The LED sits between 5V and the collector. The transistor completes the path to GND.

## How to run
1. Unplug USB, build, plug in.
2. Upload `07_bc547_transistor.ino`.

## Pass
The LED blinks once a second, switched by the transistor.

## Repeat
Test the second BC547.

## Fail
- LED always on: legs wrong (collector and emitter swapped can leak), or the transistor is shorted.
- LED never on: base resistor not on D9, wrong leg order, or a dead transistor.
- If it works with the second transistor but not the first, the first is damaged.
