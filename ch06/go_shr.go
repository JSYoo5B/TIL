package main

import "fmt"

func main() {
	var num1 uint8 = 0b_11001100

	fmt.Printf("0x%X\n", num1 >> 2)
	fmt.Printf("0x%X\n", uint8(int8(num1) >> 2))
}
