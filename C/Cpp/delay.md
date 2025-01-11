# Delay / Sleep


```cpp
#include <chrono>
#include <thread>

int main() {
    using namespace std::this_thread; // sleep_for, sleep_until
    using namespace std::chrono; // nanoseconds, system_clock, seconds

    sleep_for(nanoseconds(10));
    sleep_until(system_clock::now() + seconds(1));
}
```
 
- In Win32:
```cpp
#include<windows.h>
Sleep(milliseconds);
```

- In Unix:
```cpp
#include<unistd.h>
unsigned int microsecond = 1000000;
usleep(3 * microsecond);//sleeps for 3 second
```