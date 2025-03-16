package main

// Heapify function to maintain the heap property
func heapify(arr []int, currIndex, lenToCover int) {
	indexLargest := currIndex // Lets see which element is the largest
	//  Children are i*2 and i*2+1
	// Check both sides and pick the largest
	leftChildIndex := currIndex*2 + 1 // E.g. 0*2 = 0 + 1 = 1
	rightChildIndex := currIndex*2 + 2

	// Remember: '<' error for IndexError: list index out of range
	// Validation in case parent doesn't have a right children
	if rightChildIndex < lenToCover && arr[rightChildIndex] > arr[indexLargest] {
		indexLargest = rightChildIndex
	}
	// "left_child_index < len_to_cover" is needed because we are going to do this check recursively
	if leftChildIndex < lenToCover && arr[leftChildIndex] > arr[indexLargest] {
		indexLargest = leftChildIndex
	}

	if indexLargest != currIndex {
		arr[currIndex], arr[indexLargest] = arr[indexLargest], arr[currIndex]
		heapify(arr, indexLargest, lenToCover)
	}
}

func HeapSort(arr []int) {
	// First Build the Max-Heap
	// Parents are n/2
	// First parent
	startIndex := len(arr) / 2
	for i := startIndex; i >= 0; i -= 1 {
		heapify(arr, i, len(arr))
	}

	// Max-Heap is done
	// Next sort it
	for i := len(arr) - 1; i > -1; i -= 1 {
		// Swap max element with last element
		// Review the Readme#in-place-heap-sort for more.
		arr[0], arr[i] = arr[i], arr[0]
		heapify(arr, 0, i)
	}
}

// func main() {
// 	arr := []int{5, 8, 3, 9, 4, 1, 7}
// 	HeapSort(arr)
// 	fmt.Println("Heap Sort Result:", arr)

// 	arr = []int{4, 2, 8, 7, 1, 3, 5, 6}
// 	HeapSort(arr)
// 	fmt.Println("Heap Sort Result:", arr)
// }
