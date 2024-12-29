package main

func aFunction() {}

// What is the Big O of the below function?

// The Big O of the function is O(n)
// You could say we have O(1)+O(1)+O(n) which is simplified to O(n)
// O(1)+O(1)+O(n)
// O(2)+O(n)
// O(n)

/**
 * Rules of Big O
 * 1. Worst Case
 * 2. Remove Constants
 * 3. Different terms for inputs
 * 		- O(n + m) with + for steps in order
 * 		- O(n * n) with * for nested steps
 * 4. Drop Non-Dominant terms
 */
func ChallengeSolution(input []string) int {
	a := 10    // O(1)
	a = 50 + 3 // O(1) - with the previous step it is O(1 + 1) = O(2)

	for i := 0; i < len(input); i++ { // O(n) - with the previous it is O(2 + n)
		aFunction()       // O(1 * n) with 1 for calling the function and n for the loop it is inside of so O(n) - (O 2 + n + n) = O(2 + 2n)
		stranger := true  // O(1 * n) -  O(2 + 2n + n) = O(2 + 3n)
		println(stranger) // O(1 * n) - O(2 + 4n)
		a++               // O(1 * n) - O(2 + 5n)
	}

	// Following the rules of Big O --> O(2 + 5n) = O(1 + 1n) = O(n) by removing constants and keeping the dominant term.

	return a
}
