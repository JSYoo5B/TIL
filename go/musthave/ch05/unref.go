package main

import "fmt"

func main() {
	var num1 int
	var num2 int

	fmt.Print("Enter 2 numbers: ")
	n, err := fmt.Scanln(&num1, &num2)
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Printf("num1: %d, num2: %d", num1, num2)
	}
}
