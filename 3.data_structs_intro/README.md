# Let's dive into what is a data structure

This is a short module.

It's a theoretical one, just trying to explain/refresh people about what a data structure is.

## Skip this readme if

If you are already familiar with data structures, feel free to skip this module.

1. You feel you have a data structures foundation
2. You googled and got the answers you needed and you are able to explain what a data structure is.

## What is a Data Structure?

1. Collection of values
2. A format that defines how those values/data is organized, stored, and processed by any computer.
3. There are different data structures, each with their own applications and use cases.
4. Don't use the same data structure over and over for everything. PLEASE.

## How computers store data

Computers are made up of:

1. A CPU - interprets, processes, and executes instructions, it's where all sorts of calculations happen.
   - There's also [CPU cache](https://en.wikipedia.org/wiki/CPU_cache) but it only stores a tiny amount of data (the most recent).
2. RAM - temporary storage where variables usually live.
3. Storage - persistent storage in any shape of drives (hard drives, USB drives, memory sticks, SSDs, disks, etc. you google it) for saving all kinds of files.

The CPU accesses both the RAM and storage.

For example:

When doing

```go
example := "example"
```

What happens is that the CPU processes the instructions which in this case they assign a text to a variable.

And for a simple process like that, we keep the variable in memory in the RAM, so we can quickly access it as we need it.

But let's say we interact with a file

```go
example, err := os.ReadFile("/tmp/example")
...
err := os.WriteFile("/tmp/example1", example, 0644)
```

Then we are accessing data in the storage.

### RAM and data structures

RAM for example, uses data structures to organize and store all the data it has to process.

### Data Structures and the CPU

The way we build our code and our structures to keep track of the data we are manipulating makes it harder or easier for the CPU to go and look for that information.
How much time it takes for the CPU for writing/reading the data we want to manipulate.

## Different Languages, different Data Structures?

The way programming languages represent data structures can vary.

Also the methods will vary depending on the language you are coding with.

But that doesn't really matter as we can go and build our own implementation of the data structures we want to use.

You can use what's already built-in the language, and also you can search how efficient it is and give it a go to do your own implementation.

## Operations

As you are manipulating data in [almost any data structure you can](https://www.bigocheatsheet.com/):

1. Access the data,
2. Search for it,
3. Insert new data, &
4. Delete it.

While those are the basic, there're also other 2 day-to-day operations similar to search.

1. Traversing - visiting each element in order for any process where every element is involved.
2. Sorting

## Resources

1. [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)