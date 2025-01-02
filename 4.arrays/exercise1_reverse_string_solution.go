package main

import (
	"fmt"
	"strings"
)

/**
 * Given a certain string, return it backwards.
 */

// Step 1 - I would expect a string as a param and return another string
// In Go, because we have strict types, I won't worry about having something else being passed other than a string
// Things I might worry about though are special+escape characters, but I'll get to that later
func ReverseAStringSolution(str string) string { // Time complexity is O(n)
	reversedString := ""

	// Step 2 - if we have only 1 letter or the string is empty, we don't need to do any operations
	if len(str) < 2 {
		return str
	}

	// Step 3 - go over the string letter by letter
	// Note: you might think of doing this:
	for _, currentRune := range str { // Time complexity is O(n)
		fmt.Println(currentRune) // You'll get a rune - H: 72, h: 104
		// As you code in your interview, it is a good tip to see you're getting the results as expected step by step
		// Back on topic, str[index] or with this type of for we get a rune
		// Step 3 - [Using strconv.QuoteRune](https://stackoverflow.com/questions/39245610/golang-converting-from-rune-to-string)
		char := string(currentRune)
		fmt.Println(char) // Printing is important cause using strconv.QuoteRune(currentRune) would create a different result

		reversedString = char + reversedString
	}

	// Finally, return the string backwards
	return reversedString
}

// What will happen with the next examples:
// ReverseAStringSolution("Hi you")
// ReverseAStringSolution("Hey\tyou there")

// Step 1 - Let's say I expect a pointer as a param and return another string
// Why a pointer? That way we can enable people calling this function to pass an "optional" value.
func ReverseAStringSolution2(str *string) string {
	reversedString := ""

	if str == nil {
		return ""
	}

	if len(*str) < 2 {
		return *str
	}

	for _, currentRune := range *str { // Time complexity is O(n)
		fmt.Println(currentRune) // You'll get a rune - H: 72, h: 104
		// As you code in your interview, it is a good tip to see you're getting the results as expected step by step
		// Back on topic, str[index] or with this type of for we get a rune
		// Step 3 - [Using strconv.QuoteRune](https://stackoverflow.com/questions/39245610/golang-converting-from-rune-to-string)
		char := string(currentRune)
		fmt.Println(char) // Printing is important cause using strconv.QuoteRune(currentRune) would create a different result

		reversedString = char + reversedString
	}

	return reversedString
}

// Step 1 - Let's say I expect a pointer as a param and return another string
func ReverseTheWordsSolution(text *string) string {
	reversedText := ""

	if text == nil {
		return ""
	}

	// Step 2 - let's split the string by spaces.
	arrWords := strings.Fields(*text)

	// Join the separated strings backwards
	for _, word := range arrWords {
		reversedText = word + " " + reversedText
	}

	// Return the reversed text
	return reversedText
}
