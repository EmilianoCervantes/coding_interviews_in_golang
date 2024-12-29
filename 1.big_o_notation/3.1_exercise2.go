package main

// What is the Big O of the below function?
func AnotherFunChallenge(input int) {
	example := 5
	example2 := 10
	example3 := 50

	println(example, example2, example3)

	for i := 0; i < input; i++ {
		x := i + 1
		y := i + 2
		z := i + 3

		println(x, y, z)
	}

	for i := 0; i < input; i++ {
		p := i * 2
		q := i * 2
		println(p, q)
	}

	whoAmI := "I don't know"

	println(whoAmI)
}
