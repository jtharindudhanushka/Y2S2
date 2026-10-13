# Embedded Systems: Peer Notes (transcription)

Source: `Embedded Systems_260820_112202.pdf` (40 handwritten/annotated pages, class notes of a peer). Each page is a lecture slide with handwritten annotations in blue. Slide text is summarised in *italics*; the handwritten notes are transcribed word for word (spelling tidied). `[?]` marks a word that is hard to read. These notes are incomplete (the peer stopped taking notes at some point), so every lesson study guide fills the gaps from the lecture slides.

---

# 01. Introduction to Embedded Systems (25/06/2026)

### p1 Embedded System
*Slide: computer system embedded into some other system; used to get some dedicated task done; performs physical computing: Sensors, Processor, Actuators (input, process, output); usually operates under strict constraints. What are they?*

- Sensors capture the state of the actual world, which you feed to the processor as an input.
- Processor processes the inputs according to instructions provided (by programming) to produce outputs. These instructions are known as **Firmware** (it doesn't change).
- The processed outputs drive the actuators (ex: motor of a fan).
- ex: Sense temp, if > 30, turn on fan.

**Constraints:**
1. Cost (ES must be cheap)
2. Weight / Size (must be small)
3. Power consumption (must consume least amount of power)
4. Real-time performance

*Slide: Example, Anti-lock Braking System (ABS). What is the main task? How is it achieved?*
- Main task: apply equal brake to all 4 wheels.
- How? RSS measures Rotational speed per min. Actuator = hydraulic pump. If one wheel has less brakes than the other 3, the pump releases fluid to that wheel until all 4 wheels are rotating at the same speed.

### p2 Flight controller, Evolution, Future
*Slide: Example, Flight Controller System (quadcopter with accelerometer, gyroscope, radio control receiver, processor, 4 ESCs with motors, battery).*
- Main task: stably fly the drone.
- How: Sensors: Gyroscope, Accelerometer, Radio control receiver (receives pilot's radio signals).
- Processor varies the speed of the 4 motors (actuators) based on the inputs.

*Slide: Evolution. In the early days (Apollo guidance system, Minuteman missile guidance system) / Today (agriculture, manufacturing robot, medical MRI, consumer electronics).*
- Early days: Military and scientific purposes only, because expensive.

*Slide: Future. Embedded computing market in USD billion, rising from about $101B (2022) to about $178B (2032).*

### p3 Shift of industry, Components
*Slide: Shift of Industry. What is the secret behind exponential revenue growth? (Nokia 3310 vs a later phone with fewer chips.) What are the advantages?*
- Majority of functionalities have shifted from hard-wired electronics to software.
- Software implemented functions, aka **Embedded Systems**.
- Advantages: 1. Easier to implement (easy to get software on top of generic hardware). 2. Low cost. 3. Easier to debug. 4. Easier to modify.

*Slide: Components. CPU in the middle connected to RAM, ROM, Input/Output ports and Clock/timers/counters. The I/O ports connect to sensors and actuators (robot arm picture).*
- RAM: to keep temp inputs.

### p4 Microprocessor vs microcontroller
*Slide: Microprocessor-based (separate Microprocessor, ROM, Serial Ports, Clock, I/O Interface, RAM, Other Peripherals) vs Microcontroller-based (CPU, ROM, Clock, I/O, RAM, Serial ports, other peripherals all in one chip). What are the pros and cons?*
- Microprocessor-based = separate components on one circuit board. Therefore: **Single Board Computer**.
- Microcontroller-based = all the components are in one chip. Therefore: **Single Chip Computer**.

| Microprocessor-based (pros) | Microcontroller-based (cons) |
|---|---|
| Spec is very high | Cannot replace separate components |
| Higher performance because components are separate | Everything is miniature, therefore not high spec |
| Can replace each component | |

| Microprocessor-based (cons) | Microcontroller-based (pros) |
|---|---|
| High spec, therefore components are expensive | Cheap |
| Consume a lot of power and generate a lot of heat | Power efficient and less heat |
| | Compact |

### p5 Which to choose
*Slide: Microprocessor-based or Microcontroller-based? (traffic camera with Raspberry-Pi-type board; smoke/fire alarm with a small chip). Why are the majority of embedded systems microcontroller-based?*
- Depends on the system.
- ex 1: Adaptive traffic control system. Data coming from the camera requires image processing. For that you need a lot of RAM. Therefore this will have to be microprocessor based. Also no space or power supply constraints.
- ex 2: Fire alarm system. Here microcontroller based, because binary sensors are used; inputs and outputs are binary values. Therefore large processing power is not required. Also operated by a battery and is small, therefore low power consumption and compactness is a necessity. Must be low cost as well because fire alarms are bought in bulk.
- For most ES, power hungry, bulky systems are not needed.

---

# 02. Introduction to Microcontrollers (02/07/2026)

### p6 What is a microcontroller
*Slide: a microcontroller integrates CPU, RAM, ROM, ADC, OSC, I/O port, Serial port, PWM, Timer.*
- Microcontroller is a single chip computer.
- ROM is larger than RAM because: RAM is used to store variables and controllers which are limited, while ROM is used to store firmware which is bulky.
- **ADC**: Analog to Digital Converter, used to convert signals as the processor can only understand digital signals. (Most inputs are analog: velocity, temp, speed etc.)
- **OSC**: Oscillator is used to give precise clock pulses (1, 0, 1, 0 ...) to the processor.
- **PWM** (Pulse Width Modulator): used to give analog-like output (ex: not direct ON/OFF but dim a light).
- **Timer**: to measure elapsed time.
- **I/O ports**: to get inputs and deliver outputs.
- **Serial port**: for data communication (ex: MC to MC communication).

### p7 Core components
*Slide: Core Components. Oscillator, SPI / I2C / USART (serial communication), Timers T0 T1 T2, RAM, ROM, EEPROM (memory), ADC, PWM, CPU, I/O ports A to E, RESET and power supply.*
- ROM aka **Flash** because it's writable but only by the developer.
- **EEPROM**: to keep the settings of the system. (Things that are non-volatile but changeable.)
- Developer stores firmware in ROM while EEPROM data is stored by the user.
- **Serial communication** (data communication):
  - USART: Universal Synchronous Asynchronous Receiver Transmitter (MC to PC communication)
  - SPI: Serial Peripheral Interface } (MC to MC / memory chip)
  - I²C: Inter-Integrated Circuit } nearby devices
