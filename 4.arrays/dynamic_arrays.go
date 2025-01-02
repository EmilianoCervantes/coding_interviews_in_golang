package main

import "fmt"

/*
*
* In other languages, like C, C++, Java, arrays have a fixed size.
* In those languages you have to instantiate a new array with a new size and copy the elements from the old array to the new one.
* In Go, arrays have a fixed size while slices are dynamic.
* Slices and append allow us in Go to expand the size of the slice without needing to create a new one.
Slices are the dynamic arrays in Go.
*/
func dynamicArrays() {
	array := [5]int{1, 2, 3}
	// I can still add other 2 numbers
	array[3] = 8
	array[4] = 9
	// But I cannot add a 6th number
	// array[5] = 0 // result --> invalid argument: index 5 out of bounds [0:5]compiler(InvalidIndex)
	fmt.Println(array) // [1 2 3 8 9]

	slice := []int{}
	// slice[0] = 1 // This will throw "panic: runtime error: index out of range [0] with length 0"
	fmt.Println(len(slice)) // 0

	// We use append to add elements in our "dynamic array" aka slice
	slice = append(slice, 1)
	fmt.Println("Slice:", slice, "with length:", len(slice)) // Slice: [1] with length: 1

	// You could think of doing
	array2 := [1]rune{'a'}
	// array2 = [2]rune{'a', 'b'} // result --> cannot use [2]rune{…} (value of type [2]rune) as [1]rune value in assignment
	// Because the variable/array was already defined with a size of 1

	// Another thing you might think of doing is
	// array2 = append(array2, 'b')
	// This has 2 issues:
	// result --> first argument to append must be a slice; have array2 (variable of type [1]rune)compiler(InvalidAppend)
	// So we can try:
	// array2 = append([]rune{'a'}, 'b') // result --> cannot use append([]rune{…}, 'b') (value of type []rune) as [1]rune value in assignment compiler(IncompatibleAssign)
	// Because once again, during the variable initialization it was declared as an array of length 1
	fmt.Println(array2)
}
