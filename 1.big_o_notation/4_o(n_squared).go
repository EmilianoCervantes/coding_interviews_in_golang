package main

/**
 * Different terms for inputs
 * 		- O(n + m) with + for steps in order
 * 		- O(n * n) with * for nested steps
 */
func OofNSquared() {
	numbers := []int{1, 2, 2, 3, 4, 5, 6, 6} // O(1)

	for i := 0; i < len(numbers); i++ { // O(1 + n) - O(n)
		for j := 1; j < len(numbers); j++ { // nested O(n * n) = O(n^2)
			if numbers[i] == numbers[j] { // O(n^2 * 1) = O(n^2)
				println(numbers[i]) // O(n^2 + 1) = O(n^2)
			}
		}
	}
}
