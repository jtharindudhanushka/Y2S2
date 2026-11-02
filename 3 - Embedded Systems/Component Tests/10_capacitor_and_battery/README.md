# 10 Capacitors (2 x 100 nF) and the 9V battery

**Parts:** 2 x 100 nF capacitors (marked `104`), 1 micro switch, 9V battery. A multimeter helps for the battery and is optional for the capacitors.

## A. Capacitor, debounce test (no multimeter needed)

### Wiring
Same button wiring as Test 02, plus the capacitor.

```
D2 ---- switch leg A     switch leg B ---- GND
capacitor: one leg to D2, the other leg to GND   (added in step 2 only)
```

### How to run
1. Build the button circuit **without** the capacitor. Upload `10_capacitor_and_battery.ino` and open Serial Monitor at 9600. Press the button 10 times firmly and count the lines printed.
2. Unplug USB, add the 100 nF capacitor across the button (D2 to GND), plug in, and press 10 times again.

### Pass
- Without the capacitor you may see more than 10 detections, because the contacts bounce.
- With the capacitor you should see close to exactly 10. The capacitor smooths the bounce.
- Repeat with the second capacitor.

### Notes
- Ceramic capacitors have no polarity, so either way round works.
- Contact bounce depends on the switch, so a clean switch may show 10 even without the capacitor. If both runs show exactly 10, you have not proved anything, but the capacitor is not harmful either. A multimeter on the capacitance range (about 100 nF) is the definitive test.

## B. 9V battery

- With a multimeter on DC voltage across the snap terminals: a good battery reads about 9 V (anything above 8 V is fine, below 7 V is flat).
- Without a multimeter, it is tested by Test 09: if the motor runs from it, the battery is good.
- Never short the snap terminals and never connect it to the Arduino 5V pin.
