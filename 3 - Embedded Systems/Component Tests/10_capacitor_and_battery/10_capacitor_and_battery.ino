// Test 10: debounce test for the 100 nF capacitor.
// Counts how many LOW readings (button presses) the Uno sees per physical press.
// Run it with the capacitor OUT of the circuit, then with it IN, and compare.

const int BTN_PIN = 2;
int lastState = HIGH;
unsigned long presses = 0;

void setup() {
  pinMode(BTN_PIN, INPUT_PULLUP);
  Serial.begin(9600);
  Serial.println("Press the button. Each line is one detected press.");
}

void loop() {
  int state = digitalRead(BTN_PIN);
  if (lastState == HIGH && state == LOW) {   // falling edge
    presses++;
    Serial.print("detected press #");
    Serial.println(presses);
  }
  lastState = state;
}
