// Test 09: DC motor driven through a BC547 with PWM speed control on pin 9.
// Part 1 is on/off, part 2 ramps the speed up and down smoothly.

const int MOTOR_PIN = 9;    // pin 9 supports PWM (marked ~)

void setup() {
  pinMode(MOTOR_PIN, OUTPUT);
}

void loop() {
  // Part 1: full on, full off
  digitalWrite(MOTOR_PIN, HIGH);
  delay(1500);
  digitalWrite(MOTOR_PIN, LOW);
  delay(1500);

  // Part 2: speed up, then slow down (duty cycle 0..255)
  for (int duty = 0; duty <= 255; duty++) {
    analogWrite(MOTOR_PIN, duty);
    delay(10);
  }
  for (int duty = 255; duty >= 0; duty--) {
    analogWrite(MOTOR_PIN, duty);
    delay(10);
  }
}
