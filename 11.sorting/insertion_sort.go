package main

func InsertionSort(input []string) []string {
	for i := 1; i < len(input); i += 1 {
		currValue := input[i] // ith number

		// Review numbers until we find the spot where the ith number cannot go lower
		currLeftIndex := i - 1

		// The "currValue < left" condition allows to preserve the previous order
		// in case of sorting a table twice by diff criteria.
		for currLeftIndex > -1 && input[currLeftIndex] > currValue {
			// Moving the value to the right
			// Different from swapping
			input[currLeftIndex+1] = input[currLeftIndex]
			currLeftIndex -= 1
		}

		// Last spot before the number was too low
		input[currLeftIndex+1] = currValue
	}

	return input
}

// func main() {
// 	input := []string{"b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"}

// 	sorted := InsertionSort(input)

// 	fmt.Printf("Insertion Sort Result: %v\n", sorted)
// }
