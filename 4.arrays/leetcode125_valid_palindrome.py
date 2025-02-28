"""
LEETCODE PROBLEM #125

Description Directly from: https://leetcode.com/problems/valid-palindrome/

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

Constraints:
1 <= s.length <= 2 * 105
s consists only of printable ASCII characters.
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # cleanStr = ''.join(filter(str.isalnum, s)) # Option 1
        cleanStr = re.sub(r'[^a-zA-Z0-9]', '', s.lower())

        # There are 2 ways:
        # 1) We need to reverse the cleaned string and compare
        # 2) We can have 2 pointers go letter by letter
        # Because we could end up with an O(n^2) sol with option 1
        # I'll go with 2

        pointer1 = 0
        pointer2 = len(cleanStr) - 1
        while pointer1 <= pointer2:
            if cleanStr[pointer1] != cleanStr[pointer2]:
                return False
            
            pointer1 += 1
            pointer2 -= 1

        return True

s = Solution()

word = "AmanaplanaCanalpanama"
print(f"Is {word} a palindrome? {s.isPalindrome(word)}")

word = "raceacar"
print(f"Is {word} a palindrome? {s.isPalindrome(word)}")
