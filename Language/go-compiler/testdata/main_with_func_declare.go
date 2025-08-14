package main

import "fmt"

func main() {
	message := "Hello, AST!"
	fmt.Println(message)
}

func greet(name string, age int) {
	fmt.Printf("Hello, %s! You are %d years old.\n", name, age)
}

func add(a, b int) int {
	return a + b
}
