"""
LEETCODE PROBLEM #215

Description Directly from: https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?
"""


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        """
        Options:
        1) Use a Min-Heap? - O(n log(n))
        2) Insertion sort in a subarray k to arr.length?
        3) Quicksort? -> Quickselect?
        Adaptation passing an index_of_interest besides the array.

        nums.length - k

        So for this problem seems Quickselect is the best option.
        It's not going all the way like Quicksort.

        You want to, based on your pivot, see how many larger/smaller elements there are.
        And then go and check ONLY that "half".
        """
        pass


s = Solution()
