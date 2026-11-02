# 00 Board and USB

**Parts:** Arduino Uno and USB cable only.

## Wiring
None. Plug the Uno into the PC.

## How to run
1. Open `00_board_and_usb.ino`.
2. Tools > Board > Arduino Uno; Tools > Port > the COM port that appears when you plug in.
3. Click **Upload** (right arrow).
4. Open Tools > Serial Monitor, set the baud (bottom right) to 9600.

## Pass
- The small `L` LED next to pin 13 blinks once a second.
- The `TX` LED flickers during upload.
- The Serial Monitor prints `hello - LED on` / `hello - LED off` every half second.

## Fail
- No port listed: try another USB cable (some are charge-only) or another USB port; install the CH340 driver if you have a clone board.
- Upload error `avrdude: stk500_getsync()`: wrong board or port selected, or something is wired to pins 0 or 1 (disconnect it).
- Garbled text: the Serial Monitor baud is not 9600.
