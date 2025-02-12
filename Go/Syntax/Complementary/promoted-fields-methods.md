# Promoted fields and methods

Okay, let's break down this explanation of promoted fields and methods in Go, line by line, with examples. This is a crucial concept for understanding how embedding works in Go structs.

**Part 1: Promoted Fields**

```
Promoted fields act like ordinary fields of a struct except that they cannot be used as field names in composite literals of the struct.
```

*   **`Promoted fields act like ordinary fields of a struct...`**  This means that if you embed a type `T` within a struct `S`, you can access the fields of `T` *directly* on an instance of `S`, as if they were fields of `S` itself.  This is the "promotion."

*   **`...except that they cannot be used as field names in composite literals of the struct.`** This is the key restriction.  A composite literal is a way to create and initialize a struct (or array, slice, or map) in a concise way.  You *cannot* use the embedded type's name as a field name when initializing the outer struct.

**Example (Promoted Fields):**

```go
package main

import "fmt"

type Inner struct {
	X int
	Y string
}

type Outer struct {	Inner // Inner is an embedded (anonymous) field
	Z float64
}

func main() {
	// Accessing fields directly (promotion)
	outer := Outer{Z: 3.14}
	outer.X = 10       // Accessing Inner's X field directly on outer
	outer.Y = "Hello"  // Accessing Inner's Y field directly on outer
	fmt.Println(outer.X, outer.Y, outer.Z)

	// Valid composite literal:
	outer2 := Outer{
		Inner: Inner{X: 20, Y: "World"}, // Correct:  Initialize the embedded struct separately.
		Z:     6.28,
	}
	fmt.Println(outer2.X, outer2.Y, outer2.Z)

	// Invalid composite literal:
	// outer3 := Outer{
	// 	X: 30,  // ERROR: Cannot use X (from Inner) as a field name here.
	// 	Y: "!", // ERROR: Cannot use Y (from Inner) as a field name here.
	// 	Z: 9.42,
	// }
}
```

*   **`type Inner struct { ... }`**: Defines a simple struct with two fields.
*   **`type Outer struct { Inner ... }`**: Defines `Outer`, embedding `Inner`.  `Inner` is an *embedded field* (also called an anonymous field).
*   **`outer.X = 10`**: This is the promotion in action.  We access `X` (a field of `Inner`) directly on `outer`.
*   **`outer2 := Outer{ Inner: ... }`**: This is the *correct* way to use a composite literal with an embedded field. You initialize the embedded field as a whole, using its type name.
*   **`outer3 := Outer{ X: ... }`**: This is *invalid* and will cause a compile-time error. You cannot use the field names of the embedded type (`X`, `Y`) directly within the composite literal of the outer type.

**Part 2: Promoted Methods**

Now, let's look at promoted methods. This is where the concept of a "receiver" comes in.

*   **Method Receiver:** A method in Go is a function associated with a particular type. The *receiver* is the value on which the method is called.  It's like the `self` in Python or `this` in Java/C++, but in Go, you explicitly declare the receiver and give it a name.

    ```go
    type MyType int

    // Method with receiver of type MyType
    func (m MyType) MyMethod() {
        fmt.Println("MyMethod called on:", m)
    }

    // Method with receiver of type *MyType (pointer to MyType)
    func (m *MyType) MyPointerMethod() {
        fmt.Println("MyPointerMethod called on:", *m)
        *m = 42 // Can modify the original value
    }
    ```

    *   `func (m MyType) MyMethod() { ... }`:  `m` is the receiver, and its type is `MyType`. This is a *value receiver*.  The method receives a *copy* of the `MyType` value.
    *   `func (m *MyType) MyPointerMethod() { ... }`: `m` is the receiver, and its type is `*MyType` (a pointer to `MyType`). This is a *pointer receiver*. The method receives the *memory address* of the `MyType` value, so it can modify the original.

Now, let's analyze the rules for promoted methods:

```
Given a struct type S and a type name T, promoted methods are included in the method set of the struct as follows:

If S contains an embedded field T, the method sets of S and *S both include promoted methods with receiver T. The method set of *S also includes promoted methods with receiver *T.
```

*   **`If S contains an embedded field T...`**: We're talking about embedding again, like in the previous example.
*   **`...the method sets of S and *S both include promoted methods with receiver T.`**:  If `T` has methods, those methods become available on both `S` (value) and `*S` (pointer to `S`).  The promoted methods will have a receiver of type `T` (value receiver).
*   **`The method set of *S also includes promoted methods with receiver *T.`**:  If `T` has methods with a *pointer* receiver (`*T`), those methods are also promoted, but *only* to `*S` (pointer to `S`).  They are *not* promoted to `S` (value).

**Example (Promoted Methods, Case 1):**

```go
package main

import "fmt"type T struct {
	Name string
}

// Method with value receiver
func (t T) ValueMethod() {
	fmt.Println("ValueMethod called on:", t.Name)
	t.Name = "Changed in ValueMethod" // Modifies the copy
}

// Method with pointer receiver
func (t *T) PointerMethod() {
	fmt.Println("PointerMethod called on:", t.Name)
	t.Name = "Changed in PointerMethod" // Modifies the original
}

type S struct {
	T // Embedded field
}

func main() {
	s := S{T: T{Name: "Original"}}
	s.ValueMethod()   // Promoted to S (value)
	fmt.Println("After ValueMethod:", s.Name) // Output: Original (copy was modified)

	s.PointerMethod() // Promoted to S (because s is addressable)
	fmt.Println("After PointerMethod:", s.Name) // Output: Changed in PointerMethod

	ps := &s          // Get a pointer to s
	ps.ValueMethod()  // Promoted to *S (value receiver)
	fmt.Println("After ps.ValueMethod:", ps.Name) // Output: Changed in PointerMethod

	ps.PointerMethod() // Promoted to *S (pointer receiver)
	fmt.Println("After ps.PointerMethod:", ps.Name) // Output: Changed in PointerMethod
}

```

