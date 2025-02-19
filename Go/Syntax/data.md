# Data

## int
```go
a0 := 0 // decimal
a0 := _10_000 // decimal
a1 := 0b100 // binary
a1 := 0B100 // binary
a2 := 0  // octal
a2 := 0o72 // octal
a2 := 0O65 // octal
a3 := 0xaf // hex
a3 := 0XBC // hex
```

## float
```bash
0.
72.40
072.40       // == 72.40
2.71828
1.e+0
6.67428e-11
1E6
.25
.12345E+5
1_5.         // == 15.0
0.15e+0_2    // == 15.0

0x1p-2       // == 0.25
0x2.p10      // == 2048.0
0x1.Fp+0     // == 1.9375
0X.8p-0      // == 0.5
0X_1FFFP-16  // == 0.1249847412109375

0x15e-2      // == 0x15e - 2 (integer subtraction)

0x.p1        // invalid: mantissa has no digits
1p-2         // invalid: p exponent requires hexadecimal mantissa
0x1.5e-2     // invalid: hexadecimal mantissa requires p exponent
1_.5         // invalid: _ must separate successive digits
1._5         // invalid: _ must separate successive digits
1.5_e1       // invalid: _ must separate successive digits
1.5e_1       // invalid: _ must separate successive digits
1.5e1_       // invalid: _ must separate successive digits
```

## imaginary
```bash
0i
0123i         // == 123i for backward-compatibility
0o123i        // == 0o123 * 1i == 83i
0xabci        // == 0xabc * 1i == 2748i
0.i
2.71828i
1.e+0i
6.67428e-11i
1E6i
.25i
.12345E+5i
0x1p-2i       // == 0x1p-2 * 1i == 0.25i
```

## rune
> an integer value identifying a Unicode code point
> There are four ways to represent the integer value as a numeric constant: 
* \x followed by exactly two hexadecimal digits; 
* \u followed by exactly four hexadecimal digits; 
* \U followed by exactly eight hexadecimal digits, 
* and a plain backslash \ followed by exactly three octal digits. 
> In each case the value of the literal is the value represented by the digits in the corresponding base.

- special values
```bash
\a   U+0007 alert or bell
\b   U+0008 backspace
\f   U+000C form feed
\n   U+000A line feed or newline
\r   U+000D carriage return
\t   U+0009 horizontal tab
\v   U+000B vertical tab
\\   U+005C backslash
\'   U+0027 single quote  (valid escape only within rune literals)
\"   U+0022 double quote  (valid escape only within string literals)
```

```bash
'a'
'ä'
'本'
'\t'
'\000'
'\007'
'\377'
'\x07'
'\xff'
'\u12e4'
'\U00101234'
'\''         // rune literal containing single quote character

'aa'         // illegal: too many characters
'\k'         // illegal: k is not recognized after a backslash
'\xa'        // illegal: too few hexadecimal digits
'\0'         // illegal: too few octal digits
'\400'       // illegal: octal value over 255
'\uDFFF'     // illegal: surrogate half
'\U00110000' // illegal: invalid Unicode code point
```

## string
- raw string
> any char except back quote
> backslash have no meaning

- interpreted sting
> backslashes interpreted as runes

- These examples all represent the same string:
```bash
"日本語"                                 // UTF-8 input text
`日本語`                                 // UTF-8 input text as a raw literal
"\u65e5\u672c\u8a9e"                    // the explicit Unicode code points
"\U000065e5\U0000672c\U00008a9e"        // the explicit Unicode code points
"\xe6\x97\xa5\xe6\x9c\xac\xe8\xaa\x9e"  // the explicit UTF-8 bytes
```

```bash
`abc`                // same as "abc"
`\n
\n`                  // same as "\\n\n\\n"
"\n"
"\""                 // same as `"`
"Hello, world!\n"
"日本語"
"\u65e5本\U00008a9e"
"\xff\u00FF"
"\uD800"             // illegal: surrogate half
"\U00110000"         // illegal: invalid Unicode code point
```

[characters with accent](./Complementary/char-with-accent.md)

## interface

**What is `interface{}`?**

In Go, an interface defines a set of methods that a type must implement.  The empty interface, `interface{}`, has *no* methods.  This means *any* type in Go satisfies the empty interface.  It's a very general type.  Think of it as a "container" that can hold values of any type.

**Why use `interface{}`?**

1. **Flexibility/Generality:**  The primary use is when you need a function or data structure that can work with values of any type.  This is particularly useful when you don't know the specific type at compile time.

2. **Working with unknown types:** When receiving data from external sources (e.g., JSON, network requests), you might not know the exact structure beforehand. `interface{}` allows you to hold these values until you can determine their type.

3. **Implementing generic-like behavior:**  While Go doesn't have generics in the traditional sense, `interface{}` can be used to achieve similar effects in certain situations.

**Examples:**

```go
package main

import (
        "fmt"
)

func describe(i interface{}) {
        fmt.Printf("Type: %T, Value: %v\n", i, i)
}

