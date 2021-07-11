package main

import "fmt"

func main() {
	var arrX [5]int
	var arr3 = [3]int{3, 4, 5}
	var arr5 = [5]int{10, 20, 4:50}
	var arr8 = [8]int{7, 6, 5, 4, 3, 2, 1, 0}

	fmt.Println(arrX)

	// go vet: Cannot use 'arr3' (type [3]int) as the type [5]int
	// arrX = arr3
	copy(arrX[0:3], arr3[:])

	fmt.Println(arrX)

	arrX = arr5

	fmt.Println(arrX)

	// src length can exceed dst length
	copy(arrX[:], arr8[1:7])

	fmt.Println(arrX)
}
