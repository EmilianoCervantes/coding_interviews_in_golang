package main

import "fmt"

func OofN() {
	testSlice := []string{}

	/**
	 * This algorithm has a time complexity of O(n) because it has to iterate through the entire array to find the string
	 * The n in O(n) represents the number of elements in the array
	 * The time taken by the function is directly proportional to the number of elements in the array
	 * In other words, linear time complexity
	 * As the number of elements in the array increases, the time taken by the function also increases LINEARLY.
	 */
	for i := 0; i < len(testSlice); i++ {
		if testSlice[i] == "anything" {
			fmt.Println("Found it")
		}
	}
}
