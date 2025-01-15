package main

import "fmt"

const skip = true

// Stack - remember it is LIFO
type Stack struct {
	data   []string
	length int // We can obviously do len(data) every time, I just like being more thorough while building our data structures
}

// See the element at the top of the Stack
func (stack Stack) peek() string {
	if stack.length == 0 {
		return ""
	}

	return stack.data[stack.length-1]
}

// Add a new element to the Stack
func (stack *Stack) push(newValue string) {
	stack.data = append(stack.data, newValue)
	stack.length++
}

// Take out the element at the top of the Stack
func (stack *Stack) pop() string {
	if stack.length > 0 {
		poppedValue := stack.peek()

		stack.data = stack.data[:stack.length-1]
		stack.length--

		return poppedValue
	}

	return ""
}

func (stack Stack) isEmpty() bool {
	if stack.peek() == "" {
		return true
	}

	return false
}

// Will be used for the Linked Lists as a Queue
type Node struct {
	value    string
	nextNode *Node
}

// Queue - remember it is FIFO
type Queue struct {
	firstElement *Node // head
	lastElement  *Node // tail
	length       int
}

// Insert a new element at the "end" of the queue
func (queue *Queue) enqueue(newValue string) {
	newNode := Node{value: newValue}

	if queue.length < 1 {
		queue.firstElement = &newNode
	} else {
		queue.lastElement.nextNode = &newNode
	}

	queue.lastElement = &newNode

	queue.length++
}

// Take out the oldest element in the queue
func (queue *Queue) dequeue() string {
	if queue.length > 0 {
		dequeuedValue := queue.firstElement.value

		queue.firstElement = queue.firstElement.nextNode // Will = nil if there is no next

		if queue.length == 1 {
			queue.lastElement = nil
		}

		queue.length--

		return dequeuedValue
	}

	return ""
}

func (queue Queue) peek() string {
	return queue.firstElement.value
}

func (queue Queue) isEmpty() bool {
	if queue.length < 1 {
		return true
	}

	return false
}

func Stacks101() {
	if skip {
		return
	}

	myStack := Stack{}
	fmt.Println("My first Stack:")
	fmt.Println(myStack)

	fmt.Println()
	fmt.Println("Let's add a new element:")
	myStack.push("My first value")
	fmt.Println(myStack)

	fmt.Println()
	fmt.Println("Let's add 2 new elements and then peek:")
	myStack.push("Another value")
	myStack.push("Third value")
	fmt.Println("Peeked at the stack:", myStack.peek())

	fmt.Println("And... full stack so far")
	fmt.Println(myStack)

	fmt.Println()
	fmt.Println("Now let's start popping")
	fmt.Println("Length before popping:", myStack.length)

	originalLength := myStack.length // We have to do this, otherwise you'll have a bug in your for loop.
	for i := 0; i < originalLength; i++ {
		message := fmt.Sprintf("Pop #%d: %s", i+1, myStack.pop())
		fmt.Println(message)
		fmt.Println("Length now after popping:", myStack.length)
	}

	fmt.Println("What's left in the stack?")
	fmt.Println(myStack)
	fmt.Println("Let's pop once more:", myStack.pop()) // It returns nothing cause there is nothing else to pop

	fmt.Println("Why didn't we see anything?")
	fmt.Println("Cause it is empty:", myStack.isEmpty())
	fmt.Println(myStack)
}

func Queues101() {
	if skip {
		return
	}

	myQueue := Queue{}

	fmt.Println("My first Queue:")
	fmt.Println(myQueue)

	fmt.Println()
	fmt.Println("Let's add a new element:")
	myQueue.enqueue("My first value")
	fmt.Println("First element:", myQueue.firstElement)
	fmt.Println("Last element:", myQueue.lastElement)
	fmt.Println("Current length:", myQueue.length)
	fmt.Println(myQueue)

	fmt.Println()
	fmt.Println("Let's add a second element to our queue:")
	myQueue.enqueue("A second element")
	fmt.Println("First element:", myQueue.firstElement)
	fmt.Println("Last element:", myQueue.lastElement)
	fmt.Println("Current length:", myQueue.length)

	fmt.Println()
	fmt.Println("Let's add a third element to our queue:")
	myQueue.enqueue("Third element")
	fmt.Println("Last element:", myQueue.lastElement)
	fmt.Println("Current length:", myQueue.length)

	fmt.Println()
	fmt.Println("And a 4th:")
	myQueue.enqueue("4th element")
	fmt.Println("Last element:", myQueue.lastElement)
	fmt.Println("Current length:", myQueue.length)

	fmt.Println()
	fmt.Println("What will we get if we peek in a queue?")
	fmt.Println(myQueue.peek())
	fmt.Println("It should've been the element we will take out if we run dequeue()")

	fmt.Println()
	fmt.Println("Now let's start dequeuing:")

	totalLength := myQueue.length

	for i := 0; i < totalLength; i++ {
		message := fmt.Sprintf("Dequeue #%d: %s", i+1, myQueue.dequeue())
		fmt.Println()
		fmt.Println(message)
		fmt.Println("Length now after dequeuing:", myQueue.length)
	}

	fmt.Println()
	fmt.Println("If we try dequeuing one more time, we get (you guessed it):", myQueue.dequeue())

	fmt.Println("Cause it is empty:", myQueue.isEmpty())
	fmt.Println(myQueue)
}

func main() {
	Stacks101()
	Queues101()
}
