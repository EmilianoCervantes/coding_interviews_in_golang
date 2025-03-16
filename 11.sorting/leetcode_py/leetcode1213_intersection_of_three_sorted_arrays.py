"""
LEETCODE PROBLEM #1213

Description Directly from: https://leetcode.com/problems/intersection-of-three-sorted-arrays/

Given three integer arrays arr1, arr2, and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.
"""


class Solution:
    def intersection(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
        p1, p2, p3 = 0, 0, 0
        res = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            v1 = arr1[p1]
            v2 = arr2[p2]
            v3 = arr3[p3]
            if v1 == v2 == v3:
                res.append(v1)
                p1 += 1
                p2 += 1
                p3 += 1
            elif v1 < v2 or v1 < v3:
                p1 += 1
            elif v2 < v1 or v2 < v3:
                p2 += 1
            elif v3 < v1 or v3 < v2:
                p3 += 1

        return res


s = Solution()

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

print(f"Solution: {s.intersection(arr1, arr2, arr3)}")
