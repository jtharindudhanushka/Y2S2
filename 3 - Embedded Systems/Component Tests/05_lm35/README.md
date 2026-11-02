# 05 LM35 temperature sensor

**Parts:** 1 LM35, 3 jumpers.

## Wiring
Hold the LM35 with the **flat face towards you and the legs pointing down**. Left to right the legs are:

```
Left   (+Vs)  ---- 5V
Middle (Vout) ---- A0
Right  (GND)  ---- GND
```

**Check the orientation twice before plugging in USB.** If the legs are reversed the sensor heats up quickly. If it ever feels warm, unplug immediately.

## How to run
1. Unplug USB, build, plug in.
2. Upload `05_lm35.ino`, open Serial Monitor at 9600.
3. Pinch the metal-free flat body between your fingers for 20 seconds.

## Pass
- At rest it shows about room temperature (roughly 24 to 33 C).
- Pinching it makes the number rise by a few degrees. Letting go makes it fall.

## Fail
- Reads 0 or very low: the middle leg is not on A0, or the sensor is not powered.
- Reads about 60 C or more and the sensor is hot: legs are reversed. Unplug and swap Vs and GND. Try a second LM35 if the first one is damaged.
- Readings jump by 1 to 2 degrees: normal. The LM35 is noisy on an Uno. Averaging several readings smooths it.

Same formula as Exercises 6 and 7: `temp = ADC x 5.0 / 1024 x 100`.
