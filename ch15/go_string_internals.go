package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	str := "Hello world"
	stringHeader := (*reflect.StringHeader)(unsafe.Pointer(&str))
	fmt.Println(stringHeader)

	slice := []byte(str)
	slice[2] = 'a'
	fmt.Printf("%s\n", slice)
	sliceHeader := (*reflect.SliceHeader)(unsafe.Pointer(&slice))
	fmt.Println(sliceHeader)

	newStr := string(slice)
	fmt.Println(newStr)
	newStrHeader := (*reflect.StringHeader)(unsafe.Pointer(&newStr))
	fmt.Println(newStrHeader)
}
