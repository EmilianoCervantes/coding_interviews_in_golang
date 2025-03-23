"""
LEETCODE PROBLEM #206. Reverse Linked List

Description Directly from: https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Constraints:
* The number of nodes in the list is the range [0, 5000].
* -5000 <= Node.val <= 5000
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            # You can avoid this if by returning "prev"
            # I just failed to notice
            if not next:
                break
            curr = next

        return curr


s = Solution()
head = [1, 2, 3, 4, 5]
print(f"res: {s.reverseList(head)}")
