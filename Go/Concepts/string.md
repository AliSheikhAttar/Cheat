# string

## pass to function
How strings are passed to functions in Go (Golang). Go has a straightforward approach, but it’s worth unpacking because strings in Go have some unique characteristics.

In Go, everything is passed by value by default. That means when you pass a string to a function, the function gets a copy of the string value. However, strings in Go are immutable and implemented as a struct under the hood, consisting of two parts:
- A pointer to the underlying byte array (the actual character data).
- A length field (an integer tracking the string’s size).

This struct is defined in the Go runtime roughly like:
```go
type stringStruct struct {
    data *byte
    len  int
}

```
When you pass a string to a function, you’re copying this struct—i.e., the pointer to the data and the length. The actual byte array (the string’s content) isn’t copied, because the pointer just points to the same memory. This makes string passing efficient: you’re not duplicating the entire string’s content, just the small struct (typically 16 bytes on a 64-bit system: 8 for the pointer, 8 for the length).

Here’s an example:
```go
package main

import "fmt"

func modifyString(s string) {
    s = "World" // Changes the local copy of the string struct
    fmt.Println("Inside:", s)
}

func main() {
    str := "Hello"
    modifyString(str)
    fmt.Println("Outside:", str) // Still "Hello"
}
```
Output:
```
Inside: World
Outside: Hello
```
Why doesn’t `str` change? Because `s` in `modifyString` is a copy of the string struct. Assigning `"World"` to `s` updates the local copy’s pointer and length to point to the new string’s data, but the original `str` in `main` remains unchanged. This is classic pass-by-value behavior.

Now, if you want to modify the original string, you’d need to use a pointer to the string:
```go
package main

import "fmt"

func modifyStringPtr(s *string) {
    *s = "World" // Dereference and modify the original
    fmt.Println("Inside:", *s)
}

func main() {
    str := "Hello"
    modifyStringPtr(&str)
    fmt.Println("Outside:", str) // Now "World"
    
}
```
Output:
```
Inside: World
Outside: World
```
Here, you pass a pointer to the string variable (`&str`), and the function modifies the string it points to. The `*string` type means the function works with the address of the string struct, not a copy of it.

A few key points about strings in Go:
- **Immutability**: You can’t change the contents of a string (e.g., `s[0] = 'x'` isn’t allowed). "Modifying" a string means creating a new one and reassigning it.
- **Efficiency**: Passing by value is cheap because it’s just copying the pointer and length, not the data. But if you’re passing huge strings and want to avoid even that small copy, pointers can help.
- **No references**: Unlike C++ with `&` for references, Go sticks to pointers explicitly with `*`. There’s no pass-by-reference in the C++ sense.

So, in Go:
- **Pass-by-value**: Default for strings. Copies the string struct (pointer + length). Safe and immutable, but changes don’t affect the original.
- **Pass-by-pointer**: Use `*string` to pass the address of the string variable. Allows modification of the original string by dereferencing.

Does that clarify things? Want to dig into a specific use case or example?


## memory allocation
Let’s address your query about strings and slices in Go, specifically whether a string is a slice of bytes or runes, and where the underlying array is defined when we create them.

### Are Strings a Slice of Bytes or Runes?

In Go, **strings are not slices**. A string is a distinct type defined as an immutable sequence of bytes. These bytes represent text encoded in UTF-8, which allows strings to handle both ASCII characters (like "hello") and non-ASCII characters (like "héllo") efficiently. Unlike slices, which are mutable reference types that point to an underlying array, strings cannot be modified once created.

However, strings can be **converted** to slices:
- **Slice of bytes**: Using `[]byte(s)`, a string can be converted to a slice of bytes (type `[]byte`). This gives you the raw UTF-8 bytes of the string.
- **Slice of runes**: Using `[]rune(s)`, a string can be converted to a slice of runes (type `[]rune`), where each rune is an `int32` representing a Unicode code point.

For example:
```go
s := "héllo"
b := []byte(s)   // b is [104, 195, 169, 108, 108, 111] (UTF-8 bytes)
r := []rune(s)   // r is [104, 233, 108, 108, 111] (Unicode code points)
```
Here, "h" is `104`, "é" is encoded as `195, 169` in UTF-8 (two bytes, decimal 233 as a rune), and "l", "l", "o" are `108, 108, 111`.

Note that when you index a string directly (e.g., `s[0]`), you get a `byte` (type `uint8`), not a rune. For instance:
```go
s := "hello"
fmt.Println(s[0])  // Outputs 104 (the byte value of 'h')
```
Slicing a string (e.g., `s[1:3]`) returns another string, not a slice:
```go
sub := s[1:3]  // sub is "el", a string
```
So, to summarize this part: **strings are sequences of bytes, not slices of bytes or runes**, but they can be converted into either type explicitly.

### Where Is the Underlying Array Defined When We Create Them?

Now, let’s explore where the underlying array (the actual byte data) is stored when we create strings and when we convert them to slices.

#### Strings
When you create a string in Go, it consists of a header with two components:
- A **pointer** to an array of bytes.
- A **length** indicating the number of bytes.

The location of this byte array depends on how the string is created:
- **String literals** (e.g., `s := "hello"`): The byte array is stored in the **read-only data section** of the program’s memory. This is because string literals are constant and immutable, and the compiler can optimize them by placing them in a read-only segment.
- **Dynamically created strings** (e.g., via concatenation like `s := "hel" + "lo"` or runtime operations): The resulting byte array is typically allocated on the **heap**, as it’s constructed at runtime. Even so, the string remains immutable, and Go ensures its data cannot be altered.

For example:
```go
s := "hello"
// The bytes [104, 101, 108, 108, 111] are in read-only memory,
// and s holds a pointer to this data with length 5.
```

#### Slices Created from Strings
When you convert a string to a slice of bytes or runes, a **new underlying array** is created:
- **`[]byte(s)`**: This conversion allocates a new mutable byte array and **copies** the string’s bytes into it. The new array is typically allocated on the **heap** (though small slices might be stack-allocated in optimized cases). This copy ensures that modifications to the byte slice don’t affect the original string, which remains immutable.
- **`[]rune(s)`**: This conversion allocates a new array of `int32` values (runes), decodes the string’s UTF-8 bytes into Unicode code points, and stores them in the new array, also typically on the **heap**.

For example:
```go
s := "hello"
b := []byte(s)   // New array [104, 101, 108, 108, 111] on the heap
b[0] = 'H'       // b becomes [72, 101, 108, 108, 111], s is still "hello"
r := []rune(s)   // New array [104, 101, 108, 108, 111] on the heap
r[0] = 'H'       // r becomes [72, 101, 108, 108, 111], s is still "hello"
```
The immutability of `s` is preserved because `b` and `r` operate on their own copies of the data.

#### Efficiency Note
Copying data during conversion can be expensive for large strings. In rare cases, the `unsafe` package can be used to create a byte slice that shares the string’s underlying array without copying, but this is unsafe (it risks modifying read-only memory) and discouraged in standard Go programming.

### Final Answer
- **Are strings a slice of bytes or runes?** No, strings are not slices. They are immutable sequences of bytes representing UTF-8 encoded text. They can be converted to a slice of bytes (`[]byte`) or a slice of runes (`[]rune`), but they are a distinct type.
- **Where is the underlying array defined?**
  - For a **string**: The byte array is in **read-only memory** for literals or on the **heap** for dynamically created strings.
  - For a **slice created from a string**: A new mutable array is allocated (typically on the **heap**), and the string’s data is copied into it during conversion.

This distinction ensures strings remain immutable while allowing flexible manipulation via slices when needed.