func main() {
      
	var y interface{}

	y = 42         // Assign an integer
	describe(y)

	y = "hello"    // Assign a string
	describe(y)

	type MyStruct struct {
			Name string
			Age  int
	}
	y = MyStruct{"Alice", 30} // Assign a struct
	describe(y)

	type myArr []int
	y = myArr{1, 2, 3} // Assign a slice
	describe(y)


    // Type assertion:  You can check the underlying type and access its value.
    // This is crucial when working with interface{}.
    if str, ok := y.(string); ok {
        fmt.Println("y is a string:", str)
    }

    if myStruct, ok := y.(MyStruct); ok {
        fmt.Println("y is a MyStruct:", myStruct.Name, myStruct.Age)
    }

    if arr, ok := y.(myArr); ok {
        fmt.Println("y is a slice:", arr)
    }

    // Type switch: Use to handle different types held by interface{}
    switch v := y.(type) {
    case int:
        fmt.Println("y is an int:", v)
    case string:
        fmt.Println("y is a string:", v)
    case MyStruct:
        fmt.Println("y is a MyStruct:", v.Name, v.Age)
    case myArr:
        fmt.Println("y is a MyArr:", v)
    default:
        fmt.Println("y is of another type")
    }
}
```

1. **Type Assertion:** The `y.(string)` attempts to convert the interface value `y` to a string. The `ok` variable will be true if the conversion is successful.  This is essential for accessing the underlying value's specific properties.  If you try a type assertion to an incorrect type, your program will panic.

2. **Type Switch:**  A type switch is a more elegant way to handle different types held by an `interface{}`.  It allows you to execute different code blocks based on the underlying type.

**Important Considerations:**

* **Type Safety:** While `interface{}` provides flexibility, it comes at the cost of some type safety.  You lose static type checking at compile time.  You'll need to use type assertions or type switches at runtime to work with the actual values, and there's a risk of runtime errors (panics) if you make incorrect assumptions about the type.

* **Performance:**  Using `interface{}` can sometimes have a slight performance overhead compared to working with concrete types because of the runtime type checking. However, in many cases the flexibility outweighs this minor performance difference.

In summary,  it's crucial to use type assertions and type switches carefully to ensure type safety and avoid runtime errors. 
Use it when you genuinely need the flexibility it provides, but try to use concrete types whenever possible for better type safety and performance.

## variable
> If a variable has not yet been assigned a value, its value is the zero value for its type.
```go
var x interface{}  // x is nil and has static type interface{}
var v *T           // v has value nil, static type *T
x = 42             // x has value 42 and dynamic type int
x = v              // x has value (*T)(nil) and dynamic type *T
```

## type

### boolean
```go
// boolean
bool (true, false)
```
### numeric
```go
uint8       the set of all unsigned  8-bit integers (0 to 255)
uint16      the set of all unsigned 16-bit integers (0 to 65535)
uint32      the set of all unsigned 32-bit integers (0 to 4294967295)
uint64      the set of all unsigned 64-bit integers (0 to 18446744073709551615)

int8        the set of all signed  8-bit integers (-128 to 127)
int16       the set of all signed 16-bit integers (-32768 to 32767)
int32       the set of all signed 32-bit integers (-2147483648 to 2147483647)
int64       the set of all signed 64-bit integers (-9223372036854775808 to 9223372036854775807)

float32     the set of all IEEE 754 32-bit floating-point numbers
float64     the set of all IEEE 754 64-bit floating-point numbers

complex64   the set of all complex numbers with float32 real and imaginary parts
complex128  the set of all complex numbers with float64 real and imaginary parts

byte        alias for uint8
rune        alias for int32

// predeclared integer types with implementation-specific sizes
uint     either 32 or 64 bits
int      same size as uint
uintptr  an unsigned integer large enough to store the uninterpreted bits of a pointer value

//byte -> alias for uint8
// rune -> alias for int32
// Explicit conversions are required when different numeric types are mixed in an expression or assignment. For instance, int32 and int are not the same type even though they may have the same size on a particular architecture
```

### string
> Strings are immutable: once created, it is impossible to change the contents of a string
> The `length of a string` s can be discovered using the built-in function `len`
> It is illegal to take the address of such an element; if s[i] is the i'th byte of a string, &s[i] is invalid
```go
string x = "asasa"
len(x)
x[2]
// &x[2] illegal
```

### array
> The `length of array` a can be discovered using the built-in function `len`
```go
x := [lenght | nil]<type>
y := []int{}
z := [12]rune{}
r := [][]int{}

var r [32]byte
type myType [2*N] struct { x, y int32 }
var r [1000]*float64
var r [3][5]int
var r [2][2][2]float64  // same as [2]([2]([2]float64))
```
["Example in code"](./Complementary/Valid-types.go)

### slice
* The length of a slice s can be discovered by the built-in function len
* unlike with arrays it may change during execution
* A slice, once initialized, is always associated with an underlying array that holds its elements. A slice therefore shares storage with its array and with other slices of the same array; by contrast, distinct arrays always represent distinct storage.
* The capacity is a measure of that extent: it is the sum of the length of the slice and the length of the array beyond the slice
* a slice of length up to that capacity can be created by slicing a new one from the original slice.
* The capacity of a slice a can be discovered using the built-in function cap(a).
* A slice created with make always allocates a new, hidden array to which the returned slice value refers
```go
make([]T, length, capacity)
```
* produces the same slice as allocating an array and slicing it, so these two expressions are equivalent:
```go
make([]int, 50, 100)
new([100]int)[0:50]

