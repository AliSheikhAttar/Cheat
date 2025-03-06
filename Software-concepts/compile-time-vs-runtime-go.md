Let’s dive into the difference between **compile time** and **runtime**, and then illustrate it with examples in Go.

### Definitions

- **Compile Time**: This is the phase when your source code is translated into machine code or an executable by the compiler. During this stage, the compiler performs tasks like checking for syntax errors, ensuring types match (type checking), and other static analyses. Think of it as the preparation step before your program can run.

- **Runtime**: This is when the compiled program actually executes. It’s the phase where the code interacts with the system—using memory, processing input/output, or performing calculations. Errors that occur here are only detectable when the program is running.

In Go, a statically typed language, many checks happen at compile time, but the execution and dynamic behaviors occur at runtime. Let’s explore this with examples.

---

### Examples in Go

#### 1. Compile-Time Error: Syntax Error
Consider this Go code:

```go
package main

func main() {
    fmt.Println("Hello, World!" // Missing closing parenthesis
}
```

If you try to compile this (e.g., with `go build`), the compiler will catch the syntax error:

```
./main.go:4:28: syntax error: unexpected newline, expecting )
```

This error is detected at **compile time** because it’s a structural issue in the code. The program won’t even generate an executable until you fix it.

---

#### 2. Compile-Time Error: Type Checking
Go enforces type safety at compile time. Here’s an example:

```go
package main

func main() {
    var x int = "hello" // Trying to assign a string to an int
}
```

When you compile this, you’ll get:

```
./main.go:4:7: cannot use "hello" (type string) as type int in assignment
```

This is a **compile-time error** because the type mismatch is caught before the program runs.

---

#### 3. Runtime Error: Division by Zero
Now, let’s look at something that compiles fine but fails when executed:

```go
package main

import "fmt"

func main() {
    a := 10
    b := 0
    c := a / b // Division by zero
    fmt.Println(c)
}
```

This code compiles successfully—no syntax or type issues—but when you run it (`go run main.go`), it crashes:

```
panic: runtime error: integer divide by zero
goroutine 1 [running]:
main.main()
    /path/to/main.go:7 +0x52
```

This is a **runtime error** because the division by zero only occurs during execution.

---

#### 4. Compile Time: Constant Evaluation
In Go, constants are evaluated at compile time:

```go
package main

import "fmt"

const a = 10
const b = a * 2 // Calculated at compile time

func main() {
    fmt.Println(b) // Outputs: 20
}
```

Here, `b` is computed as `20` during compilation. The compiler resolves this before the program runs, making it a **compile-time** operation.

Contrast this with variables:

```go
package main

import "fmt"

func main() {
    a := 10
    b := a * 2 // Calculated at runtime
    fmt.Println(b) // Outputs: 20
}
```

For variables, the multiplication happens at **runtime** when the code executes.

---

#### 5. Compile Time vs. Runtime: Arrays and Slices
- **Array Length (Compile Time)**:

```go
package main

func main() {
    var arr [5]int // Length 5 is fixed at compile time
}
```

The size of an array is part of its type and must be known at compile time. If you tried `[a]int` where `a` is a variable, the compiler would reject it.

- **Slice Length (Runtime)**:

```go
package main

import "fmt"

func main() {
    s := make([]int, 5)
    fmt.Println(len(s)) // Outputs: 5

    s = append(s, 1)
    fmt.Println(len(s)) // Outputs: 6
}
```

Slices are dynamic, and their length can change at **runtime** with operations like `append`.

---

#### 6. Runtime: Interface Method Dispatch
Go’s interfaces allow behavior to be determined at runtime:

```go
package main

import "fmt"

type Speaker interface {
    Speak() string
}

type Dog struct{}
func (d Dog) Speak() string { return "Woof!" }

type Cat struct{}
func (c Cat) Speak() string { return "Meow!" }

func main() {
    var s Speaker
    s = Dog{}
    fmt.Println(s.Speak()) // Outputs: Woof!

    s = Cat{}
    fmt.Println(s.Speak()) // Outputs: Meow!
}
```

The compiler ensures `Dog` and `Cat` implement the `Speaker` interface at compile time, but which `Speak` method is called depends on the object assigned to `s` at **runtime**.

---

### Summary
- **Compile Time**: Happens during compilation. Examples include syntax checking (e.g., missing parentheses), type checking (e.g., string vs. int), constant evaluation, and array size determination. Errors here prevent the program from running.
- **Runtime**: Happens during execution. Examples include division by zero, dynamic method calls via interfaces, slice length changes, and deferred function execution. Errors here occur while the program is running.

These examples in Go highlight how compile time prepares and validates the code, while runtime is where the action—and sometimes the chaos—happens!