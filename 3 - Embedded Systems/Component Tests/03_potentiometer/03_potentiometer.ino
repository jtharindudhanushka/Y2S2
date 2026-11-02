// Test 03: potentiometer on A0. Prints the raw ADC number (0-1023) and the voltage.

void setup() {
  Serial.begin(9600);
}

void loop() {
  int adc = analogRead(A0);
  float volts = adc * 5.0 / 1024;   // Vref = 5 V, interval = 5/1024
  Serial.print("ADC = ");
  Serial.print(adc);
  Serial.print("   Vin = ");
  Serial.print(volts);
  Serial.println(" V");
  delay(200);
}
