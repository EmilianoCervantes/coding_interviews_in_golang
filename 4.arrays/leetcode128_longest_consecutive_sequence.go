package main

/**
 * LEETCODE PROBLEM #128

 * Description Directly from: https://leetcode.com/problems/longest-consecutive-sequence/

 * Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

 * You must write an algorithm that runs in O(n) time.

 * Example 1:
 * Input: nums = [100,4,200,1,3,2]
 * Output: 4
 * Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

 * Example 2:
 * Input: nums = [0,3,7,2,5,8,4,6,0,1]
 * Output: 9

 * Example 3:
 * Input: nums = [1,0,1,2]
 * Output: 3

 * Constraints:
 * 0 <= nums.length <= 105
 * -109 <= nums[i] <= 109
 */

func longestConsecutive(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	maxConsecutive := 1

	// In Go as there is no built-in set DS
	// Let's create our own
	numsSet := make(map[int]struct{})

	for _, num := range nums {
		numsSet[num] = struct{}{}
	}

	for currNum := range numsSet {
		if _, ok := numsSet[currNum-1]; !ok {
			rightCounter := 1

			// Go doesn't have while
			// That doesn't mean we cannot achieve the same respecting the three parts
			// for initialization; condition; iteration {}
			for _, isRightNumber := numsSet[currNum+rightCounter]; isRightNumber; _, isRightNumber = numsSet[currNum+rightCounter] {
				rightCounter += 1
				if maxConsecutive < rightCounter {
					maxConsecutive = rightCounter
				}
			}
		}
	}

	return maxConsecutive
}
