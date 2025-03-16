# Trees

So far we've seen linear data structures.

Trees have a **hierarchical** data structure.

Each child descends from only one parent.

## Real life examples of trees

1. File system.
2. Comments in posts - you can tell specially for comments inside comments.
3. Menus in  apps.

### Examples in programming

1. HTML - DOM.
2. Networking
3. While loop.

## Structure

We have **nodes** with any sort of information.

- There is a **root node**.
- The _root_ has **children nodes**.
- If those nodes have _children_, they are called **parent nodes** and they can point to multiple _child nodes_.
- The nodes at the same level are called _siblings_.
- Nodes that don't have any more children, area called **leaf nodes**. There's no more going forward.

## Types of trees

I won't cover everything (that would be crazy). But I'll go over the basic trees and algorithms needed for interviews.

Note: If you wanna know more, skip to the end of this file and check all types of trees.

## Binary Trees

Type of trees that follow the rules:

1. Each node has TWO children at most.
   1. If a node has 3 children, it is NOT a _binary tree_.
2. Each child only has one parent.

What we usually want to achieve is a _perfect binary tree_.

Not just fill the tree.

### Perfect Binary Tree

We will have the same (or really close) number of nodes in each level.

- Root - 1 <-- level 0
- 1st lvl - 2
- 2nd lvl - 4
- 3rd lvl - 8
- 4th lvl - 16
- nth lvl - **2^n** or **sum(_lvl_ 0 to _lvl_(n-1)) + 1**.

>Why put both formulas?

We could stick with _2^n_ and know how many nodes we have at the last level and that's it.

But if we take a good look at the second (and lets dissect it):

Formula: _sum(lvl 1 to lvl(n-1)) + 1_

1. We add the total of nodes of all previous levels except the current one / the one at the bottom.
2. If we take all the previous count of nodes and we add one, we get the total of the bottom level.

Maybe this explanation was too obvious... and I hope the next is obvious as well... that means that half our data is at the bottom of the tree.

Thus, we can have more efficient searches, resulting in:

1. Search - **O(logN)**
2. Insert - **O(logN)**
3. Delete - **O(logN)**

Going back to that first formula: _2^n_.

If we know the height of the tree, that means we know the # of nodes it contains.

`TotalOfNodes = 2^height`

Doing this backwards, the height of the tree would be: `height = log10(nodes)`.

>Why so much back and forth?

Because if we want to search for some data in a tree with 100 LEVELS...

`height = log10(100)`
`2 = log10(100)`

Where height is also the number of steps/times we need to take to find the item (or prove it doesn't exist).

- We just need to decide
- >Left or Right.

Back to the `2 = log(100)`, we would get the answer in 10 steps.

- If we did this with an _array_, we would need to check 100 times.

### Binary Search Tree

That bring us to the topic of searches.

**BSTs** are great for comparing and finding data.

>Why a _BST_ vs a _Dictionary_?

Different from a _Dictionary_, with a _BST_ we preserve the relationship between the data.

E.g. a folder in your computer.
You know that a _file system_ is an example of a tree, but why?

Because we want to know how files are related, keep them organized.
We don't want to jump between references to find what we are looking for.

#### How do BSTs work?

We know that for each node in a _Binary Trees_, they only have TWO children: a left and a right node.

NOW...

1. The _left node_ should be **smaller** in value than the _parent node_.
2. The _right node_ should be **greater** in value than the _parent node_.

BUT they still won't be enough to have search, insert, and delete in **O(logN)** times.

If you play with any BST visualizers online, you'll notice how bad it can get.

Spoiler alert: **O(n)**.

### Balanced Binary Search Trees

That's where balanced BSTs come in.

We want to keep a structure optimized.


#### Pros and cons of Balanced BSTs

Pros:

1. All operations are better than _O(n)_.
2. There's an order to the data.
   1. The data is sorted already. V.s. _arrays_ or _hash tables_.

Cons:

1. No _O(1)_ operations

## Heap



## Trie



## All types of trees

The general types are:

1. B-trees
2. Binary trees
3. Bit-slice trees
4. Heaps
5. Multi-way trees
6. Space-partitioning trees

See the [full list here](https://en.wikipedia.org/wiki/List_of_data_structures#Trees).

# Resources for this module

1. [Visual Go - BST](https://visualgo.net/en/bst)
