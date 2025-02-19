package main
import "fmt"

// > An array or struct type T may not have an element of type T, or of a type containing T as a component, directly or indirectly, if those containing types are only array or struct types.

// invalid array types
type (
	T11 [10]T11                // element type of T1 is T1
	T21 [10]struct{ f T21 }     // T2 contains T2 as component of a struct
	T31 [10]T41                 // T3 contains T3 as component of a struct in T4
	T41 struct{ f T31 }         // T4 contains T4 as component of array T3 in a struct
)

// valid array types
type (
	T51 [10]*T51                // T5 contains T5 as component of a pointer
	T61 [10]func() T61          // T6 contains T6 as component of a function type
	T71 [10]struct{ f []T71 }   // T7 contains T7 as component of a slice in a struct
)


//  #################################

// Valid array types (with indirection)// T5: Array of pointers to T5
type T5 [10]*T5

// T6: Array of functions that return T6
type T6 [10]func() T6

// T7: Array of structs containing a slice of T7
type T7 [10]struct{ f []T7 }




// Valid array types (with indirection)// T5: Array of pointers to T5
type T5 [10]*T5

// T6: Array of functions that return T6
type T6 [10]func() T6

// T7: Array of structs containing a slice of T7
type T7 [10]struct{ f []T7 }





func main() {
	// Example using T5 (Array of pointers)

	// Create a T5 instance.  Initially, all pointers are nil.
	var arrT5 T5
	fmt.Println("Initial arrT5:", arrT5)	// Create another T5 instance.
	var anotherT5 T5

	// Set the first element of arrT5 to point to anotherT5.
	arrT5[0] = &anotherT5
	fmt.Println("arrT5 after setting element 0:", arrT5)	// Demonstrate that we can access the pointer.
	if arrT5[0] != nil {
		fmt.Println("arrT5[0] is not nil")
		// Note:  We can't directly dereference and modify *arrT5[0]
		// without risking a panic, as it currently points to an
		// uninitialized T5.  To do more, we'd need to initialize
		// the elements of anotherT5.
	}

	// Example using T6 (Array of functions)

	// Create a T6 instance.
	var arrT6 T6
	fmt.Println("Initial arrT6:", arrT6) // Prints the zero value (function addresses will be nil)

	// Define a function that returns a T6.
	makeT6 := func() T6 {
		return T6{} // Return a zero-valued T6
	}

	// Assign this function to the first element of arrT6.
	arrT6[0] = makeT6
	fmt.Println("arrT6 after setting element 0:", arrT6) // Will now show a non-nil function address

	// Call the function.
	if arrT6[0] != nil {
		returnedT6 := arrT6[0]()
		fmt.Println("Returned T6 from arrT6[0]:", returnedT6) // Prints the zero value of T6
	}

	// Example using T7 (Array of structs with slices)

	// Create a T7 instance.
	var arrT7 T7
	fmt.Println("Initial arrT7:", arrT7)

	// Append a zero-valued T7 to the slice in the first element.
	arrT7[0].f = append(arrT7[0].f, T7{})
	fmt.Println("arrT7 after appending to slice in element 0:", arrT7)

	// Append another T7 to the slice.
	arrT7[0].f = append(arrT7[0].f, T7{})
	fmt.Println("arrT7 after appending again:", arrT7)

	// Access the length of the slice.
	fmt.Println("Length of slice in arrT7[0]:", len(arrT7[0].f))

	// Create a second T7 and add it to the slice of the *second* element.
	var anotherT7 T7
	arrT7[1].f = append(arrT7[1].f, anotherT7)
	fmt.Printf("arrT7 after adding to slice in element 1: %+v\n", arrT7) //Use %+v for struct details
}