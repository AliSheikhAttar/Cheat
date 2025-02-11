# Anonymous fields in structs - like object composition

Go allows you to define a struct that has fields but with no variable names. These fields are called anonymous fields. 

instance of Kitchen ni House is an anonymous field, because we have not given a variable name for it.

```Go
package main

import "fmt"

type Kitchen struct {
    numOfPlates int 
}

type House struct {
    Kitchen //anonymous field
    numOfRooms int 
}

func main() {
    h := House{Kitchen{10}, 3} //to initialize you have to use composed type name.
    fmt.Println("House h has this many rooms:", h.numOfRooms) //numOfRooms is a field of House
    fmt.Println("House h has this many plates:", h.numOfPlates) //numOfPlates is a field of anonymous field Kitchen, so it can be referred to like a field of House
    fmt.Println("The Kitchen contents of this house are:", h.Kitchen) //we can refer to the embedded struct in its entirety by referring to the name of the struct type
}
```
```bash
House h has this many rooms: 3
House h has this many plates: 10
The Kitchen contents of this house are: {10}
```

1. Note is that since we have defined Kitchen to be an anonymous field, it allows us to access its members as if they were members of the encompassing class. 

2. Note is that the composed field is still available to be accessed, but by its type name. So in this case the anonymous field for Kitchen has to be accessed as h.Kitchen. If you want to print the number of plates in the kitchen, then do this: 
`fmt.Println(h.Kitchen.numOfPlates)`.

1. Note is how we had to use the type name when initializing the values as we did: h := House{Kitchen{10}, 3}. So h := House{{10}, 3} and h := House{10, 3} will cause compilation errors.

## Anonymous fields - when naming conflicts arise
What happens when more than one of the composed structs or the composing struct has the same field name. If there is a field in an outer struct with the same name as a field in an inner anonymous struct, then `the outer one is accessible by default`. In the below example, since House is the outer struct, its numOfLamps hides Kitchen’s. If you still require to access the Kitchen’s numOfLamps, that is possible by referring to it via the type name: `h.Kitchen.numOfLamps`.

```Go
package main

import "fmt"

type Kitchen struct {
    numOfLamps int
}

type House struct {
    Kitchen
    numOfLamps int
}

func main() {
    h := House{Kitchen{2}, 10} //kitchen has 2 lamps, and the House has a total of 10 lamps
    fmt.Println("House h has this many lamps:", h.numOfLamps) //this is ok - the outer House's numOfLamps hides the other one.  Output is 10.
    fmt.Println("The Kitchen in house h has this many lamps:", h.Kitchen.numOfLamps) //we can still reach the number of lamps in the kitchen by using the type name h.Kitchen
}
```
```bash
House h has this many lamps: 10
The Kitchen in house h has this many lamps: 2
```
But there is no rule when the fields are at the same level of composition - which means that when it occurs you need to resolve it yourself.

In the code below, both the Kitchen and the Bedroom have a field numOfLamps. Now if we referred to House.numOfLamps, the Go compiler cannot resolve whether you are referring to the numOfLamps within Kitchen or that within Bedroom and it throws an error.

```Go
package main

import "fmt"

type Kitchen struct {
    numOfLamps int
}

type Bedroom struct {
    numOfLamps int
}

type House struct {
    Kitchen
    Bedroom
}

func main() {
    h := House{Kitchen{2}, Bedroom{3}} //kitchen has 2 lamps, Bedroom has 3 lamps
    fmt.Println("Ambiguous number of lamps:", h.numOfLamps) //this is an error due to ambiguousness - is it Kitchen.numOfLamps or Bedroom.numOfLamps
}
```
```bash
Compiler error
8g -o _go_.8 structs2.go
structs2.go:20: ambiguous DOT reference House.numOfLamps
make: *** [_go_.8] Error 1
```
To resolve this, you will have to refer to the required fields explicitly via the type name of the anonymous field.

```Go
package main

import "fmt"

type Kitchen struct {
    numOfLamps int
}

type Bedroom struct {
    numOfLamps int
}

type House struct {
    Kitchen
    Bedroom
}

func main() {
    h := House{Kitchen{2}, Bedroom{3}}
    fmt.Println("House h has this many lamps:", h.Kitchen.numOfLamps + h.Bedroom.numOfLamps) //refer to fields via type name
}
```
```Bash
House h has this many lamps: 5
```