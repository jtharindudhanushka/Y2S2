// Test 07: BC547 NPN transistor used as a switch.
// Pin 9 drives the base through 1k; the transistor switches the LED on and off.

const int BASE_PIN = 9;

void setup() {
  pinMode(BASE_PIN, OUTPUT);
}

void loop() {
  digitalWrite(BASE_PIN, HIGH);   // base current flows: transistor on, LED lit
  delay(500);
  digitalWrite(BASE_PIN, LOW);    // no base current: transistor off, LED dark
  delay(500);
}
