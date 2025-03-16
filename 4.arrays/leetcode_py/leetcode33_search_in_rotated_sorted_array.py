"""
LEETCODE PROBLEM #33

Description Directly from: https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1
 

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

# There are a LOT of ways to improve this
# My focus here was to divide each case/scenario to do a quicker search
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        if len(nums) < 1:
            return -1
        
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        
        # Let's see first which value is at the beginning and which one at the end
        # That way we can tell where the target is closer to
        # Maybe also the middle value of the array will help
        left_pointer = 0
        middle_pointer = len(nums) // 2
        right_pointer = len(nums)-1

        # A real quick check to see if by any chance we got it

        if target == nums[left_pointer]:
            return left_pointer
        
        if target == nums[middle_pointer]:
            return middle_pointer

        if target == nums[right_pointer]:
            return right_pointer

        # Next, let's check if the target is greater or lower than these values.
        # And based on if left or right wins,
        # we can determine where to go between the position and the middle.
        # Note: maybe we only need to check right or left, not both
        is_less_than_middle = target < nums[middle_pointer]

        # We'll search in the first half of the array
        if nums[left_pointer] <= target:
            left_pointer = left_pointer + (target - nums[left_pointer])

            print("left_pointer:", left_pointer)
            if len(nums) - 1 < left_pointer:
                if is_less_than_middle:
                    left_pointer = 0

                    while left_pointer < middle_pointer:
                        left_pointer += 1

                        if target == nums[left_pointer]:
                            return left_pointer
                    return -1
                else:
                    while middle_pointer < right_pointer:
                        middle_pointer += 1

                        if target == nums[middle_pointer]:
                            return middle_pointer
                    return -1

            if nums[left_pointer] == target:
                return left_pointer
            # The target is less than the number of positions moved
            else:
                if middle_pointer <= left_pointer:
                    while middle_pointer > 0:
                        middle_pointer -= 1
                        if target == nums[middle_pointer]:
                            return middle_pointer
                
                if left_pointer < middle_pointer:
                    while left_pointer > 0:
                        left_pointer -= 1
                        if target == nums[left_pointer]:
                            return left_pointer

        # Lets search in the second half of the array
        else:
            # If it is greater than the right, then the number doesn't exist between right < number < left
            if nums[right_pointer] < target:
                return -1

            right_pointer = right_pointer - (nums[right_pointer] - abs(target))

            if right_pointer < 0:
                if is_less_than_middle:
                    while left_pointer < middle_pointer:
                        middle_pointer -= 1

                        if target == nums[middle_pointer]:
                            return middle_pointer
                    return -1
                else:
                    right_pointer = len(nums) - 1
                
                    while middle_pointer < right_pointer:
                        right_pointer -= 1

                        if target == nums[right_pointer]:
                            return right_pointer
                    return -1

            if nums[right_pointer] == target:
                return right_pointer
            # The target is greater than the number of positions moved
            else:
                if right_pointer <= middle_pointer:
                    while middle_pointer > 0:
                        middle_pointer -= 1
                        if target == nums[middle_pointer]:
                            return middle_pointer
                
                if middle_pointer < right_pointer:
                    while right_pointer < len(nums) - 1:
                        right_pointer += 1
                        if target == nums[right_pointer]:
                            return right_pointer
        
        return -1

s = Solution()

print(s.search([4,5,6,7,0,1,2], 0))

print(s.search([4,5,6,7,0,1,2], 3))

print(s.search([1,3], 4))

print(s.search([2,4,7,9,0], 9))

print(s.search([5,8,9,1,3], 8))

print(s.search([6,8,9,2,5], 8))

print(s.search([5,7,8,0,3,4], 7))