- 2 methods for nearby communication because: SPI is fast but uses 4 wires; I²C is slower but uses only 2 wires (aka Two Wire Interface, TWI).
- **I/O port categories** (A, B, C ...): more ports mean more I/O pins. The number is decided depending on the requirements.
- **RESET**: used to reset the MC. Memory cleared and instructions are executed from the very first instruction.

### p8 I/O port and internal working
*Slide: I/O Port. What is an I/O port? How can external electronics alter the flow of program execution? How can a program in execution drive external electronics? (8-bit port register 10110011 connected to pins.) Slide: Internal Working with pseudocode `if bit 0 of PORT = 0 then bit 2 of PORT <- 1 else bit 2 of PORT <- 0`; a switch on pin 0 (through a resistor to 5 V) and an LED on pin 2.*
- 8 bit register.
- An I/O port is a register associated with MC pins.
- Pins we count like arrays (0 to 7).
- Logic high: 2 to 5 V. Logic low: 0 to 1 V.
- Pin 0 is connected through the resistor to 5 V and through the switch to ground.
- Bit value represents the logic level of the pin.
- (1) When the switch is off, pin 0 is connected to 5 V, therefore logic level high shows bit value 1.
- (2) When the switch is on (in image), pin 0 is connected to ground directly (no resistance), therefore logic level low shows bit value 0.
- Extra: the resistor is used to prevent a short circuit from 5 V being directly connected to ground.

### p9 Programming flow, word size
*Slide: Programming. PC, high level language, compiler/assembler, `.hex` file, programmer, system board, CPU executes from ROM, sensors and actuators.*
- High level language -> compiler/assembler -> Machine code file (Hex file). It is called a hex file because it is written in hexadecimal (almost machine code).
- Upload the hex file to the ROM of a blank MC (using the programmer). Plug the programmed MC into the system board.
- CPU takes instructions (one by one) from ROM. Sensors give input, actuators take output.

*Slide: Word Size (no. of bits processed at a time). 8, 16 or 32-bit? Trend: 8-bit has no growth in the microcontroller market (CAGR 11.7 % for 2022 to 2030, "Compound Annual Growth Rate"). Ease of learning. Cost.*
- When selecting an MC you need to consider academic purposes: the ideal selection is **8 bit**. Later you can migrate to 32.
- Ease of learning: 8 is easier to learn considering 32.
- Cost: 8 is also cheaper (it has free and open-source tools, plus a large community).

