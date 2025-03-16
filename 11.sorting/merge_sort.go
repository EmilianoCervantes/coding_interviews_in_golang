package main

func MergeSortHelper(input []string) []string {
	// Base case - nothing else to divide
	if len(input) < 2 {
		return input
	}

	// Divide array in halves
	middle := len(input) / 2

	leftRes := MergeSortHelper(input[:middle])
	rightRes := MergeSortHelper(input[middle:])

	left, right := 0, 0
	helperArr := []string{}

	for left < len(leftRes) && right < len(rightRes) {
		// Note: in case of a sort twice,
		// E.g. Sorting a table by any criteria
		// AND THEN sorting AGAIN by name,
		// "<=" will allow to preserve the previous criteria,
		// While also keeping the order by name.
		if leftRes[left] <= rightRes[right] {
			helperArr = append(helperArr, leftRes[left])
			left += 1
		} else {
			helperArr = append(helperArr, rightRes[right])
			right += 1
		}
	}

	helperArr = append(helperArr, leftRes[left:]...)
	helperArr = append(helperArr, rightRes[right:]...)

	return helperArr
}

func MergeSort(input []string) []string {
	input = MergeSortHelper(input)

	return input
}

// func main() {
// 	input := []string{"b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"}

// 	sorted := MergeSort(input)

// 	fmt.Printf("Merge Sort Result: %v\n", sorted)
// }
