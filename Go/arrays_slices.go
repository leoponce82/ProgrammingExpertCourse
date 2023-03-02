package main

import "fmt"

func main() {
	arr := []bool{} // def an empty array type bool
	arr2 := []bool{true, false, true}
	arr = append(arr, arr2...) // ... are like splat in python
	fmt.Println(arr)

	test(arr2)

	for i, val := range arr2 {
		fmt.Println(i, val)
	}

}

func test(x []bool) { // accepts a slice with any number of elements inside it
	x[0] = false
}

// it changed the slices [0] value, this doesnot work on arrays bc 
//when you pass an array to a func, a copy is passed and the original is not modified.
// array example: arr2 := [3]bool{true, false, true}
