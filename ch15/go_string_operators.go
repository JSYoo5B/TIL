package main

import "fmt"

func main() {
	strHello := "hello"
	strWorld := "world"

	strHelloWorld := strHello
	strHelloWorld += strWorld

	strHelloExcl := strHello + " " + strWorld + "!"

	fmt.Println(strHelloWorld)
	fmt.Println(strHelloExcl)

	fmt.Printf("It is %v that \"%s\" is equal with \"%s\"\n",
		strHelloWorld == strHelloExcl, strHelloWorld, strHelloExcl)

	if strHelloWorld < strHelloExcl {
		fmt.Printf("%s comes before %s when strings are sorted in Unicode order\n",
			strHelloWorld, strHelloExcl)
	} else if strHelloWorld > strHelloExcl {
		fmt.Printf("%s comes after %s when strings are sorted in Unicode order\n",
			strHelloWorld, strHelloExcl)
	}
}
