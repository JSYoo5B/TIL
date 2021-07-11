package main

import "fmt"

func main() {
	var contact1 struct {
		Name string
		Id   int
		Cell string
	}

	fmt.Println(contact1)

	contact1.Id = 1
	contact1.Name = "John Doe"
	contact1.Cell = "1 234-567-890"

	// Copy anonymous struct into the other variable
	contact2 := contact1

	contact2.Name = "Jane Doe"
	contact2.Id = 2

	fmt.Println(contact1)
	fmt.Println(contact2)
}