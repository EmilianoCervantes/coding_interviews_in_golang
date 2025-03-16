"""
LEETCODE PROBLEM #238

Description Directly from: https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums,
return an array answer such that answer[i] is equal
to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """
        Since we cannot use the "/" operation,
        doing a loop to multiply everything is not aan option.

        And to do it O(n) we need to traverse and keep the multiplications.

        How about we pre-populate an array with 1's?
        And we start multiplying every one as we go through the numbers?
        Would that be O(n)? - In short, no.

        But the initial array is a good start.

        Based on a hint from the comment's section,
        we can multiply left and right products...
        Okay, what does that actually mean??

        Let's do 2 loops, one to increasingly multiply from 0..n
        and a second one to increasingly multiply n..0.
        """
        
        # Let's use a list comprehension for this:
        prefix_list = [1 for _ in range(len(nums))]
        suffix_list = [1 for _ in range(len(nums))]

        # First, let's do the increasing left multiplications from 1..n
        # If you noticed, we need to actually multiply starting from position 1.
        for index in range(1,len(nums)):
            pos_to_the_left = index-1 # Just adding this extra line to make the reasoning more explicit
            increasing_multiplication = nums[pos_to_the_left] * prefix_list[pos_to_the_left]
            # Multiplication so far without the current index
            prefix_list[index] = increasing_multiplication
        
        # Then let's do it backwards
        for index in reversed(range(0, len(nums)-1)):
            # Slightly different from above
            # num_to_right * solution current_position number
            increasing_multiplication = nums[index+1] * suffix_list[index+1]
            # Last multiplication without the current index
            suffix_list[index] = increasing_multiplication
        
        solution_list = []

        for index in range(len(nums)):
            response = prefix_list[index] * suffix_list[index]
            solution_list.append(response)
        
        return solution_list
    
s = Solution()

# [  1,  2,  3,  4,  5] - Original
# [  1,  1,  2,  6, 24] - Left result
# [120, 60, 20,  5,  1] - Right result
# [120, 60, 40, 30, 24] - Final array
print(s.productExceptSelf([1,2,3,4,5]))
print(s.productExceptSelf([-1,1,0,-3,3]))
