package main

import (
	"fmt"
)

/**
 * Implementation of a hash table in Go
 */

// SEE how things CHANGE when you change this number:
const SizeOfHashTable = 50 // <- play with it

type HashTable struct {
	// [how_many_items_our_hash_table_can_contain][let's simulate a linked list][key-value pair]
	data [SizeOfHashTable][][2]string
}

func hash(key string) int {
	hash := 0

	for i := 0; i < len(key); i++ {
		charToNum := int(rune(key[i]))

		hash = (hash + charToNum*i) % SizeOfHashTable
	}

	return hash
}

func (ht *HashTable) set(key string, value string) {
	hashedKey := hash(key)

	keyValuePair := [2]string{key, value}
	arrToPush := [][2]string{keyValuePair}

	if len(ht.data[hashedKey]) == 0 {
		ht.data[hashedKey] = arrToPush
	} else {
		ht.data[hashedKey] = append(ht.data[hashedKey], keyValuePair)
	}
}

func (ht HashTable) get(key string) string {
	hashedKey := hash(key)

	if len(ht.data[hashedKey]) == 0 {
		return ""
	}

	hashEntry := ht.data[hashedKey]

	for i := 0; i < len(hashEntry); i++ {
		keyValuePair := hashEntry[i]
		if keyValuePair[0] == key {
			return keyValuePair[1]
		}
	}

	return ""
}

func keyValueExtract(ht HashTable, keyOrValue int) []string {
	elements := []string{}

	for i := 0; i < len(ht.data); i++ {
		if len(ht.data[i]) > 0 {
			for j := 0; j < len(ht.data[i]); j++ {
				elements = append(elements, ht.data[i][j][keyOrValue])
			}
		}
	}

	return elements
}

func (ht HashTable) keys() []string {
	return keyValueExtract(ht, 0)
}

func (ht HashTable) values() []string {
	return keyValueExtract(ht, 1)
}

func main() {
	myHashTable := HashTable{}

	myHashTable.set("oranges", "I'm a value")
	myHashTable.set("jackets", "999")
	oranges := myHashTable.get("oranges")
	jackets := myHashTable.get("jackets")

	fmt.Println("Res for oranges:", oranges)
	fmt.Println("Res for oranges:", jackets)
	fmt.Println()

	fmt.Println("myHashTable.data length", len(myHashTable.data))
	fmt.Println("myHashTable.data", myHashTable)
	fmt.Println("ALL myHashTable KEYS:", myHashTable.keys())
	fmt.Println("ALL myHashTable VALUES:", myHashTable.values())
}
