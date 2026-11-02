# 03 Potentiometer (10k) and ADC

**Parts:** 1 x 10k potentiometer, 3 jumpers.

## Wiring
```
5V ---- pot left leg
A0 ---- pot middle leg (wiper)
GND --- pot right leg
```

## How to run
1. Unplug USB, build, plug in.
2. Upload `03_potentiometer.ino`, open Serial Monitor at 9600.
3. Turn the knob slowly from one end to the other.

## Pass
`ADC` sweeps smoothly from about 0 to about 1023 and `Vin` from about 0 V to about 5 V.

## Fail
- Stuck at 0 or 1023: the middle leg is not on A0, or an outer leg is not connected.
- Jumping around randomly: A0 is floating (nothing connected to the wiper).
- Sweep goes backwards: just swap the outer legs, that is fine.

This is the same ADC that Lesson 4 (voltmeter) and the LM35 and LDR tests use.
