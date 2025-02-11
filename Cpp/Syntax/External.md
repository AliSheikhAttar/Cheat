# External to real world

## time
- measuring time
```cpp
#include <chrono>
auto start = std::chrono::high_resolution_clock::now();

// Your code to be timed goes here...

auto end = std::chrono::high_resolution_clock::now();

auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start); 
// Or nanoseconds, microseconds, seconds, etc.

std::cout << "Time taken: " << duration.count() << " milliseconds" << std::endl;
```