"""
LEETCODE PROBLEM #680 - Valid Palindrome II

Description Directly from: https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome_deprecated(self, s: str) -> bool:
        """
        Works for ALMOST all questions
        Has trouble with when to move the pointers.

        What are we missing?
        """
        free_pass = True

        p1, p2 = 0, len(s)-1

        while p1 <= p2:
            if s[p1] != s[p2]:
                if free_pass:
                    free_pass = False
                    # Check which one has to continue
                    # Sneak peak
                    if s[p1] == s[p2-1]:
                        p2 -= 1
                    elif s[p1+1] == s[p2]:
                        p1 += 1
                    else:
                        return False
                    continue
                else:
                    return False
            p1 += 1
            p2 -= 1

        return True

    def validate_sub_palindrome(self, s: str, p1: int, p2: int) -> bool:
        if len(s) < 2:
            return True

        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        """
        The other solution was missing to not go one way or another.

        ACTUALLY go BOTH ways.

        Let's see the changes inside the if. Btw, no free_pass this time
        """
        if len(s) < 2:
            return True

        p1, p2 = 0, len(s)-1

        while p1 <= p2:
            if s[p1] != s[p2]:
                # Check for s[p1] == s[p2-1]:
                # Check for s[p1+1] == s[p2]:
                return self.validate_sub_palindrome(s, p1, p2-1) or self.validate_sub_palindrome(s, p1+1, p2)
            p1 += 1
            p2 -= 1

        return True


s = Solution()

print(f"res for \"aba\": {s.validPalindrome("aba")}")
print(f"res for \"eceec\": {s.validPalindrome("eceec")}")
