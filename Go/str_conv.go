package main

import (
	"fmt"
	"strconv"
)

func main() {
	output := MultiplyByString("22", 5)
	fmt.Print(output)
}

func MultiplyByString(str string, number int) int {
	// Write your code here.
	x, err := strconv.Atoi(str)
	fmt.Print(err)
	res := x * number
	return res
}
