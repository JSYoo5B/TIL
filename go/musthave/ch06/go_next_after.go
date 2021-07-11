package main

import (
	"fmt"
	"math"
)

func main() {
	var num1 float64 = 0.0

	fmt.Printf("%g\n", num1)
	fmt.Printf("%g\n", math.Nextafter(num1, 1));
}
