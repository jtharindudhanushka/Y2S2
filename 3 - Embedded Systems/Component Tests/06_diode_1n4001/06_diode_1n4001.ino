// Test 06: 1N4001 diode. The LED is switched on/off from pin 9 so you can compare
// the diode facing both ways. The diode is what decides whether the LED lights.

const int OUT_PIN = 9;

void setup() {
  pinMode(OUT_PIN, OUTPUT);
}

void loop() {
  digitalWrite(OUT_PIN, HIGH);
  delay(500);
  digitalWrite(OUT_PIN, LOW);
  delay(500);
}
