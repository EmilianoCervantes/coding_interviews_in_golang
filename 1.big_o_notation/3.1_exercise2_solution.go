package main

// What is the Big O of the below function?
// Big O = O(1)+O(1)+O(1)+O(1) + O(n)+O(n)+O(n)+O(n)+O(n)+O(n)+O(n)
// Big O = O(4) + O(7n)
// Big O = O(1) + O(n)
// Big O = O(1) + O(n)
// Big O = O(n)
func AnotherChallengeSolution(input int) {
	a := 5  // O(1) just assigning a variable
	b := 10 // O(1)
	c := 50 // O(1)

	println(a, b, c)

	for i := 0; i < input; i++ { // O(n)
		x := i + 1 // O(n) because it is inside the loop
		y := i + 2 // O(n)
		z := i + 3 // O(n)

		println(x, y, z)
	}

	for i := 0; i < input; i++ { // O(n)
		p := i * 2 // O(n)
		q := i * 2 // O(n)
		println(p, q)
	}
	whoAmI := "I don't know" // O(1)

	println(whoAmI)
}