*   **`type T struct { ... }`**: Defines a type `T` with a `Name` field.
*   **`func (t T) ValueMethod() { ... }`**:  A method with a *value* receiver (`T`).
*   **`func (t *T) PointerMethod() { ... }`**: A method with a *pointer* receiver (`*T`).
*   **`type S struct { T }`**:  `S` embeds `T`.
*   **`s.ValueMethod()`**:  `ValueMethod` (which has a `T` receiver) is promoted to `S`.  Because it's a value receiver, it works on a *copy* of the embedded `T`.
*   **`s.PointerMethod()`**:  `PointerMethod` (which has a `*T` receiver) is also promoted to `S`. Go automatically takes the address of 's' because 's' is addressable.
*   **`ps := &s`**:  We get a pointer to `s`.
*   **`ps.ValueMethod()`**: `ValueMethod` is promoted to `*S`.
*   **`ps.PointerMethod()`**: `PointerMethod` is promoted to `*S`.

```
If S contains an embedded field *T, the method sets of S and *S both include promoted methods with receiver T or *T.
```

*   **`If S contains an embedded field *T...`**: Now, we're embedding a *pointer* to `T`.
*   **`...the method sets of S and *S both include promoted methods with receiver T or *T.`**:  Methods of both `T` (value receiver) and `*T` (pointer receiver) are promoted to both `S` and `*S`.

**Example (Promoted Methods, Case 2):**

```go
package main

import "fmt"

type T struct {
	Name string
}

// Method with value receiver
func (t T) ValueMethod() {
	fmt.Println("ValueMethod called on:", t.Name)
}

// Method with pointer receiver
func (t *T) PointerMethod() {
	fmt.Println("PointerMethod called on:", t.Name)
	t.Name = "Changed in PointerMethod"
}

type S struct {
	*T // Embedded pointer to T
}

func main() {
	t := T{Name: "Original T"}
	s := S{T: &t} // Embed a pointer to t

	s.ValueMethod()   // Promoted to S
	fmt.Println("After s.ValueMethod:", s.T.Name) //Original T

	s.PointerMethod() // Promoted to S
	fmt.Println("After s.PointerMethod:", s.T.Name) //Changed in PointerMethod

	ps := &s
	ps.ValueMethod()  // Promoted to *S
	fmt.Println("After ps.ValueMethod:", ps.T.Name) //Changed in PointerMethod

	ps.PointerMethod() // Promoted to *S
	fmt.Println("After ps.PointerMethod:", ps.T.Name) //Changed in PointerMethod

	// Example with nil embedded pointer:
    s2 := S{} // T is nil
    // s2.ValueMethod()   // This would panic!  Cannot call on nil receiver.
    // s2.PointerMethod() // This would also panic!

	// To safely use methods with a potentially nil embedded pointer,
    // you need to check for nil first:
    if s2.T != nil {
        s2.ValueMethod()
        s2.PointerMethod()
    } else {
        fmt.Println("s2.T is nil")
    }
}
```

*   **`type S struct { *T }`**: `S` now embeds a *pointer* to `T`.
*   **`s := S{T: &t}`**: We initialize `s` with a pointer to a `T` instance.
*   **`s.ValueMethod()` and `s.PointerMethod()`**: Both methods are promoted to `S` (and `*S`).
*   **`s2 := S{}`**: This creates an `S` where the embedded pointer `T` is `nil`.
*   **`s2.ValueMethod()` and `s2.PointerMethod()` (commented out)**: These would cause a *panic* (runtime error) because you cannot call a method on a `nil` receiver.
*   **`if s2.T != nil { ... }`**: This demonstrates the *crucial* check you need to perform when embedding pointers.  You *must* check for `nil` before calling methods on the embedded pointer.

**Summary and Key Differences**

1.  **Promoted Fields:** Allow direct access to the fields of an embedded type, but you can't use those field names in composite literals of the outer struct.

2.  **Promoted Methods:**  Methods of the embedded type are "promoted" to the outer struct, making them callable directly on instances of the outer struct.

3.  **Value vs. Pointer Receivers:** The type of receiver (value or pointer) determines whether the method operates on a copy or the original value.  This affects whether modifications made within the method are visible outside the method.

4.  **Embedding `T` vs. `*T`:**
    *   Embedding `T` promotes methods with `T` receivers to both `S` and `*S`, and methods with `*T` receivers only to `*S`.
    *   Embedding `*T` promotes methods with both `T` and `*T` receivers to both `S` and `*S`.  However, you *must* check for `nil` before calling methods on the embedded pointer.

5.  **Addressability:** When you call a method with pointer receiver on a value (like `s.PointerMethod()`), Go will automatically take the address of that value if it is *addressable*. A variable is always addressable.

This detailed explanation, along with the comprehensive examples, should give you a solid understanding of promoted fields and methods in Go.  These are powerful features that enable code reuse and composition, but it's important to understand the nuances of receivers and nil pointers to use them effectively and safely.