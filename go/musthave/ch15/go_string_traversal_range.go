package main

import "fmt"

func main() {
	str := `backquote로 감싸진 string은
그대로 줄바꿈이 되지만 \n은 동작하지 않습니다.`

	fmt.Println(str)
	for _, v := range str {
		fmt.Printf("Type: %T	Value: %d	Char: %c\n",
			v, v, v)
	}
}