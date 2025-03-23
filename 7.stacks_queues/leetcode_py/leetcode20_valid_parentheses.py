"""
LEETCODE PROBLEM #20. Valid Parentheses

Description Directly from: https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Constraints:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        We have 2 classes of parenthesis
        Opening and closing

        We can use a Stack: LIFO approach
        Append opening brackets.

        Pop when there's a closing one.

        If there's a mismatch when popping,
        or the stack is NOT empty by the end,
        It is NOT valid.
        """
        stack = []  # Remember an array is okay for implementing a stack

        for c in s:
            match c:
                case "(" | "[" | "{":
                    stack.append(c)
                case ")":
                    if not len(stack):
                        return False
                    value = stack.pop()
                    if value != "(":
                        return False
                case "]":
                    if not len(stack):
                        return False
                    value = stack.pop()
                    if value != "[":
                        return False
                case "}":
                    if not len(stack):
                        return False
                    value = stack.pop()
                    if value != "{":
                        return False
                case _:
                    pass

        return len(stack) == 0


s = Solution()
input = "()"
print(f"res: {s.isValid(input)}")

input = "()[]{}"
print(f"res: {s.isValid(input)}")

input = "(]"
print(f"res: {s.isValid(input)}")

input = "(((()))"
print(f"res: {s.isValid(input)}")

input = "([])"
print(f"res: {s.isValid(input)}")

input = "]"
print(f"res: {s.isValid(input)}")
