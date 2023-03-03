package main

import "fmt"

func main(){
	output := MergeMaps(map[int][]string{175: {"Tim", "Clement"}, 180: {"Antoine"}}, map[int][]string{27: {"Clement", "Antoine"}, 21: {"Tim"}})
	fmt.Println(output)
}

func MergeMaps(heights map[int][]string, ages map[int][]string) map[string][]int {
	// Write your code here.
	var names_map = map[string][]int{}
	for i, each_height := range heights{
		for _, each_name := range each_height{
			for j, each_age := range ages{
				for _, each_name_ages := range each_age{
					if each_name_ages == each_name{
					//fmt.Println(i,each_name, each_age,each_name_ages)
						names_map[each_name] = []int{i, j}
					}
				}
			}
		}
	}

	return names_map
}
