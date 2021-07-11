package main

import "fmt"

func main() {
	var num1 int
	var num2 int = *new(int)

	var pInt1 *int = &num1
	var pInt2 *int = &num2
	var pInt3 *int = new(int)
	var pInt4 *int = newint()
	var pInt5 *int

	n := 10
	if n % 5 == 0 {
		// force variable allocation unpredictable
		pInt5 = new(int)
	}

	fmt.Printf("pInt1: %p\n", pInt1)
	fmt.Printf("pInt2: %p\n", pInt2)
	fmt.Printf("pInt3: %p\n", pInt3)
	fmt.Printf("pInt4: %p\n", pInt4)
	fmt.Printf("pInt5: %p\n", pInt5)

	for {
		// Force infinite loop to check in /proc/**/map
	}
}

func newint() *int {
	var d int = 0
	return &d
}

