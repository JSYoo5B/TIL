package main

import "fmt"

func main() {
	var flags uint8 = 0b_11001100
	var clears uint8 = 0b_01100110

	fmt.Printf("%b\n", flags)
	flags &^= clears
	fmt.Printf("%b\n", flags)
}
