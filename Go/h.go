package main

import (
	"fmt"
)

func describe(in interface{}){
	fmt.Printf("Type: %T, Value: %v \n",in, in)
}

func main(){
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
println("**********************")
[32]byte
[2*N] struct { x, y int32 }
[1000]*float64
[3][5]int
[2][2][2]float64  // same as [2]([2]([2]float64))
}