# Control

## For
```go
// Like a C for
for init; condition; post { }

// Like a C while
for condition { }

// Like a C for(;;)
for { }
```
```go
sum := 0
for i := 0; i < 10; i++ {
    sum += i
}
```
- If you're looping over an array, slice, string, or map, or reading from a channel, a range clause can manage the loop.
```go
for key, value := range oldMap {
    newMap[key] = value
}
```
- If you only need the first item in the range (the key or index), drop the second:
```go
for key := range m {
    if key.expired() {
        delete(m, key)
    }
}
```
- If you only need the second item in the range (the value), use the blank identifier, an underscore, to discard the first:
```go
sum := 0
for _, value := range array {
    sum += value
}
```

- multi variable loop
```go   
// Reverse a
for i, j := 0, len(a)-1; i < j; i, j = i+1, j-1 {
    a[i], a[j] = a[j], a[i]
}
```
## switch
* The expressions need not be constants or even integers
* the cases are evaluated top to bottom until a match is found
* if the switch has no expression it switches on true. It's therefore possible—and idiomatic—to write an if-else-if-else chain as a switch
```go
func unhex(c byte) byte {
    switch {
    case '0' <= c && c <= '9':
        return c - '0'
    case 'a' <= c && c <= 'f':
        return c - 'a' + 10
    case 'A' <= c && c <= 'F':
        return c - 'A' + 10
    }
    return 0
}
```
* cases can be presented in comma-separated lists
```go
func shouldEscape(c byte) bool {
    switch c {
    case ' ', '?', '&', '=', '#', '+', '%':
        return true
    }
    return false
}
```
* automatically break, dont need to write it
* if dont want to break -> `fallthrough`
```go
switch c {
    case 'x':
        fmt.Println("hi")
        fallthrough
    case 'y':
        fmt.Println("bye")
}
```

* Sometimes, though, it's necessary to break out of a surrounding loop, not the switch, and in Go that can be accomplished by putting a label on the loop and "breaking" to that label
* continue statement also accepts an optional label but it applies only to loops.
```go
Loop:
    for n := 0; n < len(src); n += size {
        switch {
        case src[n] < sizeOne:
            if validateOnly {
                break
            }
            size = 1

        case src[n] < sizeTwo:
            if n+1 >= len(src) {
                err = errShortInput
                break Loop
            }
            if validateOnly {
                break
            }
        }
    }
```

### Type switch
```go
var t interface{}
t = functionOfSomeType()
switch t := t.(type) {
default:
    fmt.Printf("unexpected type %T\n", t)     // %T prints whatever type t has
case bool:
    fmt.Printf("boolean %t\n", t)             // t has type bool
case int:
    fmt.Printf("integer %d\n", t)             // t has type int
case *bool:
    fmt.Printf("pointer to boolean %t\n", *t) // t has type *bool
case *int:
    fmt.Printf("pointer to integer %d\n", *t) // t has type *int
}
```

## defer
* schedules a function call (the deferred function) to be run immediately before the function executing the defer returns
* examples are unlocking a mutex or closing a file
* effective way to deal with situations such as resources that must be released regardless of which path a function takes to return
```go
// Contents returns the file's contents as a string.
func Contents(filename string) (string, error) {
    f, err := os.Open(filename)
    if err != nil {
        return "", err
    }
    defer f.Close()  // f.Close will run when we're finished.

    var result []byte
    buf := make([]byte, 100)
    for {
        n, err := f.Read(buf[0:])
        result = append(result, buf[0:n]...) // append is discussed later.
        if err != nil {
            if err == io.EOF {
                break
            }
            return "", err  // f will be closed if we return here.
        }
    }
    return string(result), nil // f will be closed if we return here.
}
```
> Deferring a call to a function such as Close has two advantages. 
* First, it guarantees that you will never forget to close the file, a mistake that's easy to make if you later edit the function to add a new return path. 
* Second, it means that the close sits near the open, which is much clearer than placing it at the end of the function.
---

- a single deferred call site can defer multiple function executions
```go
for i := 0; i < 5; i++ {
    defer fmt.Printf("%d ", i)
}
```
> Deferred functions are executed in LIFO order, so this code will cause 4 3 2 1 0 to be printed when the function returns.

- tracing
```go
func trace(s string)   { fmt.Println("entering:", s) }
func untrace(s string) { fmt.Println("leaving:", s) }

// Use them like this:
func a() {
    trace("a")
    defer untrace("a")
    // do something....
}
```
--- 
* The arguments to the deferred function (which include the receiver if the function is a method) are evaluated when the defer executes, not when the call executes.
```go
func trace(s string) string {
    fmt.Println("entering:", s)
    return s
}

func un(s string) {
    fmt.Println("leaving:", s)
}

func a() {
    defer un(trace("a"))
    fmt.Println("in a")
}

func b() {
    defer un(trace("b"))
    fmt.Println("in b")
    a()
}

func main() {
    b()
}
```
> entering: b
in b
entering: a
in a
leaving: a
leaving: b