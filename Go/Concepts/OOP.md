# OOP
Go does not strictly support object orientation but is a lightweight object Oriented language. Object Oriented Programming in Golang is different from that in other languages like C++ or Java due to factors mentioned below:

## Struct
Go does not support custom types through classes but structs. Structs in Golang are user-defined types that hold just the state and not the behavior. Structs can be used to represent a complex object comprising more than one key-value pairs. We can add functions to the struct that can add behavior to it as shown below:

Example:

```Go
// Golang program to illustrate the 
// concept of custom types 
package main 
  
import ( 
    "fmt"
) 
  
// declaring a struct 
type Book struct{ 
      
    // defining struct variables 
    name string 
    author string 
    pages int
} 
  
// function to print book details 
func (book Book) print_details(){ 
  
    fmt.Printf("Book %s was written by %s.", book.name, book.author) 
    fmt.Printf("\nIt contains %d pages.\n", book.pages) 
} 
  
// main function 
func main() { 
      
    // declaring a struct instance 
    book1 := Book{"Monster Blood", "R.L.Stine", 131} 
      
    // printing details of book1 
    book1.print_details() 
      
    // modifying book1 details 
    book1.name = "Vampire Breath"
    book1.pages = 162 
      
    // printing modified book1 
    book1.print_details() 
      
} 
```
Output:

Book Monster Blood was written by R.L.Stine.
It contains 131 pages.
Book Vampire Breath was written by R.L.Stine.
It contains 162 pages.

## Encapsulation
It means hiding sensitive data from users. In Go, encapsulation is implemented by capitalizing fields, methods, and functions which makes them public. When the structs, fields, or functions are made public, they are exported on a package level. Some examples of public and private members are:
```Go
package gfg

// this function is public as 
// it begins with a capital letter
func Print_this(){
        // implementation
}

// public struct
type Book struct{

        // public field
        Name string
        // private field, only
        // available in gfg package
        author string
}
```

## Inheritance
When a class acquires the properties of its superclass then we can say it is inheritance. Here, subclass/child class are the terms used for the class which acquire properties. For this one, one must use a struct to achieve inheritance in Golang. Here, users have to compose using structs to form the other objects.

## Interfaces
Interfaces are types that have multiple methods. Objects that implement all the methods of the interface automatically implement the interface, i.e., interfaces are satisfied implicitly. By treating objects of different types in a consistent way, as long as they stick to one interface, Golang implements polymorphism.

Example:


```Go

// Golang program to illustrate the 
// concept of interfaces 
package main 
  
import ( 
    "fmt"
) 
  
// defining an interface 
type Sport interface{ 
      
    // name of sport method 
    sportName() string 
} 
  
// declaring a struct 
type Human struct{ 
      
    // defining struct variables 
    name string 
    sport string 
} 
  
// function to print book details 
func (h Human) sportName() string{ 
  
    // returning a string value 
    return h.name + " plays " + h.sport + "."
} 
  
// main function 
func main() { 
      
    // declaring a struct instance 
    human1 := Human{"Rahul", "chess"} 
      
    // printing details of human1 
    fmt.Println(human1.sportName()) 
      
    // declaring another struct instance 
    human2 := Human{"Riya", "carrom"} 
      
    // printing details of human2 
    fmt.Println(human2.sportName()) 
} 
```

## Polymorphism
In Go, **polymorphism** is achieved differently compared to traditional object-oriented languages like Java or C++, which rely heavily on class inheritance and method overriding. Go does not have classes or inheritance in the classical sense, but it implements polymorphism through **interfaces** and **structural typing**. This approach is lightweight, flexible, and aligns with Go's emphasis on simplicity and composition over inheritance.

Let’s explore how polymorphism works in Go, with examples and explanations.

---

### What is Polymorphism?
Polymorphism refers to the ability of different types to be treated as instances of a common supertype, allowing the same code to work with objects of different types. In Go, this is primarily accomplished using **interfaces**.

---

### Polymorphism via Interfaces
An **interface** in Go is a type that defines a set of method signatures. Any type that implements all the methods of an interface implicitly satisfies that interface—no explicit declaration (like `implements` in Java) is required. This is known as **duck typing** or structural typing: "If it walks like a duck and quacks like a duck, it’s a duck."

#### Basic Example
```go
package main

import "fmt"

// Define an interface
type Speaker interface {
    Speak() string
}

// First type implementing the interface
type Person struct {
    Name string
}

func (p Person) Speak() string {
    return "Hello, my name is " + p.Name
}

// Second type implementing the interface
type Dog struct {
    Breed string
}

func (d Dog) Speak() string {
    return "Woof! I’m a " + d.Breed
}

// Polymorphic function
func makeItSpeak(s Speaker) {
    fmt.Println(s.Speak())
}

func main() {
    p := Person{Name: "Alice"}
    d := Dog{Breed: "Labrador"}

    makeItSpeak(p) // Output: Hello, my name is Alice
    makeItSpeak(d) // Output: Woof! I’m a Labrador
}
```
- The `Speaker` interface defines a single method, `Speak()`.
- Both `Person` and `Dog` implement `Speak()`, so they implicitly satisfy the `Speaker` interface.
- The `makeItSpeak` function accepts any type that satisfies `Speaker`, demonstrating polymorphism.

---

