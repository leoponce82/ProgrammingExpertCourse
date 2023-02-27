package main

import ("fmt"
"strconv"
)

func main() {
	const x_const float64 = 12
	x := "Hello"    // Implicit asignment
	y := float64(69.69) // Implicit asignment and type casting [int -> float]
	fmt.Printf("%T", y)
	fmt.Println()
	fmt.Println(x, "World", x_const)
	str := fmt.Sprintf("%v", y)
	fmt.Println(str)

	j := "1234"
	j_value, err := strconv.Atoi(j)
	fmt.Println(j_value, err)

	str = "12345"
	a, err := strconv.ParseInt(str, 10, 64)
	fmt.Println(a, err)

}  