### p10 Families, ATmega328P
*Slide: Families. 8-bit families: 68HC08/68HC11 from NXP (formerly Motorola), 8051 from Intel, AVR from Microchip (formerly Atmel), PIC from Microchip, STM8 from STMicroelectronics. Why AVR?*

*Slide: ATmega328P features: Harvard RISC architecture; 131 single clock cycle instructions (mostly); 8-bit 20 MHz CPU with 14-bit PC; 32 KB 16-bit word addressable program ROM; 2 KB byte addressable RAM and 1 KB EEPROM; three I/O ports with 23 I/O pins; 3 timers, 6 PWM channels and 6-channel 10-bit ADC; one USART, two SPI and an I2C; 28 pin PDIP.*
- ATmega328P: made by Atmel; the "mega" part is the series name.
- 20 MHz is the *recommended* maximum, but overclock possible.
- PDIP = Plastic Dual Inline Package (important for academics as it is breadboard compatible).
- Why ATmega328P? Because it is the most popular MC; most documented MC; heart of the Arduino Uno development board (mostly used dev board).

### p11 Development boards, Arduino
*Slide: Microcontroller-based development boards: Atmel Xplained, MikroElektronika EasyAVR, Arduino Uno, a home-made board. Slide: Arduino, an open-source, low cost, easy to use hardware and software platform for prototyping embedded systems (Uno, Mega, 101, Zero, Yun, Lilypad, Nano, MKR Zero). https://www.arduino.cc/*
- (No handwriting on this page.)

### p12 Arduino Uno
*Slide: Arduino Uno features: reset button, USB port, USB-Serial interface controller, power supply circuit, power supply jack, digital I/O pins, Tx and Rx pins, LED connected to digital pin 13 (PB5), power indicator, Tx and Rx indicators, 16 MHz resonator, microcontroller, power pins, analog input pins.*
- `~` symbol: PWM supported pins.
- Tx = Transmit, Rx = Receive (data).
- USB port: data communication. USB-Serial interface controller: translates serial to USB.
- Power supply circuit: 5 V. Power supply jack: < 12 V.
- Tx and Rx used to communicate with another board: Board 1 Tx connects to Board 2 Rx, and Board 1 Rx connects to Board 2 Tx (crossed).
- Sensors / actuators are not connected to Tx/Rx pins because it will interfere with data communication.

---

# 03. I/O Port Programming

### p13 I/O ports and registers
*Slide: I/O Ports: used to get the state of the physical world via sensors; also used to drive actuators and thereby change the state of the physical world. Slide: I/O Registers: registers associated with an I/O port. Data Direction Register (DDR): determines data direction; set to configure port pins as outputs; cleared to configure port pins as inputs. Port Output Register (PORT): used to specify the state (logic) of port pins.*
- Inputs: to connect sensors. Outputs: to connect actuators.
- Data in = input, data out = output. To configure this, DDR is used.
- Diagram: port bits 7 to 0 shown as a PORT register, below it the DDR register (example DDR with bit 0 = 1 meaning output pin, bit 6 = 0 meaning input pin).
- If PORT register becomes 1 -> high; 0 -> low.

### p14 DDR and PORT registers
*Slide: DDRx = 11110000, PORTx = 10100000, four LEDs on the output pins through resistors (two lit).*
- DDR: 0 - input - clear; 1 - output - set.
- PORT: 1 - high - LED on; 0 - low - LED off.
- x because there can be many (a, b, c, ... x).

---

# 03. System 01: LED blinker (assembly)

### p15 Electricity, resistor, diode
*(Handwritten heading) System 01 - "blinker Asm".*
*Slide: Electricity. Current, voltage (water analogy, more or less voltage / current).*
- Same flow. Current flow: pressure up, voltage up. Electrons up -> current flow up.

*Slide: Resistor. Colour bands: band one (first digit), band two (second digit), band three (multiplier), band four (tolerance). Slide: Diode (anode to cathode, LED; flat edge on the body flange marks the cathode; resistor R = (Vs - VL) / IL).*
- Example written beside the colour code: 2.4 MΩ (red, yellow, green).
- Diode: anode -> cathode. Colour band indicates cathode.
- V = IR.

### p16 ATmega328P pinout, wiring
*Slide: ATmega328P I/O Ports (28 pin chip: PC6 reset; PD0 to PD7 are Arduino pins 0 to 7; PB0 to PB5 are Arduino pins 8 to 13; PC0 to PC5 are A0 to A5; ~ marks PWM pins 3, 5, 6, 9, 10, 11; pins 7 VCC, 8 GND, 22 GND, 21 AREF, 20 AVCC). Slide: Hardware wiring diagram (Arduino pin to LED to resistor to GND on a breadboard).*
- This diagram will be given for the exam.
- Breadboard: strips are connected vertically in the main area and horizontally along the power rails.

