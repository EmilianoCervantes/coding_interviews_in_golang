package main

import (
	"fmt"
)

func main() {
	/**
	 * This is a language thing:
	 * In Go, arrays have a fixed size while slices are dynamic.
	 * So most of the time you'll be working with slices.
	 * [Check these examples for more information](https://github.com/EmilianoCervantes/go-learnings/blob/main/1-go-101/3-collections/collections.go)
	 */

	// This is a slice
	// alphabet := []string{"a", "b", "c", "d", "e"}

	// // Basic access to elements in an array
	// firstLetter := alphabet[0]              // Big O?
	// lastLetter := alphabet[len(alphabet)-1] // Big O?

	// fmt.Println("First letter:", firstLetter)
	// fmt.Println("Last letter:", lastLetter)

	// // Push - add a new element at the end
	// alphabet = append(alphabet, "f") // Big O?
	// fmt.Println("Push alphabet:", alphabet)

	// // Pop - remove the last element from the array
	// alphabet = alphabet[:len(alphabet)-1] // Big O?
	// fmt.Println("Pop alphabet:", alphabet)

	// // Unshift - add a new element at the beginning
	// // Another language thing, in Go you can't unshift an array, you need to create a new one
	// // and the function `append` takes a `slice` as the 1st argument, not just an element
	// // See more at https://go.dev/play/p/wNgO9LeX514
	// alphabet = append([]string{"z"}, alphabet...) // Big O?

	// // Shift - remove the first element from the array
	// // [n:] is not exclusive to Go, you can see it in other languages, like Python
	// alphabet = alphabet[1:] // Big O?

	// // Insert - add a new element at any position within the slice
	// atIndex := 2
	// alphabet = slices.Concat(alphabet[:atIndex], []string{"w"}, alphabet[atIndex:])
	// fmt.Println("Insert alphabet:", alphabet)
	// fmt.Println()

	// str := "Hey\tyou there"
	// reversedString := ""

	// // Step 2 - go over the string letter by letter
	// for _, currentRune := range str {
	// 	// As you code in your interview, it is a good tip to see you're getting the results as expected step by step
	// 	// Back on topic, str[index] or with this type of for we get a rune
	// 	// Step 3 - [Using string](https://stackoverflow.com/questions/39245610/golang-converting-from-rune-to-string)
	// 	char := string(currentRune)

	// 	reversedString = char + reversedString
	// }

	// // Finally, return the string backwards
	// fmt.Println(reversedString)

	slice1 := []int{0, 3, 4, 31}
	slice2 := []int{4, 6, 30}
	fmt.Println(MergeSortedArraysSolution(slice1, slice2))
}
