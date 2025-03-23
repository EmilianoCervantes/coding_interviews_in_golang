"""
LEETCODE PROBLEM #160. Intersection of Two Linked Lists

Description Directly from: https://leetcode.com/problems/intersection-of-two-linked-lists/

Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """"
        Intersection occurs when the nodes are the same.
        NOT the same value.
        But the same reference.

        In Python3 node1 == node2 will suffice
        """
        if not headA or not headB:
            return

        nodes_set = set()
        while headA:
            nodes_set.add(headA)
            headA = headA.next
        while headB:
            if headB in nodes_set:
                return headB
            else:
                headB = headB.next

        return


s = Solution()
# intersectVal = 8
listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
# skipA = 2
# skipB = 3
print(f"res: {s.reverseList(listA, listB)}")
