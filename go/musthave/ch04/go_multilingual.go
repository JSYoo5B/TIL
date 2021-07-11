package main

import "fmt"

func main() {
	var multilingual string = "English와 한글이 섞인"

	fmt.Println(multilingual)

	multiLingRunes := []rune(multilingual)
	multiLingBytes := []byte(multilingual)

	fmt.Println(multiLingRunes)
	fmt.Println(multiLingBytes)
}
