# Linked Lists

Also called singly linked lists.

Is a data structure composed of nodes.

## Parts of a Linked List

1. A head - which is a node
2. A tail - which is a node
3. And _n_ number of nodes in between

## Parts of a Node

1. A value.
2. Pointer to the **next** node.

If the node we are looking at is the tail, then the pointer will be **`null`**.

# Doubly Linked Lists

Similar to the linked lists, just that the nodes point to both the next and the previous nodes.

## Parts of a Doubly Linked List

1. A head - which is a node
2. A tail - which is a node
3. And _n_ number of nodes in between

## Parts of a Node

1. A value.
2. Pointer to the _next_ node.
3. Pointer to the _previous_ node.

- If the node we are looking at is the _head_, then the pointer named _previous_ will be **`null`**.
- If the node we are looking at is the _tail_, then the pointer named _next_ will be **`null`**.

# Why Linked Lists?

While search and insertion might be O(n).

Inserting/Deleting a node in between other 2 doesn't involve moving elements like in an array.

Shift and unshift are also not that complicated.

## When to use SLL v.s. DLL?

While DLL are also `O(n)` for searching, they are technically faster.

- You can start the search either from the head or the tail.
- Doesn't matter if we kinda lose the head, we can search for it.
  - In the case of SLL, we are kinda doomed if we lose track of the head.

The downside is that they use more memory, as the reference to both _previous_ and _next_ is there.

### Use cases

1. SLL
   1. More insertions and deletions than searches.
2. DLL
   1. More memory.

# Not coding Doubly Linked Lists

For starters, Singly Linked Lists are tougher to code and to think about than Doubly Linked Lists.

- Once you code a SLL, a DLL is a lot easier. Specially remove and revert.

I encourage you to try, it's a good exercise nevertheless.

What is most important to me is for you to see the logic when coding a Linked List and all things you need to consider in my somewhat lengthy functions (which I know can be improved, but I opted to be thorough).
