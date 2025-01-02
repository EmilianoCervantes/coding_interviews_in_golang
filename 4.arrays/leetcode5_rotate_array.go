package main

import "slices"

/**
 * LEETCODE PROBLEM #189
 *
 * Description Directly from: https://leetcode.com/problems/rotate-array/description/
 *
 * Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
 *
 * Example 1:
 * Input: nums = [1,2,3,4,5,6,7], k = 3
 * Output: [5,6,7,1,2,3,4]
 * Explanation:
 * rotate 1 steps to the right: [7,1,2,3,4,5,6]
 * rotate 2 steps to the right: [6,7,1,2,3,4,5]
 * rotate 3 steps to the right: [5,6,7,1,2,3,4]
 *
 * Example 2:
 * Input: nums = [-1,-100,3,99], k = 2
 * Output: [3,99,-1,-100]
 * Explanation:
 * rotate 1 steps to the right: [99,-1,-100,3]
 * rotate 2 steps to the right: [3,99,-1,-100]
 *
 * Constraints:
 * 1 <= nums.length <= 10^5
 * -2^31 <= nums[i] <= 2^31 -1
 * 0 <= k <= 105
 */

// Leetcode challenge us to do it with SPACE OF O(1)!
func RotateForLoop(nums []int, k int) {
	if len(nums) < 2 {
		return
	}

	// First of all, k being greater than nums[] doesn't mean there is nothing to rotate
	// We could rotate [1,2] n number of times... I know

	// Maybe this involves some math? Actually no, there is a way without a for loop

	// We could do a for loop for i<k to pop and unshift - that's sol #1

	numsLen := len(nums) - 1

	for i := 0; i < k; i++ {
		// First I wanna know the last element in the list
		currentLast := nums[numsLen]

		// Then I'll remove it from the array -> pop
		nums = nums[:numsLen]

		// And finally, add it at the beginning -> unshift
		nums = append([]int{currentLast}, nums...)
	}
}

func RotateSolution2(nums []int, k int) {
	// Nothing to rotate
	if len(nums) < 2 {
		return
	}

	separation := len(nums) - k
	// Either of the next 2 lines does the trick
	nums = append(nums[separation:], nums[:separation]...)
	nums = slices.Concat(nums[separation:], nums[:separation])
}