### Key Features of Polymorphism in Go
1. **Implicit Interface Satisfaction**:
   - You don’t need to declare that a type implements an interface. If the type has the required methods, it automatically satisfies the interface.
   - This makes code less coupled and more reusable.

2. **No Inheritance Required**:
   - Unlike traditional OOP, Go doesn’t use inheritance for polymorphism. Instead, it relies on composition and interfaces.
   - You can embed structs (similar to inheritance), but polymorphism comes from interfaces.

3. **Empty Interface (`interface{}`)**:
   - The empty interface has no methods, so every type satisfies it. This can be used for extreme polymorphism (similar to `Object` in Java), though it often requires type assertions.
   ```go
   func printAnything(v interface{}) {
       fmt.Println(v)
   }

   func main() {
       printAnything(42)       // Output: 42
       printAnything("Hello")  // Output: Hello
       printAnything([]int{1, 2}) // Output: [1 2]
   }
   ```

---

### Embedding for Composition
Go supports embedding, which allows one struct to include another. This can be combined with interfaces to achieve polymorphic behavior without inheritance.

#### Example with Embedding
```go
package main

import "fmt"

type Animal interface {
    Move() string
}

type BaseAnimal struct {
    Speed int
}

func (b BaseAnimal) Move() string {
    return fmt.Sprintf("Moving at speed %d", b.Speed)
}

type Bird struct {
    BaseAnimal // Embedding BaseAnimal
    CanFly     bool
}

func (b Bird) Fly() string {
    if b.CanFly {
        return "I can fly!"
    }
    return "I can’t fly."
}

func main() {
    b := Bird{BaseAnimal: BaseAnimal{Speed: 10}, CanFly: true}
    var a Animal = b // Bird satisfies Animal via embedded BaseAnimal
    fmt.Println(a.Move()) // Output: Moving at speed 10
    fmt.Println(b.Fly())  // Output: I can fly!
}
```
- `Bird` embeds `BaseAnimal`, inheriting its `Move()` method.
- `Bird` satisfies the `Animal` interface because it has a `Move()` method (via embedding).
- This allows polymorphic use of `Bird` as an `Animal`.

---

### Pointer Receivers and Interfaces
When defining methods to satisfy an interface, the receiver type (value or pointer) matters:
- If a method uses a **pointer receiver**, only a pointer to the type will satisfy the interface.
- If a method uses a **value receiver**, both the value and a pointer to the type will satisfy the interface (Go auto-dereferences pointers when needed).

#### Example
```go
package main

import "fmt"

type Writer interface {
    Write() string
}

type MyType struct {
    Data string
}

// Value receiver
func (m MyType) Write() string {
    return m.Data
}

func main() {
    m := MyType{Data: "Test"}
    var w Writer = m   // Works with value
    fmt.Println(w.Write()) // Output: Test

    var wp Writer = &m // Works with pointer too
    fmt.Println(wp.Write()) // Output: Test
}
```

Contrast with a pointer receiver:
```go
func (m *MyType) Write() string { // Pointer receiver
    return m.Data
}

func main() {
    m := MyType{Data: "Test"}
    // var w Writer = m  // Error: MyType doesn’t implement Writer, only *MyType does
    var wp Writer = &m   // Works with pointer
    fmt.Println(wp.Write()) // Output: Test
}
```

---

### Run-Time Polymorphism with Type Assertions
Since Go doesn’t have method overriding, run-time polymorphism often involves type assertions or type switches to handle different concrete types dynamically.

#### Example
```go
package main

import "fmt"

type Shape interface {
    Area() float64
}

type Circle struct {
    Radius float64
}

func (c Circle) Area() float64 {
    return 3.14 * c.Radius * c.Radius
}

type Square struct {
    Side float64
}

func (s Square) Area() float64 {
    return s.Side * s.Side
}

func describeShape(s Shape) {
    fmt.Printf("Area: %.2f\n", s.Area())
    switch v := s.(type) {
    case Circle:
        fmt.Println("This is a circle with radius:", v.Radius)
    case Square:
        fmt.Println("This is a square with side:", v.Side)
    }
}

func main() {
    c := Circle{Radius: 2}
    s := Square{Side: 3}

    describeShape(c) // Output: Area: 12.56, This is a circle with radius: 2
    describeShape(s) // Output: Area: 9.00, This is a square with side: 3
}
```
- The `Shape` interface provides polymorphic behavior with `Area()`.
- The type switch (`s.(type)`) allows run-time inspection of the concrete type.

---

### Advantages of Go’s Approach
1. **Simplicity**: No complex inheritance hierarchies; interfaces are lightweight and explicit.
2. **Flexibility**: Any type can implement an interface without modifying its definition.
3. **Decoupling**: Code depends on behavior (methods) rather than specific types.

### Limitations
1. **No Method Overriding**: You can’t override methods like in classical OOP; polymorphism is purely interface-based.
2. **No Default Implementations**: Interfaces only define method signatures, not implementations (unlike default methods in Java).
3. **Run-Time Overhead**: Type assertions and switches introduce some overhead and require careful handling.

---

### Conclusion
Polymorphism in Go is achieved through interfaces and structural typing, providing a clean and pragmatic alternative to inheritance-based polymorphism. By defining behavior via method sets and using interfaces as contracts, Go allows different types to be treated uniformly, enabling flexible and reusable code. While it lacks some features of traditional OOP (e.g., method overriding), its simplicity and composition-based design make it powerful for many use cases.