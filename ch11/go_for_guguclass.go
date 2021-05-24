package main

import "fmt"

func main() {
	// Conventional for loop
	for i := 1; i <= 9; i++ {
	    fmt.Printf("%d * %d = %d\n", 2, i, 2 * i)
	}

	// Without initializer
	i := 1
	for ; i <= 9; i++ {
	    fmt.Printf("%d * %d = %d\n", 2, i, 2 * i)
	}

	// Without incrementor
	for i := 1; i <= 9; {
	    fmt.Printf("%d * %d = %d\n", 2, i, 2 * i)
	    i++
	}

	// Codition check only
	j := 1
	for j <= 9 {
	    fmt.Printf("%d * %d = %d\n", 2, j, 2 * j)
	    j++
	}
}
