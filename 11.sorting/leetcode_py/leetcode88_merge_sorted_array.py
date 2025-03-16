"""
LEETCODE PROBLEM #88

Description Directly from: https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""


class Solution:
    def merge_sort(self, left_input: list[str], right_input: list[str]) -> list[str]:
        pointer_left, pointer_right = 0, 0
        helper_arr = []

        # If you do "or" instead of the "and",
        # don't forget to do validations for "None"
        while pointer_left < len(left_input) and pointer_right < len(right_input):
            if left_input[pointer_left] < right_input[pointer_right]:
                helper_arr.append(left_input[pointer_left])
                pointer_left += 1
            else:
                helper_arr.append(right_input[pointer_right])
                pointer_right += 1

        helper_arr.extend(left_input[pointer_left:])
        helper_arr.extend(right_input[pointer_right:])

        return helper_arr

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # First join the arrays as it has to be in-place
        nums1 = nums1[:m]

        # Now let's sort
        # From the question, the context, everything,
        # you can tell you need to use merge sort.
        #
        # I used insertion sort for 2 reasons:
        # 1) The problem was asking for an in-place solution
        # 2) We were dealing with nearly sorted data.
        # Hence, Insertion Sort kinda made more sense to me. But that's me.
        # That said, Insertion Sort IS TOO SLOW.
        # for i in range(m, len(nums1)):
        #     curr_value = nums1[i]
        #     pos = i-1
        #     while pos > -1 and curr_value < nums1[pos]:
        #         nums1[pos+1] = nums1[pos]
        #         pos -= 1
        #     nums1[pos+1] = curr_value
        return self.merge_sort(nums1, nums2)


s = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
s.merge(nums1, m, nums2, n)
print(f"Solution: {nums1}")
print("----- ----- -----\n")

nums1 = [2, 0]
m = 1
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
print(f"Solution: {nums1}")
print("----- ----- -----\n")

nums1 = [4, 0, 0, 0, 0, 0]
m = 1
nums2 = [1, 2, 3, 5, 6]
n = 5
s.merge(nums1, m, nums2, n)
print(f"Solution: {nums1}")
print("----- ----- -----\n")
