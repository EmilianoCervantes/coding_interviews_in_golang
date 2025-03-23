"""
LEETCODE PROBLEM #641. Design Circular Deque
Note: Deque means = Double-ended queue

Description Directly from: https://leetcode.com/problems/design-circular-deque/

Design your implementation of the circular double-ended queue (deque).

Implement the MyCircularDeque class:

* MyCircularDeque(int k) Initializes the deque with a maximum size of k.
* boolean insertFront() Adds an item at the front of Deque. Returns true if the operation is successful, or false otherwise.
* boolean insertLast() Adds an item at the rear of Deque. Returns true if the operation is successful, or false otherwise.
* boolean deleteFront() Deletes an item from the front of Deque. Returns true if the operation is successful, or false otherwise.
* boolean deleteLast() Deletes an item from the rear of Deque. Returns true if the operation is successful, or false otherwise.
* int getFront() Returns the front item from the Deque. Returns -1 if the deque is empty.
* int getRear() Returns the last item from Deque. Returns -1 if the deque is empty.
* boolean isEmpty() Returns true if the deque is empty, or false otherwise.
* boolean isFull() Returns true if the deque is full, or false otherwise.


Constraints:
* 1 <= k <= 1000
* 0 <= value <= 1000
* At most 2000 calls will be made to insertFront, insertLast, deleteFront, deleteLast, getFront, getRear, isEmpty, isFull.
"""


class ListNode:
    def __init__(self, value=0, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class MyCircularDeque:
    def __init__(self, k: int):
        self.curr_size = 0
        self.max_size = k
        self.front = None
        self.last = None

    def insertFront(self, value: int) -> bool:
        new_node = ListNode(value)
        if self.isEmpty():
            self.front = new_node
            self.last = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            if self.isFull():
                return False

            new_node.prev = self.last
            new_node.next = self.front
            self.front.prev = new_node
            self.last.next = new_node
            self.front = new_node

        self.curr_size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isEmpty():
            return self.insertFront(value)
        else:
            if self.isFull():
                return False

            new_node = ListNode(value)
            new_node.prev = self.last
            new_node.next = self.front
            self.front.prev = new_node
            self.last.next = new_node
            self.last = new_node  # Only life diff from insertFront
            self.curr_size += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        # Only one node:
        if self.front == self.last:
            self.front = None
            self.last = None
            self.curr_size = 0
            return True

        # More than one node:
        self.front = self.front.next
        self.front.prev = self.last
        self.last.next = self.front
        self.curr_size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        # Only one node:
        if self.front == self.last:
            self.front = None
            self.last = None
            self.curr_size = 0
            return True

        self.last = self.last.prev
        self.last.next = self.front
        self.front.prev = self.last
        self.curr_size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.value

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.last.value

    def isEmpty(self) -> bool:
        return self.curr_size == 0

    def isFull(self) -> bool:
        return self.curr_size == self.max_size


# [
#   "MyCircularDeque"
#   ,"insertFront"
#   ,"deleteLast"
#   ,"getRear"
#   ,"getFront"
#   ,"getFront"
#   ,"deleteFront"
#   ,"insertFront"
#   ,"insertLast"
#   ,"insertFront"
#   ,"getFront"
#   ,"insertFront"
# ]
# [4],[9],[],[],[],[],[],[6],[5],[9],[],[6]
myCircularDeque = MyCircularDeque(4)
print(f"insertFront(1): {myCircularDeque.insertFront(9)}")  # return True
print(f"deleteLast(0): {myCircularDeque.deleteLast(0)}")  # return True
print(f"getRear(): {myCircularDeque.getRear()}")  # return 1
print(f"getFront(): {myCircularDeque.getFront()}")  # return True
print(f"getFront() : {myCircularDeque.getFront()}")     # return 8
print(f"deleteFront() : {myCircularDeque.deleteFront()}")      # return 1
print(f"insertLast(2) : {myCircularDeque.insertLast(2)}")  # return True
print(f"insertLast(0): {myCircularDeque.insertLast(0)}")  # return True
print(f"insertLast(4) : {myCircularDeque.insertLast(4)}")    # return True
print(f"deleteLast() : {myCircularDeque.deleteLast()}")    # return True
# print(f"getFront() : {myCircularDeque.getFront()}")    # return 1
# print("----- ----- ----- -----")
# print(f"front.prev.prev: {myCircularDeque.front.prev.prev.value}")
# print(f"front.prev: {myCircularDeque.front.prev.value}")
# print(f"front: {myCircularDeque.front.value}")
# print(f"front.next: {myCircularDeque.front.next.value}")
# print(f"front.next.next: {myCircularDeque.front.next.next.value}")
# print(f"front.next.next.next: {myCircularDeque.front.next.next.next.value}")
# print(f"front.next.next.next.next: {myCircularDeque.front.next.next.next.next.value}")
# print(f"last: {myCircularDeque.last.value}")
# print("----- ----- ----- -----")
