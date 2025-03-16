package main

import (
	"fmt"
	"sort"
)

/**
 * LEETCODE PROBLEM #15

 * Description Directly from: https://leetcode.com/problems/3sum/

 * Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

 * Notice that the solution set must not contain duplicate triplets.

 * Example 1:
 * Input: nums = [-1,0,1,2,-1,-4]
 * Output: [[-1,-1,2],[-1,0,1]]
 * Explanation:
 * nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
 * nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
 * nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
 * The distinct triplets are [-1,0,1] and [-1,-1,2].
 * Notice that the order of the output and the order of the triplets does not matter.

 * Example 2:
 * Input: nums = [0,1,1]
 * Output: []
 * Explanation: The only possible triplet does not sum up to 0.

 * Example 3:
 * Input: nums = [0,0,0]
 * Output: [[0,0,0]]
 * Explanation: The only possible triplet sums up to 0.

 * Constraints:
 * 3 <= nums.length <= 3000
 * -105 <= nums[i] <= 105
 */

func threeSum(nums []int) [][]int {
	if len(nums) < 3 {
		return [][]int{}
	}

	results := [][]int{}
	resultsMap := map[string]bool{}

	positives := []int{}
	negatives := []int{}
	zeroes := []int{}

	for _, num := range nums {
		if num > 0 {
			positives = append(positives, num)
		} else if num < 0 {
			negatives = append(negatives, num)
		} else {
			if len(zeroes) < 3 {
				// Small optimization
				// Search for Golang Dynamic memory allocation
				zeroes = append(zeroes, num)
			}
		}
	}

	// For faster searches - let's transform the arrays to maps
	positivesMap := map[int]int{}
	negativesMap := map[int]int{}

	for _, positive := range positives {
		positivesMap[positive] = positive
	}

	for _, negative := range negatives {
		negativesMap[negative] = negative
	}

	// First case where we care about the zeroes
	// If there are 3 zeroes, let's get that case out of the way.
	if len(zeroes) > 2 {
		results = append(results, []int{0, 0, 0})
	}

	// This is the only other ase where we care about zeroes
	// If there are any zeroes, let's search for pairs that will add up to zero
	// E.g. [-1,1] [-x,x]
	// We can use either the positives or negatives array, we'll find the pairs either way
	if len(zeroes) > 0 {
		for i := 0; i < len(positives); i += 1 {
			negativeToFind := -1 * positives[i]
			if _, ok := negativesMap[negativeToFind]; ok {
				resultAsString := fmt.Sprintf("%d %d %d", negativeToFind, 0, positives[i])
				if _, ok := resultsMap[resultAsString]; !ok {
					resultsMap[resultAsString] = true
					results = append(results, []int{negativeToFind, 0, positives[i]})
				}
			}
		}
	}

	// Now all that's left is to take 2 positives or 2 negatives and search for the sum in the other one
	for i := 0; i < len(positives); i += 1 {
		for j := i + 1; j < len(positives); j += 1 {
			negativeTarget := -1 * (positives[i] + positives[j])
			if _, ok := negativesMap[negativeTarget]; ok {
				result := []int{negativeTarget, positives[i], positives[j]}
				sort.Sort(sort.IntSlice(result))
				// sort.Slice(result, func(i, j int) bool {
				// 	return result[i] < result[j]
				// })

				resultAsString := fmt.Sprintf("%d %d %d", result[0], result[1], result[2])
				if _, ok := resultsMap[resultAsString]; !ok {
					resultsMap[resultAsString] = true
					results = append(results, result)
				}
			}
		}
	}

	for i := 0; i < len(negatives); i += 1 {
		for j := i + 1; j < len(negatives); j += 1 {
			positiveTarget := -1 * (negatives[i] + negatives[j])
			fmt.Println("positiveTarget:", positiveTarget)
			if _, ok := positivesMap[positiveTarget]; ok {
				result := []int{positiveTarget, negatives[i], negatives[j]}
				sort.Sort(sort.IntSlice(result))

				resultAsString := fmt.Sprintf("%d %d %d", result[0], result[1], result[2])
				if _, ok := resultsMap[resultAsString]; !ok {
					resultsMap[resultAsString] = true
					results = append(results, result)
				}
			}
		}
	}

	return results
}
