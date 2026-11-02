# 04 LDR (light dependent resistor)

**Parts:** 1 LDR, 1 x 10k resistor (brown, black, orange), 3 jumpers.

## Wiring (voltage divider)
```
5V ----[LDR]----+----[10k]---- GND
                |
                +---- A0
```
The LDR has no polarity, so either way round works.

## How to run
1. Unplug USB, build, plug in.
2. Upload `04_ldr.ino`, open Serial Monitor at 9600.
3. Cover the LDR with a finger, then shine a phone torch on it.

## Pass
The reading changes by a large amount. The LDR's resistance drops in bright light, so with this wiring the voltage on A0 rises in bright light and falls in the dark. Roughly: dark = low (below 300), bright = high (above 700).

## Fail
- No change: the LDR is not between 5V and A0, or the 10k is missing.
- Reads 0 or 1023 all the time: only one half of the divider is connected.

The thresholds you see here are the numbers you will need for the Exercise 4 "auto light".
