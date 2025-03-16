package main

import (
	"math/rand"
	"time"
)

func QuicksortNaive(slice []string) []string {
	if len(slice) < 2 {
		return slice
	}

	pivot := slice[0]

	var lower, middle, higher []string

	for _, value := range slice {
		if value < pivot {
			lower = append(lower, value)
		} else if value > pivot {
			higher = append(higher, value)
		} else {
			middle = append(middle, value)
		}
	}

	lower = QuicksortNaive(lower)
	higher = QuicksortNaive(higher)

	return append(append(lower, middle...), higher...)
}

func QuicksortLomuto(slice []string, start, end int) {
	if start >= end {
		return
	}

	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)
	pIndex := r.Intn(end-start) + start
	slice[start], slice[pIndex] = slice[pIndex], slice[start]
	pivot := slice[start]

	pointer := start

	for i := start + 1; i <= end; i += 1 {
		if slice[i] < pivot {
			pointer += 1

			if i != pointer {
				slice[i], slice[pointer] = slice[pointer], slice[i]
			}
		}
	}

	slice[start], slice[pointer] = slice[pointer], slice[start]

	QuicksortLomuto(slice, start, pointer-1)
	QuicksortLomuto(slice, pointer+1, end)
}

func QuicksortHoare(slice []string, start, end int) {
	if start >= end {
		return
	}

	source := rand.NewSource(time.Now().UnixNano())
	r := rand.New(source)
	pIndex := r.Intn(end-start) + start
	slice[start], slice[pIndex] = slice[pIndex], slice[start]
	pivot := slice[start]

	leftPointer := start + 1
	rightPointer := end

	for leftPointer <= rightPointer {
		if slice[leftPointer] < pivot {
			leftPointer += 1
		} else if slice[rightPointer] > pivot {
			rightPointer -= 1
		} else {
			slice[leftPointer], slice[rightPointer] = slice[rightPointer], slice[leftPointer]
			leftPointer += 1
			rightPointer -= 1
		}
	}

	slice[start], slice[rightPointer] = slice[rightPointer], slice[start]

	QuicksortHoare(slice, start, rightPointer-1)
	QuicksortHoare(slice, rightPointer+1, end)
}

// func main() {
// 	slice := []string{"b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"}

// 	// result := QuicksortNaive(slice)

// 	// fmt.Printf("Quicksort - Naïve Approach Result: %v\n", result)

// 	// QuicksortLomuto(slice, 0, len(slice)-1)

// 	// fmt.Printf("Quicksort - Lomuto's Approach Result: %v\n", slice)

// 	QuicksortHoare(slice, 0, len(slice)-1)

// 	fmt.Printf("Quicksort - Hoare's Approach Result: %v\n", slice)
// }
