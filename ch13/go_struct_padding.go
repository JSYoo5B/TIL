package main

import (
	"fmt"
	"unsafe"
)

type Unoptimized struct {
	A	int8
	B	int
	C 	int8
	D 	int
	E 	int8
}

type Optimized struct {
	A 	int8
	C 	int8
	E   int8
	B 	int
	D 	int
}

func main() {
	var1 := Unoptimized{}
	var2 := Optimized{}

	fmt.Printf("sizeof Unoptimized: %d, Optimized: %d\n",
		unsafe.Sizeof(var1), unsafe.Sizeof(var2))

	fmt.Printf("\nUnoptimized\n\tA: %p\n\tB: %p\n\tC: %p\n\tD: %p\n\tE: %p\n",
		&var1.A, &var1.B, &var1.C, &var1.D, &var1.E)
	fmt.Printf("\nOptimized\n\tA: %p\n\tB: %p\n\tC: %p\n\tD: %p\n\tE: %p\n",
		&var2.A, &var2.B, &var2.C, &var2.D, &var2.E)
}
