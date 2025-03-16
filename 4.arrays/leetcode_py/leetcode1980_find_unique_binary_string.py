"""
LEETCODE PROBLEM #1980

Description Directly from: https://leetcode.com/problems/find-unique-binary-string/

Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

Example 1:
Input: nums = ["01","10"]
Output: "11"
Explanation: "11" does not appear in nums. "00" would also be correct.

Example 2:
Input: nums = ["00","01"]
Output: "11"
Explanation: "11" does not appear in nums. "10" would also be correct.

Example 3:
Input: nums = ["111","011","001"]
Output: "101"
Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.

Constraints:
n == nums.length
1 <= n <= 16
nums[i].length == n
nums[i] is either '0' or '1'.
All the strings of nums are unique.
"""

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        if len(nums) < 1:
            return ""

        # We need to identify the length of each number
        # We will use this for doing all combinations
        len_to_review = len(nums[0])

        # Then wee need to check the total of potential variants
        # Why? To know if the array has all of them already
        # 2^length is the number of binaries we can have for a certain length
        total_variants = 2**len_to_review

        if total_variants < len(nums):
            return ""

        nums_set = set(nums)

        # What to do?
        # Check if the combination is exists in the set?
        # For the length of the total variants, should we check if they exist in the set?

        # 
        for index in range(total_variants):
            # Now we want to start checking
            # Starting with 0...0
            # We have to go binary per binary
            combination = f"{index:0{len_to_review}b}"
            if combination not in nums_set:
                break

        return combination

s = Solution()

s.findDifferentBinaryString(["111","011","001"])
