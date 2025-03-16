/**
 * As you can probably tell from the title of this file,
 * I'll be going specifically over Balanced BSTs.
 * For more general info and how to go from Trees to just Balanced BSTs.
 * check the README of this section.
 */

package main

import "fmt"

type BinaryTreeNode struct {
	value int
	left  *BinaryTreeNode
	right *BinaryTreeNode
}

type BinaryTree struct {
	root *BinaryTreeNode
}

// First attempt
/** Avoid duplicated code between insert and search */
func searchHelper(value int, node *BinaryTreeNode) *BinaryTreeNode {
	if value < node.value {
		if node.left != nil {
			return searchHelper(value, node.left)
		}

		return node
	}

	if value > node.value {
		if node.right != nil {
			return searchHelper(value, node.right)
		}
		return node
	}

	// So we can use it for insert and search
	return node
}

// First attempt
func (binaryTree *BinaryTree) insert(value int) {
	newNode := BinaryTreeNode{value: value}

	if binaryTree.root == nil {
		binaryTree.root = &newNode
	} else {
		// We need to traverse the tree
		parentNode := searchHelper(value, binaryTree.root)

		if value < parentNode.value {
			parentNode.left = &newNode
		} else if value > parentNode.value {
			parentNode.right = &newNode
		}
		// If there's a node with that value already, I don't want duplicates
	}
}

// First attempt
/**
 * True if removed successfully
 * False if it doesn't exist or there was an issue
 */
func (binaryTree *BinaryTree) remove(value int) bool {
	if binaryTree.root == nil {
		return false
	}

	var parentNode *BinaryTreeNode = nil
	currentNode := binaryTree.root

	for currentNode != nil {
		if value < currentNode.value {
			parentNode = currentNode
			if currentNode.left != nil {
				currentNode = currentNode.left
				continue
			}
			break
		} else if value > currentNode.value {
			parentNode = currentNode
			if currentNode.right != nil {
				currentNode = currentNode.right
				continue
			}
			break
		} else if value == currentNode.value {
			// Value found
			fmt.Println("Parent node:", parentNode)
			fmt.Println("Current node:", currentNode)
			break
		}
	}

	return false
}

// First attempt
func (binaryTree BinaryTree) search(value int) bool {
	if binaryTree.root == nil {
		return false
	}
	// We need to traverse the tree
	nodeResponse := searchHelper(value, binaryTree.root)

	if nodeResponse != nil {
		return nodeResponse.value == value
	}

	return false
}

func traverse(node *BinaryTreeNode) *BinaryTree {
	if node == nil {
		return nil
	}

	binaryTree := BinaryTree{root: node}

	// Print this pre-order to reconstruct the Tree
	fmt.Print(node.value, " -> ")

	if node.left != nil {
		traverse(node.left)
	}

	if node.right != nil {
		traverse(node.right)
	}

	return &binaryTree
}

// Implementing String() for a standardized print
// func (binaryTree BinaryTree) String() string {
// 	if binaryTree.root == nil {
// 		return "BinaryTree{Root: nil}"
// 	}
// 	allValues := fmt.Sprintf("BinaryTree{Root: '%d'}\n", binaryTree.root.value)
// 	currentNode := binaryTree.root.left
// 	for currentNode != nil {
// 		allValues += fmt.Sprintf("To the left: %d\n", binaryTree.root.left.value)
// 		currentNode = currentNode.left
// 	}
// 	return allValues
// }

/**
			9
	4				 20
1		6		15		170
*/

func BinaryTrees() {
	binaryTree := BinaryTree{}
	binaryTree.insert(9)
	binaryTree.insert(4)
	binaryTree.insert(20)
	binaryTree.insert(1)
	binaryTree.insert(6)
	binaryTree.insert(15)
	binaryTree.insert(170)
	traverse(binaryTree.root)
	fmt.Print("\n\n")
	fmt.Println("Searching for 20:", binaryTree.search(20))
	fmt.Println("Searching for 21:", binaryTree.search(21))
	fmt.Println("Searching for 170:", binaryTree.search(170))
	fmt.Println("Searching for 200:", binaryTree.search(200))
	fmt.Println("Searching for 15:", binaryTree.search(15))
	fmt.Println("Searching for 6:", binaryTree.search(6))
	fmt.Println()
	// fmt.Println("Removing 9:", binaryTree.remove(9))
	// fmt.Println("Removing 20:", binaryTree.remove(20))
	// fmt.Println("Removing 21:", binaryTree.remove(21))
	fmt.Println("Removing 21:", binaryTree.remove(170))
	traverse(binaryTree.root)
	fmt.Print("\n\n")
}

func main() {
	BinaryTrees()
}
