package solvingcodingproblems

// Based on [How to: Work at Google — Example Coding/Engineering Interview](https://youtu.be/XKu_SEDAykw)

// Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items

// For example:
// 1) ['a', 'b', 'c', 'x']
// 2) ['z', 'y', 'i']

// Example 2:
// 1) ['a', 'b', 'c', 'x']
// 2) ['z', 'y', 'x']

/**
 * By solution I meant going through the problem and the logic of how to solve it.
 */
func InterviewExampleSolution(array1, array2 []string) bool {
	// What would be your questions before starting?
	// We can ask:
	// - Are the arrays sorted? - This can help us to optimize the solution
	// - What are the sizes of the arrays? - If they are always small, like even 1000 elements, we can say we will use a nested loop because it will be always the same time.
	// - Are the arrays of the same length? - If your initial solution is nested loops, it can either be O(n*m) or O(n²).
	// - What do we want to return if we find or not a common element?

	// What other issues can you think of?
	// Think of how can you "crash" the function - like passing nil arrays
	// But don't use too much time, the coding interview has a limited amount of time
	// BE mindful of your time!!!

	// How would you solve/code this problem?
	// What would be your first thinking - take 1 - at most 2 SECONDS to think about it
	// What did you come up with? - Maybe a nested loop

	for i := 0; i < len(array1); i++ {
		for j := 0; j < len(array2); j++ {
			if array1[i] == array2[j] {
				// We found a common element
				return true
			}
		}
	}

	return false

	// What is the time complexity of your solution?
	// O(n*m) - nested loops for different arrays
	// O(n²) - in the worst case scenario
}
