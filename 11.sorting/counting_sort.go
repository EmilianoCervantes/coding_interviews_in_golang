package main

import "fmt"

func CountingSort(arr []int) []int {
	m := map[int]int{}

	res := []int{}
	max := arr[0]
	min := arr[0]

	for _, num := range arr {
		// Remember to not use an if because the reference is NOT updated.
		// Anyways, in Go this works, so less lines either way.
		m[num] += 1

		if num < min {
			min = num
		}

		if num > max {
			max = num
		}
	}

	for num := min; num <= max; num += 1 {
		if repetitions, ok := m[num]; ok {
			for i := 0; i < repetitions; i += 1 {
				res = append(res, num)
			}
		}
	}

	return res
}

func main() {
	arr := []int{9, 6, 3, 5, 2, 1, 2}
	fmt.Println("Counting Sort Result:", CountingSort(arr))

	arr = []int{5, 8, 3, 9, 4, 1, 7}
	fmt.Println("Counting Sort Result:", CountingSort(arr))

	arr = []int{4, 2, 8, 7, 1, 3, 5, 6}
	fmt.Println("Counting Sort Result:", CountingSort(arr))
}
