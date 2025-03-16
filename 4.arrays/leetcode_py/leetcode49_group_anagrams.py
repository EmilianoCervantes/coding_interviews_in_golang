"""
LEETCODE PROBLEM #49

Description Directly from: https://leetcode.com/problems/group-anagrams/

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
 
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
- There is no string in strs that can be rearranged to form "bat".
- The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
- The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
- 1 <= strs.length <= 104
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.
"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if not len(strs):
            return [[""]]
        # Set to keep track of existing anagrams
        # anagrams_set = set()
        # key will be the sorted anagram
        anagrams_dictionary: dict[str, list[str]] = {}

        # sort words
        for word in strs:
            sorted_word = ''.join(sorted(word))
            # Look into the dictionary
            if sorted_word in anagrams_dictionary:
                anagrams_dictionary[sorted_word].append(word)
            else:
                anagrams_dictionary[sorted_word] = [word]

        return list(anagrams_dictionary.values())

s = Solution()

words = ["eat","tea","tan","ate","nat","bat"]
print(f"words 1: {s.groupAnagrams(words)}")
