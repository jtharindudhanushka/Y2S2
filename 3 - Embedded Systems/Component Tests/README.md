# Component Tests

Test every part of your kit one at a time, in this order. Each folder is an Arduino sketch folder: open the `.ino` inside it with the Arduino IDE, and read the `README.md` beside it for the wiring and how to run it.

| # | Folder | Tests |
|---|---|---|
| 00 | `00_board_and_usb` | Arduino Uno, upload, USB serial link |
| 01 | `01_led_and_220_resistor` | 10 LEDs, 220 ohm resistors |
| 02 | `02_pushbutton` | 2 micro switches |
| 03 | `03_potentiometer` | 10k pot, ADC |
| 04 | `04_ldr` | LDR with 10k divider |
| 05 | `05_lm35` | LM35 temperature sensor |
| 06 | `06_diode_1n4001` | 2 x 1N4001 |
| 07 | `07_bc547_transistor` | 2 x BC547 |
| 08 | `08_2n7000_mosfet` | 2N7000 |
| 09 | `09_motor_pwm` | DC motor, flyback diode, PWM |
| 10 | `10_capacitor_and_battery` | 2 x 100nF capacitors, 9V battery |

## Rules for every test

1. Select **Tools > Board > Arduino Uno** and the correct **Tools > Port** once.
2. **Unplug the USB cable before changing any wiring**, plug it back in, then upload.
3. Top breadboard rail = 5V, bottom rail = GND. Join the Arduino `5V` and `GND` pins to the rails with jumpers.
4. Open **Tools > Serial Monitor** and set the baud to **9600** whenever a README says so.
5. Pin numbers below are Arduino pin numbers (D2, D9, A0 and so on).
6. If a test fails, swap in a spare part of the same type before deciding the part is dead. Most failures are a wrong row on the breadboard or a part turned the wrong way round.

Tick them off as you go:

- [ ] 00 board  - [ ] 01 LEDs  - [ ] 02 buttons  - [ ] 03 pot  - [ ] 04 LDR  - [ ] 05 LM35
- [ ] 06 diodes  - [ ] 07 BC547  - [ ] 08 2N7000  - [ ] 09 motor  - [ ] 10 caps and battery
