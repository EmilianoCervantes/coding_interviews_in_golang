package main

/**
 * LEETCODE PROBLEM #217
 *
 * Description Directly from: https://leetcode.com/problems/contains-duplicate/description/
 *
 * Given an integer array nums, return the first duplicated number for the first value that appears at least twice in the array, and return false if every element is distinct.
 *
 * Example 1:
 * Input: nums = [1,2,3,1]
 * Output: 1
 * Explanation:
 * The element 1 occurs at the indices 0 and 3.
 *
 * Example 2:
 * Input: nums = [1,2,3,4]
 * Output: null
 * Explanation:
 * All elements are distinct
 *
 * Example 3:
 * Input: nums = [1,1,1,3,3,4,3,2,4,2]
 * Output: 1
 *
 * Constraints:
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 */

// This solution ONLY beats 22.63%! of solutions!!
// How would you improve on this?
// Hint: same problem in case you skipped the arrays section. Remember in the sorting section you'll find a way to improve on this.
func ContainsDuplicate(nums []int) (int, bool) { // O(n)
	if len(nums) < 2 {
		return 0, false
	}

	numbers := make(map[int]int)

	for _, value := range nums {
		_, ok := numbers[value]

		if ok {
			return value, true
		} else {
			numbers[value] = value
		}
	}

	return 0, false
}
