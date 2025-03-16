package solvingcodingproblems

import "errors"

// Based on [How to: Work at Google — Example Coding/Engineering Interview](https://youtu.be/XKu_SEDAykw)

// Given 2 arrays, create a function that let's a user know (true/false) whether these two arrays contain any common items

// For example:
// 1) ['a', 'b', 'c', 'x']
// 2) ['z', 'y', 'i']

// Example 2:
// 1) ['a', 'b', 'c', 'x']
// 2) ['z', 'y', 'x']

/**
 * This is the actual code
 */
func InterviewExampleSolutionCode(array1, array2 []rune) bool {
	// Let's assume the arrays are sorted --> Which was one of the questions we asked
	// array1 := ['a', 'b', 'c', 'x']
	// array2 := ['x', 'y', 'z']

	// We can prob go over each index based on 'a' < 'b' = true
	i, j := 0, len(array2)-1
	// For those unfamiliar, [this is a while in Go]((https://go.dev/tour/flowcontrol/3)
	for i < len(array1) && j >= 0 {
		letterFirstArray := array1[i]
		letterSecondArray := array2[j]

		if letterFirstArray == letterSecondArray {
			return true
		} else if letterFirstArray < letterSecondArray {
			i++
		} else {
			j--
		}
	}

	return false

	// What is the time complexity of your solution?
	// O(n+m) --> =O(n) + O(m) = O(n)

	// So, did we do better than O(n²)? - Yes
}

func InterviewExampleSolutionCode2(array1, array2 []rune) (rune, error) {
	// Let's assume the arrays are NOT sorted
	// We cannot go with the previous approach

	// For:
	// array1 := []rune{'a', 'b', 'c', 'x'}
	// array2 := []rune{'z', 'y', 'x'}
	// What can we do?

	// Let's use a hash table to store the values - prob O(n) and search with Θ(1)
	mapArray1 := make(map[rune]bool) // We can either do map[string]string or map[string]bool - personally I think it is the same, it is more around your taste OR let me know if you see improvements with either version
	// At the end of the day, we just want know if the record/entry exists
	for _, letter := range array1 {
		mapArray1[letter] = true
	}

	// Let's loop through the second array and check if the value exists in the map
	for _, letter := range array2 {
		if mapArray1[letter] {
			return letter, nil
		}
	}

	return 0, errors.New("no common items found")
	// What is the time complexity of your solution?
	// O(n+m) --> =O(n) + O(m) = O(n)
}
