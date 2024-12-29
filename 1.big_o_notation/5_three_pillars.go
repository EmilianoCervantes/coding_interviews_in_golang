package main

/**
 * Heap - where we store variables
 * And Stacks - where we keep track of function calls
 * Space complexity:
 * 	- Is caused by:
 * 		- Variables - Generally O(1)
 * 		- Data structures // Arrays, Objects, Hash tables - Generally O(n)
 * 		- Function calls
 * 		- Allocations
 */
func printElements(arr []int) { // O(1) - Space complexity
	// Why O(1) for space complexity?
	// Because we are NOT creating any new variables, data structures, etc.
	for i := 0; i < len(arr); i++ { // The only variable is i, which is O(1)
		println(arr[i])
	}
}

func fillWithHi(length int) []string { // O(n) - Space complexity
	hiArr := []string{} // O(n) - Space complexity

	for i := 0; i < length; i++ {
		hiArr = append(hiArr, "hi")
	}

	return hiArr
}

func CalculateSpaceExample() {
	printElements([]int{})
	fillWithHi(10)
}