// copy
copy(dst, src)
// Element-wise copy: copy copies elements one by one from src to dst.
[more info](./Complementary/copy.md)
```

### struct
```go
// An empty struct.
struct {}

// A struct with 6 fields.
struct {
	x, y int
	u float32
	_ float32  // padding
	A *[]int
	F func()
}
```
#### embedded field
- embedded field (fields with no name)
- unqualified type name acts as the field name
```go
// A struct with four embedded fields of types T1, *T2, P.T3 and *P.T4
struct {
	T1        // field name is T1
	*T2       // field name is T2
	P.T3      // field name is T3
	*P.T4     // field name is T4
	x, y int  // field names are x and y
}
```
#### Promoted fields & methods
- A field or method f of an embedded field in a struct x is called promoted if x.f is a legal selector that denotes that field or method f.
> Promoted fields act like ordinary fields of a struct except that they cannot be used as field names in composite literals of the struct.

Given a struct type S and a type name T, promoted methods are included in the method set of the struct as follows:

If S contains an embedded field T, the method sets of S and *S both include promoted methods with receiver T. The method set of *S also includes promoted methods with receiver *T.
If S contains an embedded field *T, the method sets of S and *S both include promoted methods with receiver T or *T.
[more on Promoted fields and methods](./Complementary/promoted-fields-methods.md)
- field names must be unique within struct type
```go
struct {
	T     // conflicts with embedded field *T and *P.T
	*T    // conflicts with embedded field T and *P.T
	*P.T  // conflicts with embedded field T and *T
}
```

#### tags
> A field declaration may be followed by an optional string literal tag, which becomes an attribute for all the fields in the corresponding field declaration. An empty tag string is equivalent to an absent tag. The tags are made visible through a reflection interface and take part in type identity for structs but are otherwise ignored.
[explain tags in more detail & example](./Complementary/tags.md)
* used for orm, json and ... mapping
* applied to all of the fields in their line (for example : x, y int "this tag applied to both x and y)
* if empty, is like no tag is specified for the field
```go
struct {
	x, y float64 ""  // an empty tag string is like an absent tag
	name string  "any string is permitted as a tag"
	_    [4]byte "ceci n'est pas un champ de structure"
}

// A struct corresponding to a TimeStamp protocol buffer.
// The tag strings define the protocol buffer field numbers;
// they follow the convention outlined by the reflect package.
struct {
	microsec  uint64 `protobuf:"1"`
	serverIP6 uint64 `protobuf:"2"`
}

```
### const
```go
type EducationLevel int 

const (
	Diploma EducationLevel = iota + 1
	Bachelor
	Master
	PHD
)
```

## function
```go
func()
func(x int) int
func(a, _ int, z float32) bool
func(a, b int, z float32) (bool)
func(prefix string, values ...int)
func(a, b int, z float64, opt ...interface{}) (success bool)
func(int, int, float64) (float64, *[]int)
func(n int) func(p *T)
```
- declare output variable
```go
func ReadFull(r Reader, buf []byte) (n int, err error) {
    for len(buf) > 0 && err == nil {
        var nr int
        nr, err = r.Read(buf)
        n += nr
        buf = buf[nr:]
    }
    return
}
```

## map
* The value of an uninitialized map is nil
* unordered group of elements
* nil map is equivalent to an empty map except that no elements may be added
[how it works](./Complementary/map.md)
```go

map[string]int
map[*T]struct{ x, y float64 }
map[string]interface{}

// delete
delete clear

// size
len(myMap)

// define
make(map[string]int, 100) // argument capacity optionaly

// existence
if v2, ok := m2[k] // return value and boolean
// if not existed, return false along with the value zero-value
```

## channel
* A channel provides a mechanism for concurrently executing functions 
* to communicate by sending and receiving values of a specified element type
* if a direction is given, the channel is directional, otherwise it is bidirectional
* A channel may be constrained only to send or only to receive by assignment or explicit conversion
* calls to the built-in functions cap and len by any number of goroutines without further synchronization
* Channels act as first-in-first-out queues
* If the capacity is zero or absent, the channel is unbuffered and communication succeeds only when both a sender and receiver are ready
* Otherwise, the channel is buffered and communication succeeds without blocking 
* if the buffer is not full (sends) or not empty (receives)
* A nil channel is never ready for communication.


```go
chan T          // can be used to send and receive values of type T
chan<- float64  // can only be used to send float64s
<-chan int      // can only be used to receive ints

chan<- chan int    // same as chan<- (chan int)
chan<- <-chan int  // same as chan<- (<-chan int)
<-chan <-chan int  // same as <-chan (<-chan int)
chan (<-chan int)

// construct
make(chan int, 100)//optional capacity

// close
close
```

