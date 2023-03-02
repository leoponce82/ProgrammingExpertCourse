package main
import "fmt"

func main() {
	output := NestedSliceSum([][]int{{3, 4, 5}, {-3, -4, -5}, {-1, -1, 0}, {-4, 25}})
	fmt.Println(output)

}

func NestedSliceSum(numbers [][]int) []int {
	// Write your code here.
	res := 0
	res_slice := []int{}
	for _, each_slice := range numbers{
		res = 0
		for _, each_number := range each_slice{
			res = res + each_number
		}
		res_slice = append(res_slice, res)
	}

	return res_slice
}

