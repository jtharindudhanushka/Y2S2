// Test 00: board, upload and USB serial link.
// Blinks the on-board LED (pin 13 = PB5) and prints "hello" to the Serial Monitor.

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  Serial.println("hello - LED on");
  delay(500);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.println("hello - LED off");
  delay(500);
}
