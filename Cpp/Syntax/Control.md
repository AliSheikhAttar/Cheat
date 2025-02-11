# Control and Loop statements

- for
```cpp
//enumerating 
vector<int> numbers;
for(auto x: numbers){ }
for(int i=0;i<numbers.size();i++){}
for(int i=0;i<numbers.size();++i){}

// infinite
for(;;){}
```

- Assertion
```cpp
#include <cassert>
int x = 10;
assert(x > 0); // Assertion that x is greater than 0
// if fails throw runtime error
```