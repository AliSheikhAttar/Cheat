package main

import (
	"fmt"
	"runtime"
	"time"
)

func allocateMemory() {
	for i := 0; i < 10; i++ {
		_ = make([]int, 1_000_000_000)    // Allocate a large slice
		time.Sleep(60 * time.Millisecond) // Simulate work
	}
	fmt.Println("Finished allocating memory")
}

func main() {
	go func() {
		for {
			time.Sleep(500 * time.Millisecond)
			fmt.Println("Program is still running...")
		}
	}()

	go allocateMemory()

	for i := 0; i < 5; i++ {
		var memStats runtime.MemStats
		runtime.ReadMemStats(&memStats)
		fmt.Printf("Alloc = %v KB, GC Cycles = %v\n", memStats.Alloc/1024, memStats.NumGC)
		time.Sleep(1 * time.Second)
	}

	fmt.Println("Main program finished")
}