### p17 Firmware algorithm
- Switching on and off an LED with 1/2 second time intervals.
*Slide: Firmware algorithm "blinkerAsm": configure PB0 as an output -> make PB0 high -> delay() -> make PB0 low -> delay() -> loop back. Delay subroutine: START delay() -> run a loop for 500 ms -> RETURN delay().*
- LED connected to this pin. That pin is I/O. For this we are using output, therefore configure as output.
- Logic high, therefore 5 V. Pin voltage 5 V and 0 V: voltage difference, therefore current flows. Logic low, therefore 0 V, pin voltage = GND.
- Subroutine symbol (delay is a function). "1/2 a second LED on" after the first delay; "1/2 second LED off" after the second.
- To explain the subroutine we need another flowchart. Without doing anything consume clock cycles for 500 ms (purpose of the loop).
- Since there is no OS, we can only do line by line execution. Since there is no control (control fall out) we run the code again to prevent it. Therefore having an **endless loop is a must**.

### p18 Configuring and driving a pin
*Slide: Configuring an I/O pin: `SBI DDRB, 0 ; set bit 0 of DDRB & configure PB0 as an output`. Making an I/O pin high: `SBI PORTB, 0 ; set bit 0 of PORTB & turn on LED`.*
- SBI = Set Bit I(n I/O register). "Start of comment" is marked at the `;`.
- `SBI DDRB, 0`: bits set to 0 indicate input pins; therefore pin 0 is configured to output.
- `SBI PortB, 0`: Port register bit 0 is set to 1; therefore the voltage at the pin becomes 5 V.

### p19 Delay calculation (single loop)
*Slide: Delaying. Engage CPU by running a loop and delay half a second. (1) Clock cycle time t = 1/f = 1/(16 x 10^6 Hz) = 62.5 x 10^-9 s. (2) Clock cycles for 0.5 s: n = d/t = 0.5 / (62.5 x 10^-9) = 8 x 10^6. (3) Cycles for one loop: `LDI R18, 255; LOOP3: DEC R18; BRNE LOOP3`; n3 = (1 + 2) x (255 - 1) + (1 + 1) x 1 = 764 clock cycles.*
- (1) Cycle time = 1/frequency = 1/(16 x 10^6 Hz) = 62.5 x 10^-9 s (nano seconds). (16 MHz.)
- (2) No. of clock cycles = delay / time for 1 clock cycle = 0.5 / (62.5 x 10^-9) = 8 x 10^6 clock cycles. If the CPU is engaged for this amount of clock cycles, we can obtain a 0.5 s delay.
- Why 255? Because of the 8 bit word size.
- "BRNE: branch if result is not 0" refers to the outcome of the previous instruction.
- **LDI**: Load Immediate (consumes 1 clock cycle). **DEC**: Decrement (1 clock cycle). **BRNE**: Branch if not equal (2 clock cycles when the branch is taken; 1 when it falls through).

### p20 Nested loops
*Slide: Delaying with nested loops (two loops): `LDI R17,255 / LOOP2: LDI R18,255 / LOOP3: DEC R18; BRNE LOOP3; DEC R17; BRNE LOOP2`; n2 = (1 + n3 + 1 + 2) x 254 + (1 + n3 + 1 + 1) x 1 = (1 + 764 + 1 + 2) x 254 + (1 + 764 + 1 + 1) x 1 = 195839 cycles. Three nested loops: `LDI R16,41 / LOOP1: ...`; n1 = (1 + n2 + 1 + 2) x (41 - 1) + (1 + n2 + 1 + 1) x 1 = 8029562 cycles.*
- Number of outer loops needed = total clock cycles needed / clock cycles consumed by n2 = 8 x 10^6 / 195839 = 40.8, approx. 41 (take the larger / greater value).

