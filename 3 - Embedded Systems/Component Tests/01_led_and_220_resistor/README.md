# 01 LED and 220 ohm resistor

**Parts:** 1 LED (test all 10 in turn), 1 x 220 ohm resistor (red, red, brown), 2 jumpers.

## Wiring
```
D9 ----[220 ohm]----(+ long leg) LED (- short leg)---- GND
```
- The LED's long leg is the anode (+), the short leg and the flat edge on the body are the cathode (-).
- Put the resistor and the LED in different breadboard rows, joined by one end each.

## How to run
1. Unplug USB, build the circuit, plug USB back in.
2. Open `01_led_and_220_resistor.ino`, Upload.

## Pass
The LED blinks (0.3 s on, 0.3 s off).

## Repeat
Swap in each LED, one at a time, with the same resistor. Then keep one good LED and swap the 10 resistors. Note which parts fail.

## Fail
- Never lights: turn the LED round. If still dark with a different LED too, check that the resistor row is connected to D9 and the LED's other leg reaches GND.
- Very dim: the resistor may be much larger than 220 ohm (check its colour bands).
- Never connect an LED without a resistor, it can burn out the LED or the pin.
