# Stacks and Queues

These are linear data structures.

Different from the previous structures we've seen, for these two you'll notice we can only see one value at a time.

It is tied to their usual purposes.

# Stacks

**LIFO** or _Last in, first out_.

## Real life examples

1. Groceries at the market. Good shoppers get the latest supplied.
   1. Also sellers usually get a harder time selling older items.
2. Getting items from a pile.
3. Getting in and exiting a cab.
4. Anything stored in a box.
5. Plates in your kitchen.

### Programming examples

1. Browser history.
2. Undoing changes.

## Fun facts

Google _stack overflow_.
- Not the site, but the term.

# Queues

**FIFO** or _First in, first out_.

## Real life examples

1. Line at the bank.
2. Purchasing tickets.
3. Printing.

Pretty much, anything that makes a line in this world.

### Programming examples

1. Requests.
2. Messages.
3. Uber rides.

# A more real programming life example

## The _JavaScript Runtime Environment_

It has (among other things) a **call `stack`** and a **callback `queue`**.

# Important Note regarding how to implement Stacks and Queues

Not to hurt anybody, but I've seen courses like this [Udemy supposed masterclass](https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/) which uses arrays for pretty much anything.

While I agree it is super easy to use an array to go and implement a Stack or a Queue.
The performance of your algorithms will plummet like crazy, which goes the opposite way of what these structures should be helping you with.

## Counter point

While using `arrays` for `queues` is definitely a bad choice, you can use `arrays` for stacks.

### Stacks is push and pop

Push and pop in arrays is O(1) so no issues there.
- And it's technically faster than a Linked List as the items are next to each other in memory.

## Queues is enqueue and dequeue

Enqueue being a sort of unshift - so arrays are not doable, we want a O(1) operation.
- Linked Lists in this case are the way to go.

Dequeue being a sort of pop is O(1)
- Using Linked Lists we can also easily achieve this.
