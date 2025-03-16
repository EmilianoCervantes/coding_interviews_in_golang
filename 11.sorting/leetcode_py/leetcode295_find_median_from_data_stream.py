"""
LEETCODE PROBLEM #295

Description Directly from: https://leetcode.com/problems/find-median-from-data-stream/

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
"""


class MedianFinder:
    def __init__(self):
        """
        How about we use both a Max-Heap for the smaller half,
        and a Min-Heap for the bigger half?

        If either heap > other heap by 2.
        We:
        - max_heap.insert(min_heap.extract_min())
        - min_heap.insert(max_heap.extract_max())

        We'll have everything balanced from the get go.

        And getting the "median" at all times will be an O(1) operation.
        """
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


s = MedianFinder()
