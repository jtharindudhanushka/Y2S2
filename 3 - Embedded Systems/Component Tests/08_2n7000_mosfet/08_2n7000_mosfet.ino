// Test 08: 2N7000 N-channel MOSFET used as a switch.
// Pin 9 drives the gate; the MOSFET switches the LED on and off.

const int GATE_PIN = 9;

void setup() {
  pinMode(GATE_PIN, OUTPUT);
}

void loop() {
  digitalWrite(GATE_PIN, HIGH);   // gate high (5 V): channel on, LED lit
  delay(500);
  digitalWrite(GATE_PIN, LOW);    // gate low: channel off, LED dark
  delay(500);
}
