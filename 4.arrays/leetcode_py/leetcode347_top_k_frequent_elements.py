"""
LEETCODE PROBLEM #347

Description Directly from: https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique. 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        """
        This is my solution
        As you go through the comments, you'll see my reasoning.
        You can also see my full reasoning here:
        https://leetcode.com/problems/top-k-frequent-elements/solutions/6451440/maybe-not-the-best-approach-but-it-has-a-time-complexity-of-o-n

        But as you can see from the code, there's another solutions,
        which seems to be the best approach.
        Bucket Sort. I learned about it after doing this challenge.
        """
        if not len(nums):
            return []
        
        # Do a map of all counts
        # count_nums_dict = {num:nums.count(num) for num in set(nums)} # Do not - O(unique num * num)
        count_nums_dict: dict[int, int] = {} # O(n)
        for num in nums:
            if num in count_nums_dict:
                count_nums_dict[num] += 1
            else:
                count_nums_dict[num] = 1

        # Now let's invert the dictionary
        # Why? In count_nums_dict we have now how many times a number repeats
        # We can now group numbers by how many times they repeat
        lists_per_repetitions_dict: dict[int, list[int]] = {}
        # We can do 2 things, keep track of the largest amount of repetitions
        # Or sort by number of repetitions
        # As sorting would put us at O(n log(n)) - I will keep track of the most frequent(s) and go from there
        most_frequent_count = 1
        for key in count_nums_dict:
            num_of_repetitions = count_nums_dict[key]
            # Updating most frequent
            most_frequent_count = num_of_repetitions if most_frequent_count < num_of_repetitions else most_frequent_count

            if num_of_repetitions in lists_per_repetitions_dict:
                lists_per_repetitions_dict[num_of_repetitions].append(key)
            else:
                lists_per_repetitions_dict[num_of_repetitions] = [key]

        # Now let's go form the most frequent(s) all the way down until we cover k
        most_frequent_nums = []
        for num_of_repetitions in range(most_frequent_count, 0, -1):
            if num_of_repetitions in lists_per_repetitions_dict:
                most_frequent_nums.extend(lists_per_repetitions_dict[num_of_repetitions])
            # We reached the limit!
            if k <= len(most_frequent_nums):
                break

        # Maybe the code above is a lazy approach
        # But for going fast I kept it
        # Now I'll just remove the excess
        while len(most_frequent_nums) > k:
            most_frequent_nums.pop()

        return most_frequent_nums
    
    def topKFrequentBucketSort(self, nums: list[int], k: int) -> list[int]:
        """
        Bucket Sort Solution.
        Go through the pseudo code (check the resources),
        try it,
        before you take a look at the solution.

        Spoiler: it's actually similar to what I did.
        The version of Bucket Sort is using count as the index
        and a value of list as the numbers.

        Note: I'm assuming you already know Bucket sort
        """
        
        count_nums_dict: dict[int, int] = {} # O(n)
        # Similar to sudoku, but instead of sets, we do lists
        # Which was a thought I had, but I got stuck / hardheaded on doing sets
        lists_per_repetitions = [[] for _ in range(len(nums) + 1)] # +1 is not necessary, just makes things easier in your head

        for num in nums:
            # Similar to what I did,
            # this is just a one line cool Python trick.
            count_nums_dict[num] = 1 + count_nums_dict.get(num, 0)

        # Another trick I didn't know about - .items()
        for key, num_of_repetitions in count_nums_dict.items():
            lists_per_repetitions[num_of_repetitions].append(key)
        
        most_frequent_nums = []
        for num_of_repetitions in range(len(lists_per_repetitions) - 1, 0, -1):
            if len(most_frequent_nums) < k:
                most_frequent_nums.extend(lists_per_repetitions[num_of_repetitions])
        
        # Still separated this as I don't like nested loops
        while len(most_frequent_nums) > k:
            most_frequent_nums.pop()
        
        return most_frequent_nums

s = Solution()

print(f"Sol 1: {s.topKFrequent([1,1,1,2,2,3,4,5,5,6,6,6,6,7,7,7], 2)}")
print(f"Sol with Bucket Sort: {s.topKFrequentBucketSort([1,1,1,2,2,3,4,5,5,6,6,6,6,7,7,7], 2)}")
