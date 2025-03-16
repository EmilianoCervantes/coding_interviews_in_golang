"""
LEETCODE PROBLEM #703

Description Directly from: https://leetcode.com/problems/kth-largest-element-in-a-stream/

You are part of a university admissions office and need to keep track of the kth highest test score from applicants in real-time. This helps to determine cut-off marks for interviews and admissions dynamically as new applicants submit their scores.

You are tasked to implement a class which, for a given integer k, maintains a stream of test scores and continuously returns the kth highest test score after a new score has been submitted. More specifically, we are looking for the kth highest score in the sorted list of all scores.

Implement the KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of test scores nums.
int add(int val) Adds a new test score val to the stream and returns the element representing the kth largest element in the pool of test scores so far.
"""


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        pass

    def add(self, val: int) -> int:
        """
        Use a Min-Heap.

        We want the kth element - it will always be the same.
        Meaning --> the smallest of the largest numbers.
        You got it?

        We will always return the number AT THE SAME POSITION.
        Doesn't matter which number.

        If we want the 3th largest, we'll maintain 3 numbers in our heap.
        2th largest? Maintain 2 numbers.
        5th largest? Maintain 5 numbers.
        BUT we WON'T maintain the whole list.

        So not even O(n).
        Nor complicated lookups.

        That's why a Min-Heap.
        Time complexity: O(log(k)) - even less than O(log(n)).
        Superb time.
        """
        # TODO: implement it
        pass


s = KthLargest()

# ["KthLargest", "add", "add", "add", "add", "add"]
# [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
