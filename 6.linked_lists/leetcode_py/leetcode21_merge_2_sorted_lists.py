"""
LEETCODE PROBLEM #21. Merge Two Sorted Lists

Description Directly from: https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Constraints:
* The number of nodes in both lists is in the range [0, 50].
* -100 <= Node.val <= 100
* Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return

        # This feels like a repeat of the last piece (line 54)
        # I don't recommend adding this duplicated logic
        # if not list1:
        #     return list2
        # if not list2:
        #     return list1

        head = ListNode()
        curr_node = head

        while list1 and list2:
            if list1.val < list2.val:
                curr_node.next = list1
                list1 = list1.next
            else:
                curr_node.next = list2
                list2 = list2.next

            curr_node = curr_node.next

        curr_node.next = list1 or list2

        return head.next


s = Solution()
list1 = [1, 2, 4]
list2 = [1, 3, 4]
print(f"res: {s.mergeTwoLists(list1, list2)}")
