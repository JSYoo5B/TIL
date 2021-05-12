package main

import "fmt"

func main() {
	dividend := 16
	divisor := 5
	quot, remain, valid := Divide(dividend, divisor)
	if valid {
		fmt.Printf("The quotient of %d divided by %d is %d with a remainder of %d",
			dividend, divisor, quot, remain)
	}
}

func Divide(dividend, divisor int) (quotient, remainder int, validity bool) {
	if divisor == 0 {
		return 0, 0, false
	}
	quotient = dividend / divisor
	remainder = dividend % divisor
	validity = true
	return
}
