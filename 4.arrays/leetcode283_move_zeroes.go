package main

/**
 * LEETCODE PROBLEM #283
 *
 * Description Directly from: https://leetcode.com/problems/move-zeroes/
 *
 * Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
 * Note that you must do this in-place WITHOUT making a copy of the array.
 *
 * Example 1:
 * Input: nums = [0,1,0,3,12]
 * Output: [1,3,12,0,0]
 *
 * Example 2:
 * Input: nums = [0]
 * Output: [0]
 *
 * Constraints:
 * 1 <= nums.length <= 10^4
 * -2^31 <= nums[i] <= 2^31 -1
 */

// Trying to move zeroes while keeping the order means I cannot move one zero all the way to the back
// I have to move it place by place
// If I encounter other zeroes, do I move them together?
// Or one by one?
// How do I keep track of the zeroes I left along the way?

// Solution 1:
func MoveZeroesInitialThinking(nums []int) {
	for i := 0; i < len(nums)-1; i++ {
		// I wanna see if I'm looking at a zero or not
		// [0,1,0,2]

		// If I'm looking at a zero, I wanna know if I need to swap it with the next value
		// nums[i] = 0

		// If the next number is not a 0 I'll swap it
	}

	// BUT there are a few issues

	// Essentially, I would end up with O(n^2) and it is not what I want
}

// NOW...
// What if instead of moving the zeroes, we moved the other numbers?
func MoveZeroesSolution1(nums []int) { // QUESTION AT THE END OF THE FOR LOOP
	// Same as before, I wanna see if I'm looking at a zero or not
	// [2,0,0,0,1]
	// [0,0,0,2]

	// If I'm NOT looking at a zero, I won't touch it
	// If I am looking at a zero, I'll just keep track of it until I encounter a different number
	pointer1 := 0 // will help me check where I left the last zero
	pointer2 := 0 // will keep track of where I'm at
	encounteredAZero := false

	for pointer2 < len(nums) {
		currValue := nums[pointer2]

		// I found a zero
		if currValue == 0 {
			encounteredAZero = true
			pointer2++
		} else { // This is not a zero
			if encounteredAZero { // I'll wait until I see no more zeroes
				nums[pointer1] = currValue
				nums[pointer2] = 0
				pointer1++          // Move one place after the first 0 was encountered
				pointer2 = pointer1 // Starting from that position
				encounteredAZero = false
			} else { // No zeroes so far
				pointer1++
				pointer2++
			}
		}
	} // Is this O(n) or O(n^2)
}

// Now, there is an easier way, IT IS SIMILAR to solution 1
// I was just overcomplicating things
func MoveZeroesSol2(nums []int) {
	// If I'm looking at a zero, I won't do a thing
	// If I am looking at a number, either I want to swap it with a zero
	// And if there are no zeros, I'll just move my pointer to the right one place
	pointer1 := 0 // will help me check where I left the last zero

	for i := 0; i < len(nums); i++ {
		currValue := nums[i]

		// I found a zero
		if currValue == 0 {
			// Let's not do anything
		} else { // I found a value that is not zero
			if nums[pointer1] == 0 {
				nums[pointer1] = currValue
				nums[i] = 0
				pointer1++
			} else {
				// Whenever there's a number that is not 0, let's move pointer 1 to the right
				pointer1++
			}
		}
	}
}

func MoveZeroesSolShort(nums []int) {
	pointer1 := 0 // will help me check where I left the last zero

	for i := 0; i < len(nums); i++ {
		currValue := nums[i]

		// I found a value that is not zero
		if currValue != 0 {
			if nums[pointer1] == 0 {
				nums[pointer1] = currValue
				nums[i] = 0
			}

			// And either way, because I found a non-zero value, I'll move my pointer to the right
			pointer1++
		}
	}
} // THIS IS O(n) and at least at the time of submission, it beat 100% of people in Go in Leetcode!

// case1 := []int{0, 0, 0, 2}
// case2 := []int{0, 1, 0, 3, 12}
// case3 := []int{4, 2, 4, 0, 0, 3, 0, 5, 1, 0}
// MoveZeroes(case1)
