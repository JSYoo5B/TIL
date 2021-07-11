package main

import "fmt"

func main() {
	if age := getMyAge(); age > 14 {
		fmt.Println("You're ok to sign up.")
	} else if approve := getParentApprove(); age >= 12 && approve {
		fmt.Println("Your parent approved you to sign up.")
	} else if age < 12 {
		fmt.Println("You need to be at least 12-years-old to sign up.")
	} else {
		fmt.Println("Your parent didn't approved you to sign up.")
	}
}

func getMyAge() int {
	return 12
}

func getParentApprove() bool {
	return false
}