### p21 Delay calculation (result) and the NOP trick
*Slide: Delay calculation: n = 1 for LDI + n1 = 1 + 8029562 = 8029563 clock cycles; d = t x n = 62.5 x 10^-9 x 8029563 = 0.501847625, approx. 0.5 s.*
- d = t x n (time x no. of clock cycles).
- Peer's exact version: `LDI R16, 72` / `LOOP1: LDI R17, 188` / `LOOP2: LDI R18, 196` / `LOOP3: DEC R18; BRNE LOOP3; DEC R17; BRNE LOOP2; DEC R16; BRNE LOOP1` followed by 8 NOP instructions.
  - n3 = 587, n2 = 111,107, n1 = 7,999,991 (the page shows "799,991"; the correct value is 7,999,991), n = 7,999,992.
  - Only missing 8 clock cycles to get exactly 0.5 s, therefore run 8 NOP (1 cc per NOP, without doing anything) to reach 8 million.

### p22 Calling a subroutine
*Slide: Calling a subroutine: `CALL DELAY`; `DELAY: LDI R16, 41 ... RET`. Making an I/O pin low: `CBI PORTB, 0 ; clear bit 0 of PORTB & turn off LED`.*
- The subroutine consumes the small loops and then returns.
- PORTB bit 0 goes from 1 to 0 with CBI.

### p23 Indefinite tasks, bitwise operators
*Slide: Performing tasks indefinitely: `START: SBI PORTB,0 / CALL DELAY / CBI PORTB,0 / CALL DELAY / JMP START` (infinite loop).*
- Hardware error -> replace components. Software error -> debug the code.
- **Bitwise logical operators:**
  - Set bit: `PORTB = PORTB | 00000001` (bitwise OR). xxxx xxxx | 0000 0001 = xxxx xxx1. Using this only the interested value will be changed.
  - Clear bit: `PORTB = PORTB & 11111110`. xxxx xxxx & 1111 1110 = xxxx xxx0.

---

# Code examples written by hand (5 LED blinker)

### p24 Arduino code: 5 LED blinker
```c
int ledPin[] = {9, 10, 11, 12, 13};

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(ledPin[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPin[i], HIGH);
    delay(500);
    digitalWrite(ledPin[i], LOW);
  }
}
```
(Transcribed as written; the closing brace of `setup` and the second brace layout were incomplete on the page and are completed here.)

### p25 C code: 5 LED blinker
```c
#include <avr/io.h>
#define F_CPU 16000000UL
#include <util/delay.h>

int main() {
  arr[] = {1, 2, 3, 4, 5};
  for (int i = 0, i < 5, i++) {
    DDRB |= (1 << i);
  }
  while (1)
  {
    for (int i = 0; i < 5; i++)
    {
      PORTB |= (1 << arr[i]);
      _delay_ms(500);
      PORTB &= ~(1 << arr[i]);
    }
  }
  return 0;
}
```
**Errors in the peer's version (fixed in the lesson):** the array needs a type (`int arr[]`), the first `for` has commas instead of semicolons, and the data direction loop sets DDRB bits 0 to 4 while the blink loop drives bits 1 to 5 (so PB5 is never configured as an output). Use the same index set in both places (for example `DDRB |= (1 << arr[i])`). `return 0` is unreachable after `while(1)`.

### p26 C code: 5 LED blinker, Knight Rider
The page is a copy of p25 (the same code, headed "Knight Rider"); the return sweep was not written here, see p27 for the Arduino version of the idea.

### p27 Arduino code: 5 LED blinker, Knight Rider
```c
int ledPin[] = {9, 10, 11, 12, 13};

void setup() {
  for (int i = 0; i < 5; i++) {
    pinMode(ledPin[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPin[i], HIGH);
    delay(500);
    digitalWrite(ledPin[i], LOW);
  }
  for (int i = 3; i > 0; i--) {
    digitalWrite(ledPin[i], HIGH
    // (the page stops here)
```
The return sweep is the idea: go forward over LEDs 0 to 4 and then back over LEDs 3 to 1, so the end LEDs are not repeated. Completed in the lesson.

---

# 04. Polling and Interrupt Handling (30/07/2026)

### p28 Polling, System 5 (polling based trigger)
*Slide: Polling and Interrupt. Two approaches to perform more than one task seemingly at the same time. Used to provide CPU's service to the peripheral devices when CPU is busy with another task. Slide: Polling. CPU keeps on checking status of peripheral devices at regular intervals repeatedly while performing another task; when the status condition of a device is met, CPU provides its service and then resumes the task; CPU then starts again monitoring the status of devices.*
- How to perform a task while another task is in process (multiple tasks).
- Polling: periodically check if the peripheral device requires any services. If required provide service, otherwise continue current task.
- **System 5: Polling Based Trigger** (toggles an LED on user input while blinking an LED every 2 seconds using polling).
*Slide: Hardware. Schematic with ATmega328P: 10 kΩ reset pull-up, a push button on PD2 to ground, 16 MHz crystal, LED with 220 Ω on PB5 and LED with 1 kΩ on PB0. Wiring diagram: blinking LED and toggle LED on a breadboard with a push button.*
- Labels: PB5 LED = "Blink every 2 s"; PB0 LED = "user input LED"; the push button on PD2 = "user input". (Wiring labels "Blinking LED" and "Toggle LED".)
- The pin connected 2 (PD2) must always be high. If there is a user input it will be low.

