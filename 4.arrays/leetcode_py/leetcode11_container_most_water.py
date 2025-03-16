"""
LEETCODE PROBLEM #11

Description Directly from: https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Constraints:
n == height.length
2 <= n <= 10^5
0 <= height[i] <= 10^4
"""

class Solution:
    def __area(self, height1: int, height2: int, distance: int) -> int:
        return min(height1, height2) * distance

    def __failed_maxArea(self, height: list[int]) -> int:
        """
        Problems to solve:
        1. Which pair of walls make the most area together
        2. Which pair of walls together with distance make the most area together
        3. Be careful to not calculate the area when the pointers are at the same position

        The reason this failed is because my 2 pointers where at the beginning.
        That didn't allow me true visibility.
        """

        # If there are no walls to check, there is no area
        if len(height) < 2:
            return 0
        

        max_area = min(height[0], height[1])

        if len(height) < 3:
            return max_area

        pointer1 = 0
        pointer2 = 2

        while pointer2 < len(height):
            area1 = self.__area(height[pointer1], height[pointer2], pointer2-pointer1)
            area2 = self.__area(height[pointer1+1], height[pointer2], pointer2-(pointer1+1))
            if area1 < area2:
                pointer1 += 1
                max_area = max(max_area, area2)
            else:
                max_area = max(area1, max_area)
            
            pointer2 += 1

        return max_area
    
    def maxArea(self, height: list[int]) -> int:
        """
        Two pointers.
        One at the beginning.
        Another all the way to the right.
        """

        # Just a line
        if len(height) < 2:
            return 0

        # There's only one square
        if len(height) < 3:
            return min(height[0], height[1])
        
        left = 0
        right = len(height)-1
        max_area = 0

        while left < right:
            new_area = self.__area(height[left], height[right], right-left)
            max_area = max(max_area, new_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

s = Solution()

print(f"s.maxArea([]): {s.maxArea([])}")
print(f"s.maxArea([100]): {s.maxArea([100])}")
print(f"s.maxArea([1,2]): {s.maxArea([1,2])}")
print(f"s.maxArea([1,2,3]): {s.maxArea([1,2,3])}")
print(f"s.maxArea([1,8,6,2,5,4,8,3,7]): {s.maxArea([1,8,6,2,5,4,8,3,7])}")
