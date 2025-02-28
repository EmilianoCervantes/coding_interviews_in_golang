"""
LEETCODE PROBLEM #128

Description Directly from: https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Example 3:
Input: nums = [1,0,1,2]
Output: 3

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

class Solution:
    # I didn't code further because, even though it's close to the answer
    # And we can finish solving this recursively, I felt the code was too big.
    def longestConsecutiveFailedSolution(self, nums: list[int]) -> int:
        if not len(nums):
            return 0

        # Have a dictionary to save the arrays
        # The keys will be the numbers
        nums_counter: dict[int, list[int]] = {}

        # Go over every number
        for curr_num in nums:
            # Check if the number is saved or not
            if curr_num not in nums_counter:
                # If not:
                # Check if the numbers next to it are saved
                one_down = curr_num - 1
                one_up = curr_num + 1
                if one_down in nums_counter and one_up in nums_counter:
                    # If there are both ways, join everything
                    list_down = nums_counter[one_down]
                    list_up = nums_counter[one_up]
                    final_list = list_down + [curr_num] + list_up
                    nums_counter[curr_num] = final_list
                    # Updating these keys as well as there could be future numbers looking for them
                    nums_counter[one_down] = final_list
                    nums_counter[one_up] = final_list
                # If there are saved numbers next to each the current, save them together
                elif one_down in nums_counter:
                    list_down = nums_counter[one_down]
                    nums_counter[curr_num] = list_down + [curr_num]
                    nums_counter[one_down] = list_down + [curr_num]
                elif one_up in nums_counter:
                    list_up = nums_counter[one_up]
                    nums_counter[curr_num] = [curr_num] + list_up
                    nums_counter[one_up] = [curr_num] + list_up
                else:
                    nums_counter[curr_num] = [curr_num]
                
                print(f"Current numbers: {curr_num}")
                print(f"nums_counter: {nums_counter}")


        max_consecutive = 1
        results = list(nums_counter.values())

        print(f"Consecutive results: {results}")

        for result in results:
            max_consecutive = max(max_consecutive, len(result))

        return max_consecutive
    
    # I used the overall logic from above
    # But the approach starts differently
    def longestConsecutiveLongTrainOfThought(self, nums: list[int]) -> int:
        if not len(nums):
            return 0
        
        # Have an easier time looking up the numbers
        # You'll notice in the next code
        nums_set = set(nums)
        # Still a place to store our results
        # Note: you can skip this variable, that's why there is a third solution
        # I just wanted to point out what others might think.
        # This makes the solution longer without a real need.
        sequences_dict: dict[int, list[int]] = {}

        # We still want to check each number left and right
        for curr_num in nums:
            # left
            left_num_to_find = curr_num - 1
            # right
            right_num_to_find = curr_num + 1

            if left_num_to_find in nums_set:
                # There's another potential sequence already
                # Let's skip this iteration
                continue
            if right_num_to_find in nums_set:
                # There's another above it we need to pull
                # And let's keep going all the way to the right
                # Full solution next
                pass
            else:
                sequences_dict[curr_num] = 1

        
        results = list(sequences_dict.values())

        print(f"Consecutive results: {results}")

        for result in results:
            max_consecutive = max(max_consecutive, len(result))

        return max_consecutive
    
    def longestConsecutive(self, nums: list[int]) -> int:
        if not len(nums):
            return 0
        
        # Have an easier time looking up the numbers
        # You'll notice in the next code
        nums_set = set(nums)
        # This is how we avoid the extra code of `sequences_dict`.
        max_consecutive = 1

        # We still want to check each number left and right
        # Remember to do it to nums_set instead of nums
        for curr_num in nums_set:
            if (curr_num - 1) in nums_set:
                # There's another potential sequence already
                # Let's skip this iteration
                continue
            if (curr_num + 1) in nums_set:
                # There's another above it we need to say, there's a larger consecutive number
                right_counter = 1
                # And let's keep going all the way to the right
                while (curr_num + right_counter) in nums_set:
                    # First iteration right_counter == 2
                    # Current number is one position, one to the right is another position
                    right_counter += 1
                    max_consecutive = max(max_consecutive, right_counter)

        return max_consecutive

s = Solution()

nums = [100,4,200,1,3,2]
print(f"Solution 1: {s.longestConsecutive(nums)}")

nums = [0,3,7,2,5,8,4,6,0,1]
print(f"Solution 2: {s.longestConsecutive(nums)}")
