# External Interrupt
- Description
attachInterrupt allows your Arduino to respond to external events (like a button press) by triggering an Interrupt Service Routine (ISR). This is useful for handling real-time events without constantly polling in the loop() function.

- Example Scenario
Toggle an LED when a button connected to pin 2 is pressed.

- Code Example
```cpp
// Constants
const int buttonPin = 2;    // Pin connected to the button (interrupt pin)
const int ledPin = 13;      // Built-in LED pin

volatile bool ledState = false; // Flag to toggle LED

void setup() {
  pinMode(buttonPin, INPUT_PULLUP); // Initialize button pin with pull-up resistor
  pinMode(ledPin, OUTPUT);          // Initialize LED pin as output
  // Attach interrupt to buttonPin, calling handleButtonPress on FALLING edge
  attachInterrupt(digitalPinToInterrupt(buttonPin), handleButtonPress, FALLING);
}

void loop() {
  // Update LED based on ledState
  digitalWrite(ledPin, ledState ? HIGH : LOW);
}

// Interrupt Service Routine (ISR)
void handleButtonPress() {
  ledState = !ledState; // Toggle LED state
}
```
- Explanation
buttonPin: Connected to a button that pulls the pin LOW when pressed.
ledPin: Built-in LED toggles its state each time the button is pressed.
attachInterrupt: Links the button press to the handleButtonPress ISR, triggered on the FALLING edge (button press).
ISR (handleButtonPress): Toggles the ledState flag, which updates the LED in the loop().


