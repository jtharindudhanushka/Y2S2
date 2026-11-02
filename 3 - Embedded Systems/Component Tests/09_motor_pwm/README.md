# 09 DC motor, flyback diode and PWM

**Parts:** 6-9V DC motor, BC547, 1 x 1k, 1N4001, 9V battery with snap connector, jumpers. Test 07 (BC547) and Test 06 (diode) must have passed first.

## Wiring
Power the motor from the **9V battery**, not from the Uno's 5V pin. A motor can draw more current than the board can supply and will reset it. The grounds must be shared.

```
D9 ----[1k]---- BC547 base (B)
BC547 emitter (E) ---- GND
BC547 collector (C) ---- motor terminal 1
motor terminal 2 ---- battery +
battery - ---- GND (same GND rail as the Uno)
1N4001 across the motor: stripe (cathode) to battery +, other end to the collector side
```
The diode sits across the motor terminals, **backwards** compared with the current flow. It absorbs the voltage spike when the motor switches off (flyback or freewheel diode). Without it the spike can kill the transistor.

## How to run
1. Unplug USB, build with the battery **disconnected**. Check the wiring, then clip the battery on.
2. Plug in USB, upload `09_motor_pwm.ino`.

## Pass
- The motor spins for 1.5 s, stops for 1.5 s.
- Then it smoothly speeds up and slows down, repeatedly.

## Fail
- Nothing happens: battery flat, BC547 pins wrong, or common GND missing.
- Motor runs all the time: BC547 shorted, or collector and emitter swapped.
- Uno resets when the motor starts: you powered the motor from the Uno. Use the battery.
- Does not start at low duty: normal. A motor needs a minimum voltage, usually from duty of about 60 upward.
- Transistor gets warm: unplug. Check the diode direction.
