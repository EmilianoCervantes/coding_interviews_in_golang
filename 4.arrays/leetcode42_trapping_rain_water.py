"""
LEETCODE PROBLEM #42

Description Directly from: https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

class Solution:
    def trap(self, height: list[int]) -> int:
        # Can't do anything if there are no walls
        if len(height) < 3:
            return 0
        """
        What do we need to check out for?
        - When height is at any elevated point
        - When it decreases
        - When it increases again

        How do we calculate irregular intervals?
        - n decreases followed by m increases,
        - New sections that have the same height,
        - What happens if the tallest is at the start?
                - However many times it increases and decreases.

        I would propose:
        - When number is > 0.
        - While it decreases - add the temp square per square
        - While it grows, keep adding until the height is larger than the first one.
        - Restart from new greater height OR when it starts to decrease again. <-- NO
        - Just -> Restart from new greater height.

        So having the tallest at opposite ends of the array.
        As well as a rollercoaster of ups and downs.
        Does that affect?
        How will I keep track of calculations?
        """

        # I want to keep separate if there's a continuous decrease
        # right before the list ends
        trapped_water = temp_trapped = 0

        left = 0
        right = 1
        # tallest = height[0] # Prob not needed now with our "sections" thing

        # Let's call each section where there's a taller wall a "new section"
        # Note: a "section" can be the whole list
        # We want to go section per section
        while right < len(height):
            # Check if right is decreasing.
            height1 = height[left]
            height2 = height[right]
            print(f"Left: {height1} - Right: {height2}")
            print(f"trapped_water: {trapped_water}")
            if height1 > height2:
                # How many squares we'll add?
                # Height left - height right
                temp_trapped = trapped_water + (height1 - height2)
            
            # Check if right is increasing? Yes
            # E.g. 3-2-1-2: there's one block of water between both 2's.
            # But how do we compare with only 2 pointers?
            
            # Check if there's a new section we need to review
            # Which means we've reached a height as high at least as the left
            if height1 <= height2:
                left = right
                trapped_water += temp_trapped
                temp_trapped = 0
            
            right += 1
        
        return trapped_water

s = Solution()

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(f"{height}: {s.trap(height)}") # 6

# height = [4,2,0,3,2,5]
# print(f"{height}: {s.trap(height)}") # 9

# height = [0,2,0,3,1,0,1,3,2,1]
# print(f"{height}: {s.trap(height)}") # 9
