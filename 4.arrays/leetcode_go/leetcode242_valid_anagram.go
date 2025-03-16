package main

import "sort"

/**
 * LEETCODE PROBLEM #242

 * Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 * Example 1:
 * Input: s = "anagram", t = "nagaram"
 * Output: true

 * Example 2:
 * Input: s = "rat", t = "car"
 * Output: false

 * Constraints:
 * 1 <= s.length, t.length <= 5 * 104
 * s and t consist of lowercase English letters.

 * Follow up: What if the inputs contain Unicode characters?
 * How would you adapt your solution to such a case?
 */

// Note: an alternative could be doing dictionaries and comparing keys and items per key

// Avoid code repetition
func sortStringHelper(text string) string {
	// Transform to runes which is chars for Go
	runes := []rune(text)
	sort.Slice(runes, func(i, j int) bool { return runes[i] < runes[j] })
	return string(runes)
}

func isAnagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	return sortStringHelper(s) == sortStringHelper(t)
}
