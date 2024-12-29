package main

func anotherFunction() {}

// What is the Big O of the below function?
func FunChallenge(input []string) int {
	a := 10
	a = 50 + 3

	for i := 0; i < len(input); i++ {
		anotherFunction()
		stranger := true
		println(stranger)
		a++
	}

	return a
}
