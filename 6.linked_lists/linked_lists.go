package main

import "fmt"

type Node struct {
	value    string
	nextNode *Node
}

type SinglyLinkedList struct {
	head   *Node
	length int
}

func (list *SinglyLinkedList) push(newValue string) { // O(n) BUT...
	// We could make this  // O(1) if we are allowed to add the property "tail *Node" as part of the SLL in the interview
	// Or you might be asked, how would this work/change if you have no "tail" property.

	newNode := Node{value: newValue}
	if list.length == 0 { // O(1)
		list.head = &newNode
		list.length++
		return
	}

	currentNode := list.head

	for i := 0; i < list.length; i++ { // O(n) because I made things trickier by not keeping track of the tail as a property
		if i == list.length-1 {
			currentNode.nextNode = &newNode
			list.length++
			return
		}

		currentNode = currentNode.nextNode
	}
}

func (list *SinglyLinkedList) insert(newValue string, insertPosition int) { // O(n) BUT...
	// If we insert at position 0 = "unshift", it is O(1), contrary to arrays.

	newNode := Node{value: newValue}

	if insertPosition == 0 { // O(1)
		if list.head == nil {
			list.head = &newNode
		} else {
			temp := list.head
			list.head = &newNode
			list.head.nextNode = temp
		}

		list.length++
	} else { // O(n)
		currentNode := list.head

		for i := 1; i < list.length; i++ {
			// Connect the node previous to the target position
			// And point to the added node the original next node
			if i == insertPosition {
				nextNode := currentNode.nextNode
				currentNode.nextNode = &newNode
				newNode.nextNode = nextNode
			}
			// } else if i == list.length-1 { // We reached the end of the linked list cause the insert position was greater
			// 	currentNode.nextNode = &n
			// }

			currentNode = currentNode.nextNode
		}

		list.length++
	}
}

func (list *SinglyLinkedList) removeAt(position int) string { // O(n)
	valueErased := ""
	currentNode := list.head

	if list.length == 0 {
		return valueErased
	}

	if position <= 0 {
		list.head = list.head.nextNode
	}

	for i := 1; i < list.length; i++ {
		if i == position {
			// Ex position 1:
			// currentNode == head
			nodeToBeRemoved := currentNode.nextNode
			currentNode.nextNode = nodeToBeRemoved.nextNode
			list.length--
			return nodeToBeRemoved.value
		}

		currentNode = currentNode.nextNode
	}

	return valueErased
}

// Will make it so head <- node2 <- node3 ... <- tail
// The tail will be the new head
func (list *SinglyLinkedList) revert() { // O(n)
	if list.head == nil {
		return
	}

	// You can also use list.head.next == nil
	// Or combine both conditions into list.length <=1
	// Depends on your **interview** questions!
	if list.length == 1 {
		return
	}

	currentNode := list.head         // node 3
	nextNode := currentNode.nextNode // node 4

	currentNode.nextNode = nil

	for i := 0; i < list.length; i++ { // i = 3, length = 4
		if nextNode != nil {
			tempNode := nextNode.nextNode // nil

			nextNode.nextNode = currentNode // Node 4 points to node 3 instead of nil

			currentNode = nextNode // current = node 4
			nextNode = tempNode    // next = nil
		}

		if i == list.length-1 { // i = 3
			list.head = currentNode // head = node 4
		}
	}
}

// Extremely similar to PrintAllItems()
func (list SinglyLinkedList) search(searchedValue string) { // O(n)
	currentNode := list.head
	counter := 0
	found := false
	for i := 0; i < list.length; i++ {
		if currentNode.value == searchedValue {
			found = true
			break
		} else {
			counter++
			currentNode = currentNode.nextNode
		}
	}

	if found {
		message := fmt.Sprintf("Value '%s' found at node with index %d", searchedValue, counter)
		fmt.Println(message)
	} else {
		message := fmt.Sprintf("Value '%s' NOT found", searchedValue)
		fmt.Println(message)
	}
}
func (list SinglyLinkedList) at(position int) *Node { // O(n)
	currentNode := list.head

	if list.length-1 < position {
		return nil
	}

	for i := 0; i < list.length; i++ {
		if i == position {
			return currentNode
		}

		currentNode = currentNode.nextNode
	}

	return nil
}

// Extremely similar to search()
func (list SinglyLinkedList) PrintAllItems() { // O(n)
	currentNode := list.head
	for i := 0; i < list.length; i++ {
		message := fmt.Sprintf("Node %d: %v, with value '%s'", i, currentNode, currentNode.value)
		fmt.Println(message)
		currentNode = currentNode.nextNode
	}
}

func main() {
	linkedList := SinglyLinkedList{}
	fmt.Println("Singly Linked List:", linkedList)
	fmt.Println("Singly Linked List length:", linkedList.length)
	fmt.Println("Singly Linked List head:", linkedList.head)

	fmt.Println()
	fmt.Println("Let's push our first node")
	linkedList.push("#1")
	fmt.Println("Singly Linked List:", linkedList)
	fmt.Println("Singly Linked List length:", linkedList.length)
	fmt.Println("Singly Linked List head:", linkedList.head)
	fmt.Println("Singly Linked List head value:", linkedList.head.value)

	fmt.Println()
	fmt.Println("Let's push our second node")
	linkedList.push("second node")
	fmt.Println("Singly Linked List length:", linkedList.length)
	fmt.Println("Singly Linked List at position 1:", linkedList.at(1))
	fmt.Println("Singly Linked List at position 1 - value:", linkedList.at(1).value)

	fmt.Println()
	fmt.Println("Let's push 2 more nodes")
	linkedList.push("node 3")
	linkedList.push("node 4")
	fmt.Println("And see all the values so far:")
	linkedList.PrintAllItems()

	fmt.Println()
	fmt.Println("Let's try inserting at index 2")
	linkedList.insert("I was inserted at index 2", 2)
	fmt.Println("And print again all nodes:")
	linkedList.PrintAllItems()

	fmt.Println()
	fmt.Println("Let's try removing at index 3")
	linkedList.removeAt(3)
	fmt.Println("And print again all after:")
	linkedList.PrintAllItems()

	fmt.Println()
	fmt.Println("Let's search for 2 different values")
	fmt.Println("Searching for '#1'")
	fmt.Println("And also let's search for 'node 3' that we just removed")

	valueToFind := "#1"
	linkedList.search(valueToFind)
	valueToFind = "node 3"
	linkedList.search(valueToFind)

	fmt.Println()
	fmt.Println("Let's remove all nodes but the first 2")
	linkedList.removeAt(linkedList.length - 1)
	linkedList.removeAt(linkedList.length - 1)
	fmt.Println("And print all nodes just to make sure")
	linkedList.PrintAllItems()

	fmt.Println()
	fmt.Println("For the final exercise, let's revert our Singly Linked List")
	linkedList.revert()
	linkedList.PrintAllItems()

	fmt.Println()
	fmt.Println("So far so good, it works with 2 items")

	fmt.Println()
	fmt.Println("Let's try with a 4 items")
	linkedList.push("node 3")
	linkedList.push("node 4")
	fmt.Println(" ----- BEFORE ----- ")
	linkedList.PrintAllItems()
	linkedList.revert()
	fmt.Println(" ----- AFTER ----- ")
	linkedList.PrintAllItems()
}
