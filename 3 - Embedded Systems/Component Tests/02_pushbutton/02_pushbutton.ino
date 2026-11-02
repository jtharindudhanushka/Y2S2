// Test 02: pushbutton with the internal pull-up.
// Released = 1 (HIGH), pressed = 0 (LOW). The on-board LED (pin 13) lights while pressed.

const int BTN_PIN = 2;

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);   // PORT bit set on an input = pull-up on
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  int state = digitalRead(BTN_PIN);
  digitalWrite(LED_BUILTIN, !state);
  Serial.println(state);
  delay(100);
}
