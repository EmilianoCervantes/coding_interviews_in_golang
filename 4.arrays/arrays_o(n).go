package main

import (
	"fmt"
	"slices"
)

func mainBigO() {
	/**
	 * This is a language thing:
	 * In Go, arrays have a fixed size while slices are dynamic, but they are pretty similar otherwise.
	 * So most of the time you'll be working with slices.
	 * [Check these examples for more information](https://github.com/EmilianoCervantes/go-learnings/blob/main/1-go-101/3-collections/collections.go)
	 */

	// This is a slice
	alphabet := []string{"a", "b", "c", "d", "e"}

	// Basic access to elements in a slice
	firstLetter := alphabet[0]              // O(1)
	lastLetter := alphabet[len(alphabet)-1] // O(1)

	fmt.Println("First letter:", firstLetter)
	fmt.Println("Last letter:", lastLetter)

	// Push - add a new element at the end
	alphabet = append(alphabet, "f") // O(n) or O(1)?
	// Append is usually O(1) as it is just adding a new element
	// For Go's append(), it is amortized O(1). It depends on if it has to copy all elements which would make it O(n).
	// Check the `Resources` section of this module for more information.
	fmt.Println("Push alphabet:", alphabet)

	// Pop - remove the last element from the slice
	alphabet = alphabet[:len(alphabet)-1] // O(n) - as we are creating a new slice
	fmt.Println("Pop alphabet:", alphabet)

	// Unshift - add a new element at the beginning
	// Another language thing, in Go you can't unshift a slice, you need to create a new one
	// and the function `append` takes a `slice` as the 1st argument, not just an element
	// See more at https://go.dev/play/p/wNgO9LeX514
	alphabet = append([]string{"z"}, alphabet...) // O(n) - as we are creating a new slice
	fmt.Println("Unshift alphabet:", alphabet)

	// Shift - remove the first element from the slice
	// [n:] is not exclusive to Go, you can see it in other languages, like Python
	alphabet = alphabet[1:] // O(n) - as we are creating a new slice
	fmt.Println("Shift alphabet:", alphabet)

	// Insert - add a new element at any position within the slice
	alphabet = slices.Concat(alphabet[:3], []string{"w"}, alphabet[3:])
	fmt.Println("Insert alphabet:", alphabet)
}
