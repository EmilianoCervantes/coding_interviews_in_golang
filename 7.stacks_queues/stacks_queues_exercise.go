package main

/**
 * Challenge
 *
 * Code the structure and functions of the Stack and Queue based on what you read in the README.md and the notes in here.
 * Remember you already have a solution for Linked Lists on the previous section.
 */

// Stack - remember it is LIFO
type _Stack struct{}

// See the element at the top of the Stack
func (stack _Stack) _peek() {
}

// Add a new element to the Stack
func (stack *_Stack) _push() {
}

// Take out the element at the top of the Stack
func (stack *_Stack) _pop() {
}

// Will be used for the Linked Lists in the Queue
type _Node struct{}

// Will be used for creating a Queue
type _SinglyLinkedList struct{}

// Queue - remember it is FIFO
type _Queue struct{}

// Insert a new element at the "end" of the queue
func (queue *_Queue) _enqueue() {
}

// Take out the oldest element in the queue
func (queue *_Queue) _dequeue() {
}
