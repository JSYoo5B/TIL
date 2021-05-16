package main

import "fmt"

func main() {
	switch age := getMyAge(); age {
    case 9:
        fallthrough
	case 10:
        fallthrough
    case 11:
        fmt.Println("You need to be at least 12-years-old to sign up.")
    case 12:
        fallthrough
    case 13:
        fmt.Println("You need parent's approval to sign up.")
    default:
        fmt.Println("You're ok to sign up.")
	}
}

func getMyAge() int {
	return 9
}
