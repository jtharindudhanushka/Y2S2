# 06 Diode (1N4001)

**Parts:** 1N4001 diode (test both), 1 LED, 1 x 220 ohm resistor, jumpers.

## Wiring
Diode stripe = cathode. The LED lights only if current flows anode to cathode through the diode.

**Version A (diode forward):**
```
D9 ----[220]----LED(+ to -)----[diode anode > stripe]---- GND
```
Stripe towards GND.

**Version B (diode reversed):** same circuit with the diode turned round, stripe towards the LED.

## How to run
1. Unplug USB, build Version A, plug in.
2. Upload `06_diode_1n4001.ino`.
3. Unplug USB, flip the diode, plug in and run again (no re-upload needed).

## Pass
- Version A: the LED blinks.
- Version B: the LED stays dark (the diode blocks).

## Repeat
Test the second 1N4001 the same way.

## Fail
- LED blinks in both directions: the diode is shorted, replace it.
- LED never blinks in either direction: the diode is open (dead), or the LED/resistor wiring is wrong. Recheck Test 01 first.

Why this matters: Test 09 uses this diode backwards across the motor as a flyback diode.
