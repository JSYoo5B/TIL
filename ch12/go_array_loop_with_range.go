package main

import "fmt"

func main() {
	var nums [5]int = [...]int{2, 3, 5, 8, 13}

	for i, val := range nums {
		fmt.Printf("nums[%d] = %d\n", i, val)
	}
    fmt.Println()

    for i := 0; i < len(nums); i++ {
		fmt.Printf("nums[%d] = %d\n", i, nums[i])
	}
}
