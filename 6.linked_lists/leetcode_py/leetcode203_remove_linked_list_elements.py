"""
LEETCODE PROBLEM #203. Remove Linked List Elements

Description Directly from: https://leetcode.com/problems/remove-linked-list-elements/

Constraints:
* The number of nodes in the list is in the range [0, 5 * 104].
* -105 <= Node.val <= 105
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return
        prev = None
        curr = head
        while curr:
            # If we have to remove the head
            if curr.val == val and curr == head:
                curr = head.next
                head = curr
            elif curr.val == val:  # Any other besides the head
                prev.next = curr.next
                curr = curr.next
            elif curr.val != val:  # Keep moving
                prev = curr
                curr = curr.next

        return head


s = Solution()
s.removeElements()
