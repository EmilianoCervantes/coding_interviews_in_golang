"""
LEETCODE PROBLEM #2816. Double a Number Represented as a Linked List

Description Directly from: https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

You are given the head of a non-empty linked list representing a non-negative integer without leading zeroes.

Return the head of the linked list after doubling it.

Constraints:
* The number of nodes in the list is in the range [1, 104]
* 0 <= Node.val <= 9
* The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.
"""
import sys
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    sys.set_int_max_str_digits(100000)

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Steps:
        1) Get the full number as a string
        2) Transform to number and double it
        3) Transform it back as a string and split it OR don't split it.
        4) Each char in the string put it in a node.
        """
        if not head:
            return

        # Step 1
        original_number = ""
        while head:
            original_number += f"{head.val}"
            head = head.next

        # Steps 2 & 3
        # Error, had to add sys.set_int_max_str_digits()
        doubled_number = f"{int(original_number) * 2}"

        # Step 4
        new_head = curr_node = ListNode()
        for i in range(len(doubled_number)):
            curr_digit = doubled_number[i]
            curr_node.next = ListNode(int(curr_digit))
            curr_node = curr_node.next

        # Finally
        return new_head.next
