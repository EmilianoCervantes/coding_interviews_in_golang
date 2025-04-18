"""
LEETCODE PROBLEM #1

Description Directly from: https://leetcode.com/problems/two-sum/
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
2 <= nums.length <= 104
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
Only one valid answer exists.
"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        O(n) solution
        We need to check the pair, if there is a pair saved previously, then return both.
        If there is no pair, save the value and wait to see if later the pair comes up.
				"""
        numbers_so_far: dict[int, int] = {}
        
        for i, num in enumerate(nums):
            look_up = target - num
            
            if look_up in numbers_so_far:
              is_index_found = numbers_so_far[look_up]
              return [is_index_found, i]
            
            numbers_so_far[num] = i
            
        return []


nums = [2,3,4,5,6,7,8,9]

s = Solution()
res = s.twoSum(nums, 10)

print(f"res: {res}")