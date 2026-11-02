// Test 01: LED and 220 ohm resistor.
// Blinks the LED on pin 9. Repeat the test for each of your 10 LEDs and each resistor.

const int LED_PIN = 9;

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);
  delay(300);
  digitalWrite(LED_PIN, LOW);
  delay(300);
}
