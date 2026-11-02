// Test 04: LDR in a voltage divider on A0.
// Cover the LDR, then light it with a phone torch, and watch the number change.

void setup() {
  Serial.begin(9600);
}

void loop() {
  int adc = analogRead(A0);
  Serial.print("ADC = ");
  Serial.print(adc);
  Serial.print("   Vin = ");
  Serial.print(adc * 5.0 / 1024);
  Serial.println(" V");
  delay(300);
}
