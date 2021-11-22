package main

import (
	"fmt"
	"bufio"
	"os"
)

func get_Z_value(exp, row, col int) int {
	if exp == 0 {
		return 0
	}
	middle := 1 << (exp-1)
	cur_val := 0
	if row >= middle {
		cur_val += middle * middle * 2
	}
	if col >= middle {
		cur_val += middle * middle
	}
	return cur_val + get_Z_value(exp-1, row%middle, col%middle)
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	writer := bufio.NewWriter(os.Stdout)
	defer writer.Flush()

	var exponent, row, col int
	fmt.Fscan(reader, &exponent, &row, &col)

	answer := get_Z_value(exponent, row, col)
	fmt.Fprint(writer, answer)
}
