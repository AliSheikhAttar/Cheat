# I2C Protocol

- Description
I2C (Inter-Integrated Circuit) is a multi-master, multi-slave, synchronous serial communication protocol. It uses two lines: SDA (data) and SCL (clock) for communication between devices.

- Example Scenario
Read temperature data from a common I2C temperature sensor (e.g., TMP102).

- Code Example
```cpp
#include <Wire.h>

// TMP102 I2C address
const int TMP102_ADDR = 0x48;

void setup() {
  Serial.begin(9600);
  Wire.begin(); // Join I2C bus as master
}

void loop() {
  Wire.beginTransmission(TMP102_ADDR);
  Wire.write(0x00); // Point to temperature register
  Wire.endTransmission(false); // Restart for repeated start

  Wire.requestFrom(TMP102_ADDR, 2); // Request 2 bytes

  if (Wire.available() == 2) {
    int raw = (Wire.read() << 4) | (Wire.read() >> 4);
    float temperature = raw * 0.0625; // Convert to Celsius
    Serial.print("Temperature: ");
    Serial.print(temperature);
    Serial.println(" C");
  }

  delay(1000); // Wait 1 second before next reading
}
```
- Explanation
Libraries: Uses Wire.h for I2C communication.
TMP102_ADDR: I2C address of the TMP102 temperature sensor (commonly 0x48).
Wire.beginTransmission(): Starts communication with the TMP102.
Wire.write(0x00): Selects the temperature register.
Wire.requestFrom(): Requests 2 bytes of temperature data.
Data Conversion: Combines the two bytes and converts the raw data to Celsius.
Output: Prints the temperature to the Serial Monitor every second.
