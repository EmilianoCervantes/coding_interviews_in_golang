package main

/**
 * Description:
 * Given 2 sorted arrays
 * Merge them and keep the resulting array sorted
 */

// Step 1: accept 2 arrays
/** What kind of arrays do we take?
 * - Usually you get an example and you can ask if you can assume the arrays will be of that type.
 * - Ex: [0,3,4,31] and [4,6,30]
 * - And based on the description, we want to return a sorted array
 */
func MergeSortedArraysSolution(arr1, arr2 []int) []int {
	// Let's create a slice that we will return
	sortedResult := []int{}

	// We don't know the length of each array, either could be smaller than the other
	// So let's just traverse through the first array
	// What I'll do next is compare number by number between the arrays
	// and insert them in the new array based on which number is smaller
	// For that I'll need an extra pointer to know which position I'm pointing at in the second array
	arr1Position := 0
	arr2Position := 0

	// What happens in any of those 2 arrays is empty?
	// Then the for will never happen
	if len(arr1) < 1 {
		return arr2
	} else if len(arr2) < 1 {
		return arr1
	}

	for arr1Position < len(arr1) && arr2Position < len(arr2) { // O(n+m)
		valueArr1 := arr1[arr1Position]
		valueArr2 := arr2[arr2Position]
		if valueArr1 < valueArr2 { // 0 is less than 4
			sortedResult = append(sortedResult, valueArr1)
			arr1Position++

			// Note: we could simplify the last 2 elses, how and why?
		} else if valueArr1 > valueArr2 { // When 6 is less than 31
			sortedResult = append(sortedResult, valueArr2)
			arr2Position++
		} else { // When 4 == 4
			sortedResult = append(sortedResult, valueArr1)
			sortedResult = append(sortedResult, valueArr2)
			arr1Position++
			arr2Position++
		}

		// Now what happens if len(arr1) > len(arr2) ?
		// That means we no longer have anything to compare
		// We cans skip to add the rest of the array #1 to the sorted results
		// I'll check this by seeing if we already reached the end of the array 2
		if arr2Position == len(arr2) {
			sortedResult = append(sortedResult, arr1[arr1Position:]...)
			break
		}

		// And if len(arr1) < len(arr2)
		// This means we didn't finish adding the values of arr2
		// We will add the rest of the array #2 to the sorted results
		if arr1Position == len(arr1) {
			sortedResult = append(sortedResult, arr2[arr2Position:]...)
		}
	}

	return sortedResult
}
