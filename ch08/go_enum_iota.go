package main

import "fmt"

const (
	FLAG_ALPHA = 1 << iota
	FLAG_BRABO
	FLAG_CHARLIE
)

func main() {
	fmt.Println(FLAG_ALPHA, FLAG_BRABO, FLAG_CHARLIE)
}

