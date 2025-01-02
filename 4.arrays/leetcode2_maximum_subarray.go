package main

import "math"

/**
 * LEETCODE PROBLEM #53
 *
 * Description Directly from: https://leetcode.com/problems/maximum-subarray/description/
 *
 * Given an integer array nums, find the subarray with the largest sum, and return its sum.
 * You can return the answer in any order.
 *
 * Example 1:
 * Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
 * Output: 6
 * Explanation: The subarray [4,-1,2,1] has the largest sum 6.
 *
 * Example 2:
 * Input: nums = [1]
 * Output: 1
 * Explanation: The subarray [1] has the largest sum 1.
 *
 * Example 3:
 * Input: nums = [5,4,-1,7,8]
 * Output: 23
 * Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 *
 * Constraints:
 * 1 <= nums.length <= 10^5
 * -10^4 <= nums[i] <= 10^4
 */

// Not checking everything
func SecondFailedAttempt(nums []int) int {
	// For that I need a new array
	historyOfSums := []int{}

	historyOfSums = append(historyOfSums, nums[0])

	for i := 1; i < len(nums); i++ {
		previousNum := historyOfSums[i-1]
		currentNum := nums[i]
		sum := previousNum + currentNum

		historyOfSums = append(historyOfSums, sum)
	}

	largestSum := nums[0]

	for i := 1; i < len(historyOfSums); i++ {
		currentSum := historyOfSums[i]

		if largestSum < currentSum {
			largestSum = currentSum
		}
	}

	return largestSum
}

func helperSubArraySum(nums []int, index1, index2 int) int {
	sum := 0
	for i := index1; i <= index2; i++ {
		sum = sum + nums[i]
	}

	return sum
}

// Doesn't really work as we could drop pointer 1 or 2
// But the checking for other positive integers then gets tricky
func ThirdFailedAttempt(nums []int) int {
	largestSum := 0

	// Let's use pointers to keep track of the positive integers
	pointer1, pointer2 := 0, 0

	for i := 0; i < len(nums); i++ {
		currentNum := nums[i]

		// Check if we have reached a positive number
		if currentNum > -1 {
			// Check if the first pointer was to a negative number
			if nums[pointer1] < 0 {
				pointer1 = i
				pointer2 = i
			} else {
				// We need to check if the sum of negative numbers between both of them outperforms keeping the subarray
				// [pointer1:pointer2]
				pointer2 = i

				// Check the sum of the sub array [pointer1:pointer2]
				res := helperSubArraySum(nums, pointer1, pointer2)

				if res < nums[pointer2] {
					pointer1 = pointer2
				}
			}
		}
	}

	return largestSum
}

// This fails because we stop checking after the first negative number comes in
func FourthFailedAttempt(nums []int) int {
	historyOfSums := []int{}
	historyOfSums = append(historyOfSums, nums[0])
	largestAcc := nums[0]
	indexOfLargestAcc := 0

	for i := 1; i < len(nums); i++ {
		previousNum := historyOfSums[i-1]
		currentNum := nums[i]
		sum := previousNum + currentNum

		historyOfSums = append(historyOfSums, sum)

		if largestAcc < sum {
			largestAcc = sum
			indexOfLargestAcc = i
		}
	}

	// We know the first element was the highest number and no other sums helped
	if indexOfLargestAcc == 0 {
		return nums[indexOfLargestAcc]
	}

	// We know adding all numbers in the array will create the largest sum
	if indexOfLargestAcc == len(nums)-1 {
		return largestAcc
	}

	// Now I know what's the highest number in the array
	highestNum := nums[indexOfLargestAcc]

	// I want to start checking the values around
	// We will start from the origin, in case the highest number is also the largest subArray
	pointer1, pointer2 := indexOfLargestAcc, indexOfLargestAcc
	limitLeftReached, limitRightReached := false, false
	sumLeft, sumRight := highestNum, highestNum

	for !limitLeftReached || !limitRightReached {
		// It fails because of this
		newSumLeft := sumLeft + nums[pointer1-1]
		newSumRight := sumRight + nums[pointer2+1]

		if newSumLeft < sumLeft {
			// It fails because of this
			limitLeftReached = true
		} else {
			sumLeft = newSumLeft
			if pointer1 != 0 {
				pointer1--
			} else {
				limitLeftReached = true
			}
		}

		if newSumRight < sumRight {
			// It fails because of this
			limitRightReached = true
		} else {
			sumRight = newSumRight
			if pointer2 != len(nums)-1 {
				pointer2++
			} else {
				limitRightReached = true
			}
		}
	}

	// Now let's make the sum of the largest subarray
	largestSum := 0
	for i := pointer1; i <= pointer2; i++ {
		largestSum += nums[i]
	}

	return largestSum
}

