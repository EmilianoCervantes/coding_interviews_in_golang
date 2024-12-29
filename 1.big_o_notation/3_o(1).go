package main

func getFirstBox(boxes []string) string {
	return boxes[0]
}

func getCarModel(c car) string {
	return c.model
}

type car struct {
	Make  string
	model string
	Year  int
}

/**
 * O(1) - Constant Time
 * We are only doing one operation, regardless of the size of the input
 * Thus, the time taken by the function is constant.
 */
func Oof1() {
	boxes := []string{}
	getFirstBox(boxes)

	myCar := car{}
	model := getCarModel(myCar)
	println(model)
}