### p29 Firmware and C program (polling)
*Slide: Firmware algorithm: main(): configure PB0 and PB5 as outputs -> configure PD2 as an input -> pull-up PD2 -> while(1): toggle PB5 -> wait for 2000 ms -> if PD2 is low then toggle PB0 -> (loop). Slide: C program `pollingBasedTriggerC.c`:*
```c
#include <avr/io.h>
#define F_CPU 16000000UL      // define CPU clock speed for delay.h
#include <util/delay.h>

int main(void)
{
    DDRB = DDRB | 0b00100001;   // configure PB0 & PB5 as outputs
    DDRD = DDRD & 0b11111011;   // configure PD2 as an input
    PORTD = PORTD | 0b00000100; // pull-up PD2
    while (1)
    {
        PORTB = PORTB ^ 0b00100000;   // toggle state of PB5
        _delay_ms(2000);              // delay 2000ms
        if ((PIND & 0b00000100) == 0) // if state of PD2 is low
            PORTB = PORTB ^ 0b00000001; // toggle state of PB0
    }
    return 0;
}
```
- Make the default state high (pull-up to 5 V).
- Main task (toggle on-board LED every 2 s). Peripheral check = the `if` on PD2.

### p30 Reading an input bit, polling problems
- `if ((PIND & 00000100) == 0)`: xxxx xxxx & 0000 0100 -> `if (0000 0x00 == 0)`.
- default: 0000 0100 == 0 (false). Press button: 0000 0000 == 0 (true).
- `PORTB = PORTB ^ 00000001` (XOR with 1 flips the bit): xxxx xxxx ^ 0000 0001 = xxxx xxx(x-bar).
- If the input is given using a quick pulse the input will not be detected. That is because for the input to be detected, the input should be received during the delay time that the CPU is checking the peripheral device. If the input actuator is a sensor, there might be multiple undetected inputs due to this. This is the issue of polling.
*Slide: Polling problems: if the state of a device changes too fast or the CPU's monitoring interval is too long, the state change may go undetected; no support for the concept of priority as CPU repeatedly performs all tasks in the same order.*
- Cannot prioritize if there are multiple devices.

### p31 digitalRead, interrupts
- `digitalRead` -> gives the current state of the pin (high / low).
- ex: `digitalWrite(2, !digitalRead(2));` Write the state of pin 2 to be the opposite of the current state of pin 2.
*Slide: Interrupt. Peripheral devices interrupt the CPU when they need CPU's service while CPU is busy with another task; CPU suspends the currently performing task and provides its service to the interrupted device; CPU then resumes the task it was doing; frees CPU from monitoring (polling) the state of peripheral devices; supports the concept of priority.*
*Slide: Interrupt Handling, steps 1 to 3 (an interrupt arrives -> jump to the Interrupt Vector Table address, the return address is pushed on the STACK -> ISR runs -> return address popped, program resumes).*
- Interrupt Vector Table: contains addresses of interrupt service routines.

### p32 Interrupt vector table and the flag pattern
- Every interrupt has an interrupt service routine (ISR).
*Slide: Widely used interrupt vectors (address / interrupt / vector name):* 0x0002 External interrupt on INT0 pin INT0_vect; 0x0004 INT1 pin INT1_vect; 0x0006 pin change on Port B PCINT0_vect; 0x0008 pin change Port C PCINT1_vect; 0x000A pin change Port D PCINT2_vect; 0x0012 Timer/Counter 2 overflow TIMER2_OVF_vect; 0x001A Timer/Counter 1 overflow TIMER1_OVF_vect; 0x0020 Timer/Counter 0 overflow TIMER0_OVF_vect; 0x0024 USART receive complete USART_RX_vect; 0x0028 USART transmit complete USART_TX_vect; 0x002A ADC conversion complete ADC_vect.
- Lower the address, higher the priority.
- Flag pattern (main loop reacts to a variable that the ISR sets):
```c
int flag = 0;
int main() {
  while (1) {
    if (flag == 0)
      // do something
    else
      // do something else
  }
  return 0;
}

ISR(INT0_vect)
{
  flag = 1;
}
```

