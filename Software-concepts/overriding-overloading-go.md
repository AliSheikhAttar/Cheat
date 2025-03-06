### Definitions

- **Overloading**: This refers to defining multiple functions or methods with the **same name** but **different parameter lists** (e.g., different numbers or types of parameters). The correct function or method is chosen at compile time based on the arguments provided. Overloading is common in languages like Java or C++, but as we’ll see, Go handles this differently.

- **Overriding**: This occurs when a subtype (e.g., a subclass or, in Go, an embedding struct) provides a **new implementation** of a method that is already defined in its supertype (e.g., a parent class or embedded type). The subtype’s version replaces the inherited version when called on an instance of the subtype.

- **Overwriting?**: In programming, "overwriting" isn’t a standard term for functions or methods. It might imply redefining a function in the same scope (overwriting the old definition), but in Go, you can’t redefine a function with the same name in the same package—each function name must be unique. For methods, "overwriting" could be confused with overriding, which is more precise. In file systems, "overwriting" means replacing content, but that’s unrelated to functions or methods. Thus, I’ll treat "overwriting" as a likely typo for "overriding."

### Overloading and Overriding in Go

Go has a unique design compared to languages like Java or C++. It lacks traditional class-based inheritance and doesn’t support function or method overloading in the conventional sense. Let’s break this down:

#### Overloading in Go
Go **does not support overloading**. You cannot define multiple functions or methods with the same name but different parameter lists within the same package or on the same type. This is a deliberate design choice to keep the language simple and avoid ambiguity. For example:

```go
// This is invalid in Go
func Do(a int) {
    println(a)
}

func Do(a string) {  // Error: Do redeclared in this block
    println(a)
}
```

Similarly, for methods:

```go
type MyType struct{}

func (m MyType) Do(a int) {
    println(a)
}

func (m MyType) Do(a string) {  // Error: method Do redeclared for MyType
    println(a)
}
```

In Go, every function or method name must be **unique** within its scope (package for functions, type for methods). To achieve similar functionality to overloading, you’d typically use different function names (e.g., `DoInt` and `DoString`) or rely on variadic functions or interface types, though these are workarounds, not true overloading.

#### Overriding in Go
Go doesn’t have classical inheritance with classes, but it supports **embedding** of structs and interfaces, which allows a form of method overriding. When a struct embeds another struct (or a type with methods), the embedded type’s methods are promoted to the embedding struct. However, if the embedding struct defines a method with the same name, it **overrides** the embedded type’s method for instances of the embedding struct.

Here’s how it works:

- If a struct `Derived` embeds a struct `Base`, `Derived` inherits `Base`’s methods.
- If `Derived` defines a method with the same name as one in `Base`, `Derived`’s version takes precedence when called on a `Derived` instance.

### Example in Go

Since overloading isn’t possible in Go, I’ll focus the example on overriding, which is suitable and demonstrates the concept clearly:

```go
package main

import "fmt"

// Base struct with a method
type Base struct{}

func (b Base) Say() {
    fmt.Println("Base")
}

// Derived struct embedding Base
type Derived struct {
    Base // Embedding Base into Derived
}

// Derived overrides the Say method
func (d Derived) Say() {
    fmt.Println("Derived")
}

func main() {
    // Create an instance of Derived
    d := Derived{}

    // Call Say on Derived
    d.Say()        // Outputs: Derived (overridden method)

    // Access the Base method explicitly
    d.Base.Say()   // Outputs: Base (original method from embedded type)
}
```

#### Explanation
- **Embedding**: `Derived` embeds `Base`, so it inherits the `Say` method from `Base`.
- **Overriding**: `Derived` defines its own `Say` method, which overrides `Base`’s `Say` when called on a `Derived` instance (`d.Say()` prints "Derived").
- **Accessing the Original**: You can still call the embedded `Base`’s `Say` method using `d.Base.Say()`, showing that the original method isn’t lost—it’s just shadowed by the override.

If `Derived` didn’t define its own `Say` method, `d.Say()` would call `Base`’s `Say` and print "Base". This demonstrates how embedding and overriding work together in Go.

### Key Differences

| **Aspect**         | **Overloading**                          | **Overriding**                          |
|---------------------|------------------------------------------|-----------------------------------------|
| **Definition**      | Multiple functions/methods with the same name, different parameters | Redefining a method in a subtype to replace the supertype’s version |
| **Purpose**         | Provide flexibility for different argument types/numbers | Customize behavior in a subtype |
| **Supported in Go?**| No—names must be unique                 | Yes—via struct embedding               |
| **Scope**           | Same scope (e.g., package or type)       | Involves type hierarchy (embedding in Go) |
| **Example**         | Not possible in Go                      | `Derived` overrides `Base`’s `Say`     |

### Conclusion
- **Overloading**: Not supported in Go. You can’t have multiple `Do` methods or functions with different parameters under the same name.
- **Overriding**: Supported in Go through struct embedding. A struct can override methods of an embedded type by defining a method with the same name, as shown in the example.
