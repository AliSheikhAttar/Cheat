package main

// import (
// 	"fmt"
// 	"runtime"
// 	"time"
// )

// func allocateMemory() {
// 	// Creating a slice of 1 million integers
// 	numbers := make([]int, 1_000_000)
// 	for i := 0; i < len(numbers); i++ {
// 		numbers[i] = i
// 	}
// 	// The slice goes out of scope after this function ends
// 	fmt.Println("Finished allocating memory")
// }

// func main() {
// 	// Print memory stats before allocation
// 	var memStats runtime.MemStats
// 	runtime.ReadMemStats(&memStats)
// 	fmt.Printf("Before allocation: Alloc = %v KB\n", memStats.Alloc/1024)

// 	allocateMemory()

// 	runtime.ReadMemStats(&memStats)
// 	fmt.Printf("After allocation Before GC : Alloc = %v KB\n", memStats.Alloc/1024)

// 	// Trigger garbage collection manually (usually not recommended)
// 	runtime.GC()

// 	// Print memory stats after allocation and garbage collection
// 	runtime.ReadMemStats(&memStats)
// 	fmt.Printf("After allocation After GC: Alloc = %v KB\n", memStats.Alloc/1024)

// 	// Let GC work in the background
// 	time.Sleep(2 * time.Second)
// }
