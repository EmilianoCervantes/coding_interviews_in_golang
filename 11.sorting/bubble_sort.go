package main

/**
func BubbleSort(input []string) []string {
	for i from 0 to n-1 {
		for j in n-1 down to i+1 {
			if input[j-1] > input[j] {
				Swap: input[j-1], input[j]
			}
		}
	}
	return input
}
*/

func BubbleSort(input []string) []string {
	for i := range input {
		for j := len(input) - 1; j > i; j -= 1 {
			if input[j] < input[j-1] {
				input[j], input[j-1] = input[j-1], input[j]
			}
		}
	}
	return input
}

// func main() {
// 	input := []string{"b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"}

// 	sorted := BubbleSort(input)

// 	fmt.Printf("Bubble Sort Result: %v\n", sorted)
// }
