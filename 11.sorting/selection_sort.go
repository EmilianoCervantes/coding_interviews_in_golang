package main

// func SelectionSortPseudoCode(input: []string) []string{
//   For an initial i position we have the current minimum value
//
//   minValue = input[i] // We need to know the min value in the subarray
//   minIndex = i // What we actually keep track of

//   for current_subarray_index in i+1 to n-1:
//     if input[current_subarray_index] < minValue:
//       minValue = input[current_subarray_index]
//       minIndex = current_subarray_index
//
// 			 Swap: input[i], input[minIndex]
// }

func SelectionSort(input []string) []string {
	for i := range input {
		smallestPosition := i
		for j := i + 1; j < len(input); j++ {
			if input[j] < input[smallestPosition] {
				smallestPosition = j
			}
		}
		input[i], input[smallestPosition] = input[smallestPosition], input[i]
	}
	return input
}

// func main() {
// 	input := []string{"b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"}

// 	sorted := SelectionSort(input)

// 	fmt.Printf("Selection Sort Result: %v\n", sorted)
// }
