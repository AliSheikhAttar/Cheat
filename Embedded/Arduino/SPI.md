# SPI Protocol

- Description
SPI (Serial Peripheral Interface) is a synchronous serial communication protocol used to communicate with peripherals like sensors, SD cards, and displays. It involves a master device and one or more slave devices.

- Example Scenario
Communicate with an SPI-based SD card module to initialize and read data.

- Code Example
```cpp
#include <SPI.h>
#include <SD.h>

// Constants
const int chipSelect = 10; // SD card CS pin

void setup() {
  Serial.begin(9600);
  while (!Serial) { ; }

  // Initialize SPI bus and SD card
  if (!SD.begin(chipSelect)) {
    Serial.println("SD initialization failed!");
    while (1);
  }
  Serial.println("SD initialization done.");

  // Open a file and write data
  File dataFile = SD.open("example.txt", FILE_WRITE);
  if (dataFile) {
    dataFile.println("Hello, SPI!");
    dataFile.close();
    Serial.println("Data written to example.txt");
  } else {
    Serial.println("Error opening example.txt");
  }
}

void loop() {
  // Nothing needed here
}
```

- Explanation
Libraries: Includes SPI.h for SPI communication and SD.h for SD card functions.
chipSelect: Pin 10 is commonly used as the CS (Chip Select) for the SD card.
SD.begin(): Initializes the SD card. If successful, proceeds to write data.
File Operations: Opens (or creates) example.txt on the SD card and writes a line of text.