// Almost THERE!
// Now I just need to deal with cases where big numbers throw things astray
// Which is basically what Kadane's algorithm is doing, so I'll stick with it
// BUT IT WAS A GOOD MENTAL EXERCISE!
func FifthFailedAttempt(nums []int) int {
	historyOfSums := []int{}
	historyOfSums = append(historyOfSums, nums[0])
	largestAcc := nums[0]
	indexOfLargestAcc := 0

	for i := 1; i < len(nums); i++ {
		previousNum := historyOfSums[i-1]
		currentNum := nums[i]
		sum := previousNum + currentNum

		historyOfSums = append(historyOfSums, sum)

		if largestAcc < sum {
			largestAcc = sum
			indexOfLargestAcc = i
		}
	}

	// We know the first element was the highest number and no other sums helped
	if indexOfLargestAcc == 0 {
		return nums[indexOfLargestAcc]
	}

	// We know adding all numbers in the array will create the largest sum
	if indexOfLargestAcc == len(nums)-1 {
		return largestAcc
	}

	// Now I know what's the highest number in the array
	highestNum := nums[indexOfLargestAcc]

	// Similar to FourthFailedAttempt, I'll check the accumulations to the left and right, but won't stop until I reach the end of the array
	pointerLeft, pointerRight := indexOfLargestAcc, indexOfLargestAcc
	sumLeft, sumRight := highestNum, highestNum
	highestLeft, highestRight := highestNum, highestNum

	// I'll check left first
	// Where the highest acc to the left is
	for i := indexOfLargestAcc - 1; i >= 0; i-- {
		sumLeft = sumLeft + nums[i]

		if highestLeft < sumLeft {
			highestLeft = sumLeft
			pointerLeft = i
		}
	}

	// I'll do the same for the right
	for i := indexOfLargestAcc + 1; i < len(nums); i++ {
		sumRight = sumRight + nums[i]

		if highestRight < sumRight {
			highestRight = sumRight
			pointerRight = i
		}
	}

	// Now let's make the sum of the largest subarray
	largestSum := 0
	for i := pointerLeft; i <= pointerRight; i++ {
		largestSum += nums[i]
	}

	return largestSum
}

// First version
func MaxSubArray(nums []int) int {
	if len(nums) == 0 {
		return 0
	}

	if len(nums) == 1 {
		return nums[0]
	}

	/**
	 * Before diving into the problem, yes, you can brute force this with nested for loops and get the largest sum.
	 * I think this is more of a general context so you can speak about it during interviews.
	 */

	/**
	 * My original thoughts where:
	 * Let's go first over the array to see the sum of all elements, that should be our minimum threshold/subarray.
	 * Now we have to find if there's a subarray which sum is greater than the current "sum"
	 */

	// But that poses too many challenges
	// As I would have to iterate over and over to find the right subarray

	/**
	 * My second thought:
	 * Instead, let's keep track of all additions as we iterate
	 * We will do 2 separate for loops
	 * One where we will have the history of the sums
	 * And the second one where we will check which of those sums is the largest
	 * BUT that poses the problem, I'm just checking subarrays based on all containing from the first element on.
	 * I'm not checking subarrays starting on index 1 or index 2 or index n.
	 */

	/**
	 * Third thinking:
	 * Let's discard the negative numbers from the subarray
	 * Check if the next negative numbers in between 2 positive numbers are subtracting more than when we find the next largest positive number.
	 * BUT let's say it doesn't work, and the result is less than either of the positive integers, then which one do we drop?
	 * And based on that, how do we find the next positive integer and perform the operation?
	 */

	/**
	 * 4TH COMMENT - 4th attempt
	 * Either you've given it a shot a few times OR you've read my comments and dived into deep thought.
	 * This problem isn't as easy as it might seem at first.
	 * And the issue are: the negative numbers.
	 *
	 * I'll say these 2 things:
	 * 1) If you open leetcode and looked at their hint, yes, it can be solved by dividing an conquer.
	 * 2) It can also be solved by iterating ONCE through the array = O(n).
	 * Hint: remember, the issue are the negative numbers... and yes, at first it took me a few hours, but it was a great mental exercise.
	 * Afterwards, yes, I went out and learned there is something called Kadane's algorithm 😐.
	 */

	// BEFORE reading the next code, check all the attempts and see what you would improve in each iteration or if you had gone down in a completely different path.

	// I'll implement Kadane's algorithm, which is a lot simpler than what I do
	currentLargestSum, highestSumFound := nums[0], nums[0]

	for i := 1; i < len(nums); i++ {
		currValue := nums[i]
		currentLargestSum = int(math.Max(float64(currValue), float64(currentLargestSum+currValue)))
		highestSumFound = int(math.Max(float64(currentLargestSum), float64(highestSumFound)))
	}

	// Why does this work?
	// Because let's say we have theses cases:
	// case1 := []int{3, 5, -4, 8, 11, 1, -1, 6} // 29
	// case2 := []int{-2, 1, -3, -4, -1, -2, 2, -5, -4} // 2
	// case3 := []int{-5, 3, 98, -99, -2, 200}

	// For case 1: we can see we are comparing between the current value and the sum of the current value + the accumulator
	// When we compare (-4, 8 + (-4)), we see 4 is the largest of the 2 BUT it doesn't beat the highest sum found
	// "highestSumFound" is either a single number or the accumulation of a certain subarray.

	// For case 2: we know 1 is the highest number until we get to 2.

	// How does it work for case 3 then?

	return highestSumFound
}
