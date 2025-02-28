package main

/**
 * LEETCODE PROBLEM #1
 *
 * Description Directly from: https://leetcode.com/problems/two-sum/
 * Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
 * You may assume that each input would have exactly one solution, and you may not use the same element twice.
 * You can return the answer in any order.
 *
 * Example 1:
 * Input: nums = [2,7,11,15], target = 9
 * Output: [0,1]
 * Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 *
 * Example 2:
 * Input: nums = [3,2,4], target = 6
 * Output: [1,2]
 *
 * Example 3:
 * Input: nums = [3,3], target = 6
 * Output: [0,1]
 *
 * Constraints:
 * 2 <= nums.length <= 104
 * -10^9 <= nums[i] <= 10^9
 * -10^9 <= target <= 10^9
 * Only one valid answer exists.
 */
func TwoSum(nums []int, target int) []int { // O(n)
	// This is the indices I'll return at the end
	indices := []int{}

	// If I have less than 2 elements in the array, I cannot return a sum up to the target.
	if len(nums) < 2 {
		return indices
	}

	// I want to store all numbers I've seen
	// together with their indices in the array.
	// seenIndices[number] = index in the array
	seenIndices := make(map[int]int)
	seenIndices[nums[0]] = 0

	for i := 1; i < len(nums); i++ { // Because O(n)
		currentNum := nums[i]
		// I want to check if there's already an existing counter part that together sum up to the target.
		potentialPair := target - currentNum
		val, ok := seenIndices[potentialPair]

		if ok {
			indices = append(indices, val, i)
			return indices
		}

		// I'll add them to the map as I iterate through the array
		seenIndices[currentNum] = i
	}

	return indices

	// In Runtime this code beats "58.68%" of people according to Leetcode.
	// In Memory this code ONLY beats "15.50%" of people according to Leetcode.

	// What would you improve?
	// How would you do it better for both cases?
}
