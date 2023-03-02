package main

import (
	"fmt"
)

func main() {
	str := "hello"
	for index, element := range str{
		fmt.Println(index, element)
		fmt.Printf("%c\n", element)
	}
}

