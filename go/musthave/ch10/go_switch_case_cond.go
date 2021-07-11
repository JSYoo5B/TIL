package main

import "fmt"

func main() {
	switch age := getMyAge(); true {
	case age < 12:
		fmt.Println("You need to be at least 12-years-old to sign up.")
	case 12 <= age && age < 14:
		fmt.Println("You need parent's approval to sign up.")
	default:
		fmt.Println("You're ok to sign up.")
	}
}

func getMyAge() int {
	return 8
}
