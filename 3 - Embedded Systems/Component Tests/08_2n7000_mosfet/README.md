# 08 2N7000 MOSFET

**Parts:** 1 x 2N7000, 1 LED, 1 x 220 ohm, jumpers.

## Pinout
Flat face towards you, legs down. For most 2N7000 parts (ON Semi / Fairchild) the order left to right is **S (source), G (gate), D (drain)**. Some makers use D, G, S instead. Check page 1 of `Lecture Materials/06 - 2N7000 N Channel MOSFET Datasheet.PDF`. If the LED does not light, swap the two outer legs and try again.

## Wiring
```
D9 ---- G
5V ----[220]----LED(+ to -)---- D
S ---- GND
```
No gate resistor is needed for this brief test, the gate draws almost no current.

## How to run
1. Unplug USB, build, plug in.
2. Upload `08_2n7000_mosfet.ino`.

## Pass
The LED blinks once a second.

## Fail
- Never lights: try swapping source and drain (the pinout for your brand may be reversed). Check the datasheet.
- Always lit: the MOSFET is shorted, or the gate is floating. Make sure the gate goes to D9.
- A MOSFET can be damaged by static. Don't wipe your feet and handle it by the body.

Gate threshold is about 1 to 3 V, so the Uno's 5 V pin switches it fully on.
