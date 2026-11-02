// Test 05: LM35 temperature sensor on A0. Output is 10 mV per degree C.

void setup() {
  Serial.begin(9600);
}

void loop() {
  int adc = analogRead(A0);
  float volts = adc * 5.0 / 1024;
  float tempC = volts * 100;        // 10 mV/C  ->  V x 100
  Serial.print("ADC = ");
  Serial.print(adc);
  Serial.print("   ");
  Serial.print(tempC);
  Serial.println(" C");
  delay(500);
}