### p33 Interrupt registers
- Set interrupt -> `sei()`; Clear interrupt -> `cli()` (both from the `interrupt.h` register).
*Slide: Interrupt registers block diagram: the External Interrupt Control Register (ISC bits of EICRA) selects low level / logic change / falling edge / rising edge for INTn; EIMSK (INTn bit), PCMSKn (PCINTm), PCICR (PCIEn bit), TIMSK (TOIE), ADCSRA (ADIE) and UCSR (TXCIE, RXCIE) enable individual sources; the sources feed an OR gate -> the global interrupt enable bit I of SREG -> CPU.*
- External interrupt pins: INT pins.

---

# 05. Analog to Digital Conversion (1 class missed by the peer)

### p34 ADC reference voltage
*Slide: ADC reference voltage. ADC converts any analog input voltage between 0 and Vref to a number of discrete voltage intervals between 0 and 2^resolution - 1. Resolution is the number of bits used for ADC. Total number of intervals = 2^resolution. Interval size = Vref / 2^resolution. Analog voltage = number of intervals x interval size, Vin = ADCW x Vref / 2^resolution. Interval size is the smallest change in analog input voltage that ADC can distinguish.*
- Vin -> [ADC] -> discrete number. Vin is between 0 and Vref; the discrete number is between 0 and (2^resolution - 1).
- For our MC, operating voltage is 5 V, therefore default Vref = 5 V, therefore resolution = 10 bit.
- Therefore for our MC: Vin (0 to 5 V) -> ADC -> discrete number (n) from 0 to (2^10 - 1), i.e. 0 to 1023.
- Number line drawn: 0 V ... Vref with points 0, 1, 2, 3, ... 1020, 1021, 1022, 1023 and the gap between neighbouring points marked ΔV.
- **No. of points (not gaps)**: total number of intervals = 2^10 = 1024.
- Interval size = (Vref - 0) / total intervals = 5 / 1024 (default voltage for Vref = 5 V).
- Vin = ΔV x n (n = discrete number).

### p35 ADC value to voltage range, reducing the interval
- As written by the peer (first row appears to be a slip: the first interval corresponds to ADC = 0 with the standard floor convention):
  - ADC = 1: 0 <= Vin < ΔV
  - ADC = 2: ΔV <= Vin < 2ΔV
  - ADC = 1023: 1022ΔV <= Vin < 1023ΔV
- The smaller the range, the more accurate the voltage ADC gives. Therefore we must try to reduce the intervals (ΔV): (1) increase resolution; (2) if resolution is fixed, reduce Vref.
- Vin -> [ADC] -> ADCW. Examples: 0 to 5 V uses Vref = 5 V (default); 0 to 1 V uses Vref = 1.1 V (internal); 0 to 2.5 V uses Vref = 2.5 V (externally).
*Slide: ADC registers. ADMUX (ADC Multiplexer selection) register: bits REFS1, REFS0, ADLAR, (bit 4 unused), (bit 3 n/a), MUX2, MUX1, MUX0. REFS1 and REFS0 set Vref and thereby the interval size of the ADC. In Arduino, use `analogReference(type)`. REFS1 REFS0 = 00: Vref supplied externally at AREF (EXTERNAL); 01: AVcc internally (DEFAULT); 10: reserved; 11: 1.1 V internally (INTERNAL).*
- `analogReference(type)`: call in the setup once is enough.

### p36 ADMUX continued
*Slide: ADLAR (ADC Left Adjust Result) bit specifies whether the conversion result is left justified (ADLAR = 0: right justified, result in ADCH bits 1 to 0 and ADCL bits 7 to 0; ADLAR = 1: left justified, result in ADCH 7 to 0 and ADCL bits 7 to 6). MUX2, MUX1, MUX0 select the analog input channel: 000 = ADC0, 001 = ADC1, 010 = ADC2, 011 = ADC3, 100 = ADC4, 101 = ADC5.*
- (No handwriting on this page.)

