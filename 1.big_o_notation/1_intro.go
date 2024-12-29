package main

import (
	"fmt"
	"time"
)

func findString(slice []string) {
	for i := 0; i < len(slice); i++ {
		if slice[i] == "test" {
			fmt.Println("Found the string")
		}
	}
}

/**
 * NOTE: Go does't have a built-in function to measure the monotonic time since some unspecified starting point.
 * I'm going to use the time package to measure the time taken by the function.
 */
func main() {
	// Create a slice with 1000 elements
	start := time.Now()

	testSlice := []string{}
	fmt.Println(testSlice)

	findString(testSlice)

	// Measure the time taken by the function
	end := time.Now()
	elapsed := end.Sub(start) // But this is not an efficient way to measure the efficiency of any function

	// The time can vary between computers
	// It can even vary as you run it multiple times
	// So it is not a good way to measure the efficiency of any function
	fmt.Println("Time taken by the function: ", elapsed)

	// That is why we use O notation.
}
