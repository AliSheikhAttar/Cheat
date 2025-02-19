# Errors


dont compare negative long long number to int number, cast the int to long long
```cpp
(n - sum) <= static_cast<long long>(summands.size())
```