### p37 Voltmeter C program
*Slide: C program `voltMeterC.c` (5-LED bar-graph voltmeter on PB0 to PB4, input on PC0 = ADC0):*
```c
#include <avr/io.h>                                   // include I/O definitions
int main(void)
{
    DDRB = DDRB | 0b00011111;                         // configure PB0 to PB4 as outputs
    DDRC = DDRC & 0b11111110;                         // configure PC0 (ADC0) as an input
    ADMUX = (ADMUX & 0b01111111) | 0b01000000;        // set Vref to AVcc (5V)
    ADMUX = ADMUX & 0b11111000;                       // multiplex PC0 as analog input channel (ADC0)
    ADCSRA = ADCSRA | 0b00000111;                     // set ADC clock speed to F_CPU/128
    ADCSRA = ADCSRA | 0b10000000;                     // enable ADC
    while (1)
    {
        ADCSRA = ADCSRA | 0b01000000;                 // start ADC
        while (ADCSRA & 0b01000000);                  // poll till ADC is over
        float vIn = ADCW * 5.0 / 1024;                // compute analog input voltage
        PORTB = PORTB & 0b11100000;                   // set PB0 to PB4 low & turn off LEDs
        if (vIn > 4)      PORTB = PORTB | 0b00011111; // > 4 V: 5 LEDs on
        else if (vIn > 3) PORTB = PORTB | 0b00001111; // > 3 V: 4 LEDs
        else if (vIn > 2) PORTB = PORTB | 0b00000111; // > 2 V: 3 LEDs
        else if (vIn > 1) PORTB = PORTB | 0b00000011; // > 1 V: 2 LEDs
        else if (vIn > 0) PORTB = PORTB | 0b00000001; // > 0 V: 1 LED
    }
    return 0;
}
```
- At least one operand must be floating point (so `5.0 / 1024` does not become integer division).

---

# 06. Transducers

### p38 Transducers
*Slide: Transducer: converts energy from one form to another; used at the boundary of an embedded system; categorized by the direction of conversation: sensors, actuators.*
- PIR = Pyro-electric InfraRed (sensor).

---

# 07. Timing and Counting

### p39 Timer and counter
*Slide: Timer. Increments on each clock pulse when the oscillator is connected; as frequency is known, using the pulse count, time elapsed can be determined; operates as a Counter when an external pulse source is connected (used to count events). What is the need?*
- Timer is connected to a switch and the timer is reset each time the button is pressed. Then the timer acts as a counter (generates pulses).
- When an oscillator is connected to the timer, we can find elapsed time.
- Why do we need this? The same thing can be done using software. If software is used for timing and counting, it ties up the CPU. In MCs we have a very small CPU, so this is a huge burden. Therefore we leave the CPU for computational works and use timers (which is an external peripheral device) for this purpose.
*Slide: Timing and counting: how an 8-bit timer works (oscillator -> clock select CS bits of TCCRn -> TCNTn register (0 to 255) -> TOV bit of TIFRn; a T_n pin with a sensor for counting external events).*
- Oscillator is connected to Timer. At each clock pulse the timer increments.
- Increments happen 0 to 255. Then it overflows and goes back to 0.
- TIFR = Timer Interrupt Flag Register. TOV = Timer Overflow Bit. When the timer overflows the TOV bit is set. This tells the CPU that the timer overflowed.

### p40 Determining elapsed time
*Slide: Determining elapsed time. TCNT register counts from Number A (start) to Number B (stop) with +1 per pulse. Elapsed time = (B - A) / f. With a prescaler (1/N) between the oscillator and the timer: Elapsed time = N x (B - A) / f.*
- TOV: set it to clear. **W1C: Write One to Clear** (you clear the TOV flag by writing a 1 to it).

---

# What the peer notes cover and what is missing

| Lecture | Peer notes | Gap that the study guides fill from slides |
|---|---|---|
| 01 Introduction | Complete | few definitions (requirements, architectures, co-design, ...) |
| 02 Microcontrollers | Complete | Harvard vs von Neumann, RISC/CISC, memory map details |
| 03 I/O port programming | Complete, with the blinker | PIN register input, button reading, exercises 1 and 2, instruction set |
| 04 Polling and interrupts | Complete to the interrupt registers | EICRA/EIMSK values, ISR with the button example, exercise 3 |
| 05 ADC | Partial (reference voltage, ADMUX, voltmeter C) | ADCSRA bits, prescaler, Arduino `analogRead`, LM35/LDR, exercise 4 |
| 06 Transducers | One page | sensors/actuators, transistor/MOSFET/diode driver circuits, datasheets |
| 07 Timing and counting | First 2 pages | Timer0/1/2 registers, prescalers, overflow and CTC mode, exercise 5 |
| 08 PWM | Missing | full lecture |
| 09 Serial communication | Missing | full lecture |
