"""
LEETCODE PROBLEM #75 - Sort colors (Dutch National Flag)

Description Directly from: https://leetcode.com/problems/sort-colors/

Given an array nums with n objects colored red, white, or blue, sort them **in-place** so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:
* Input: nums = [2,0,2,1,1,0]
* Output: [0,0,1,1,2,2]

Example 2:
* Input: nums = [2,0,1]
* Output: [0,1,2]

Constraints:
* n == nums.length
* 1 <= n <= 300
* nums[i] is either 0, 1, or 2.
"""


class Solution:
    def ball_to_int(self, ball: str) -> int:
        switch_dict = {
            "R": 0,
            "G": 1,
            "B": 2
        }
        return switch_dict.get(ball)

    def int_to_ball(self, num: int) -> str:
        switch_dict = {
            0: "R",
            1: "G",
            2: "B"
        }
        return switch_dict.get(num)

    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # We can do a insertion sort
        # Because we want in place
        # Also a pivot won't really help much as there's only 3 numbers
        for i in range(1, len(nums)):
            curr_value = nums[i]
            pos = i-1
            while pos > -1 and curr_value < nums[pos]:
                nums[pos+1] = nums[pos]
                pos -= 1

            nums[pos+1] = curr_value

    def counting_sort(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return []

        # [value, repetitions]
        arr_as_dict: dict[int, int] = {
            0: 0,
            1: 0,
            2: 0
        }

        res = []

        max_value = 2
        min_value = 0

        for value in arr:
            arr_as_dict[value] += 1

        # Go from min_value to max_value
        for num in range(min_value, max_value+1):
            if num in arr_as_dict:
                repetitions = arr_as_dict[num]
                for _ in range(repetitions):
                    res.append(num)
        return res

    def dutch_flag_sort(self, balls: list[str]) -> None:
        """
        Do not return anything, modify balls in-place instead.
        """
        # We can do a insertion sort
        # Because we want in place
        # Also a pivot won't really help much as there's only 3 numbers
        for i in range(len(balls)):
            balls[i] = self.ball_to_int(balls[i])

        # Turns out using Counting Sort IS WAAAY Better!
        res = self.counting_sort(balls)

        for i in range(len(res)):
            balls[i] = self.int_to_ball(res[i])


s = Solution()

nums = [2, 0, 2, 1, 1, 0]
s.sortColors(nums)
print(f"Sorted colors: {nums}")

nums = [2, 0, 1]
s.sortColors(nums)
print(f"Sorted colors: {nums}")

balls = ["G", "B", "G", "G", "R", "B", "R", "G"]
s.dutch_flag_sort(balls)
print(f"Sorted balls: {balls}")
