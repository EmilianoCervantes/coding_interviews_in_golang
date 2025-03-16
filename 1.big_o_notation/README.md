# Big O Notation

We use Θ (Theta) notation is used to describe the, roughly, behaviors of the algorithms.

But we cannot always put in simple mathematical terms the behavior, so the try to grasp the worst and best cases.

If we identify either or both of them, we write them like this:

- Big O notation is to specify the worst case scenario for the algorithm.
  - E.g. O(n) "X" algorithm **runs in time at most n**, at most in linear time.
  - This is the upper bound.
- And Ω (Omega) notation to describe the best case scenario.
  - Lower bound.

The worst, average, and best scenarios can be the same.
- If we describe an algorithm as **Θ(_x_)**, we mean that its running time grows exactly like **Θ(_x_)**.
- So... does Θ(n²) imply O(n²)?
  - Yes.
  - But the opposite ISN'T the same.

If we describe an algorithm as _O(n²)_, that only refers to the worst case.
- It will take at most _O(n²)_.
- But it could be faster.

## In place algorithms

An algorithm is **in place** if it does not require extra memory.
- Except a constant amount of memory units.

# Resources for this module

1. [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)
