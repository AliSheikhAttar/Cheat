# OOP
Go does not strictly support object orientation but is a lightweight object Oriented language. Object Oriented Programming in Golang is different from that in other languages like C++ or Java due to factors mentioned below:

1. Struct
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

2. Encapsulation
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

3. Inheritance
When a class acquires the properties of its superclass then we can say it is inheritance. Here, subclass/child class are the terms used for the class which acquire properties. For this one, one must use a struct to achieve inheritance in Golang. Here, users have to compose using structs to form the other objects.

4. Interfaces
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