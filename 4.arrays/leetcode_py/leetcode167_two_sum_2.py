"""
LEETCODE PROBLEM #167

Description Directly from: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2,
added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution.
You may not use the same element twice.

Your solution must use only constant extra space.

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

Constraints:
2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

class Solution:
    # This is based on "The tests are generated such that there is exactly one solution."
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """
        Remember we must respect constant extra space
        That means no sets, dicts, etc.
        The good this is the list is sorted.
        """
        pointer1 = 0
        pointer2 = 1

        while pointer2 < len(numbers):
            if (numbers[pointer1] + numbers[pointer2]) < target:
                pointer1 += 1
                pointer2 += 1
            elif (numbers[pointer1] + numbers[pointer2]) > target:
                pointer1 -= 1
            else:
                return [pointer1+1, pointer2+1]

    # Follow up question: what if there are cases with no solution?     
    def twoSumNoSolution(self, numbers: list[int], target: int) -> list[int]:
        """
        Again with constant space.
        Code for the cases with no solution
        """
        pointer1 = 0
        pointer2 = len(numbers) - 1

        # Notice the difference in the approaches?
        while pointer1 < pointer2:
            if (numbers[pointer1] + numbers[pointer2]) < target:
                pointer1 += 1
            elif (numbers[pointer1] + numbers[pointer2]) > target:
                pointer2 -= 1
            else:
                return [pointer1+1, pointer2+1]

s = Solution()

numbers = [2,7,11,15]
target = 9
print(f"{numbers} - target {target}: {s.twoSum(numbers, target)}")

numbers = [2,3, 4]
target = 6
print(f"{numbers} - target {target}: {s.twoSum(numbers, target)}")

numbers = [-1, 0]
target = -1
print(f"{numbers} - target {target}: {s.twoSum(numbers, target)}")
