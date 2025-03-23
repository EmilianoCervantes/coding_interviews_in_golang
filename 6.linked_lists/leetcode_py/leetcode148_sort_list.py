"""
LEETCODE PROBLEM #148. Sort List

Description Directly from: https://leetcode.com/problems/sort-list/description/

Constraints:
* The number of nodes in the list is in the range [1, 104]
* 0 <= Node.val <= 9
* The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list = []  # Using an array for support and later sort values

        while head:
            list.append(head.val)
            head = head.next

        list.sort()  # In "module 11" we see sorting, reference to that to see how you could do it manually

        head = curr = ListNode()
        for val in list:
            curr.next = ListNode(val)
            curr = curr.next

        return head.next


s = Solution()
s.sortList()
