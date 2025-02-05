# Nested condition

- ternary
```cpp
if (a)
    c = someValue;
else
    c = anotherValue;

// Using the ternary operator
c = (a) ? someValue : anotherValue;
```

- ternary abuse
```cpp
c = a ? b : d ? e : f;
```

- simplify true/false
```cpp
if(a)
    b = true;
else 
    b = false

//
b = a;
```

```cpp
if (customer.TotalOrders > 50)
    isGoldCustomer = true;
else
    isGoldCustomer = false;

// Simplified version
isGoldCustomer = customer.TotalOrders > 50;
```

- combine
```cpp
if(a){
    if(b){
        statement
    }
}
// combine
if (a && b){
    statement
}
```

- Early exit
```cpp
if(a){
    if(b){
        statement
    }
}
// Early exit
if(!a)
    return;
if(!b)
    return;
statement

// Early exit + combine
if(!a || !b)
    return;
statement
```

- Swap orders
```cpp
// Original order
if (a) {
    if (b) {
        isValid = true;
    }
}
if (c) {
    if (b) {
        isValid = true;
    }
}

// Swapped order
if (b) {
    if (a) {
        isValid = true;
    }
    if (c) {
        isValid = true;
    }
}

// Combined condition
if (b && (a || c)) {
    isValid = true;
}

// simplify
isValid = (b && (a || c));
```