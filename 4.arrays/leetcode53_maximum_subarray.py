"""
LEETCODE PROBLEM #53

Description Directly from: https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum, and return its sum.
You can return the answer in any order.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        if not len(nums):
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        current_max_sum = global_max_sum = nums[0]

        print(f"current_max_sum: {current_max_sum}")
        print(f"global_max_sum: {global_max_sum}")
        print("----------------------------------------")

        for index in range(1, len(nums)):
            current_num = nums[index]
            # Remember:
            # current_max_sum will be different from global_max_sum
            # in most cases.
            current_max_sum = max(current_num, current_max_sum + current_num)
            print(f"Run {index}")
            print(f"current_max_sum: {current_max_sum}")

            if global_max_sum < current_max_sum:
                global_max_sum = current_max_sum
            print(f"global_max_sum: {global_max_sum}")
            print("----------------------------------------")

        return global_max_sum

s = Solution()
s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# s.maxSubArray([5,4,-1,7,8])

