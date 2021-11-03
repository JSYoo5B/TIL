package main

import (
	"fmt"
    "bufio"
    "os"
)

type pos struct {
	r int
	c int
}

func rotate_table(idx int, tbl *[][]int, rotate int) {
	row_cnt := len(*tbl)
	col_cnt := len((*tbl)[0])

	buff_len := (col_cnt - idx * 2) + (row_cnt - idx * 2 - 2)
	buff_len *= 2
	val_buff := make([]int, 0, buff_len)
	pos_buff := make([]pos, 0, buff_len)

	// top (left to right)
	for c := idx; c < col_cnt - idx; c++ {
		r := idx
		val_buff = append(val_buff, (*tbl)[r][c])
		pos_buff = append(pos_buff, pos{r, c})
	}

	// right (up to down)
	for r := idx + 1; r < row_cnt - idx - 1; r++ {
		c := col_cnt - idx - 1
		val_buff = append(val_buff, (*tbl)[r][c])
		pos_buff = append(pos_buff, pos{r, c})
	}

	// down (right to left)
	for c := col_cnt - idx - 1; c >= idx; c-- {
		r := row_cnt - idx - 1;
		val_buff = append(val_buff, (*tbl)[r][c])
		pos_buff = append(pos_buff, pos{r, c})
	}

	// left (down to up)
	for r := row_cnt - idx - 2; r >= idx + 1; r-- {
		c := idx
		val_buff = append(val_buff, (*tbl)[r][c])
		pos_buff = append(pos_buff, pos{r, c})
	}

	// rotate values
	rotate %= len(val_buff)
	val_buff = append(val_buff[rotate:], val_buff[:rotate]...)

	for idx = 0 ; idx < len(val_buff); idx++ {
		val := val_buff[idx]
		r := pos_buff[idx].r
		c := pos_buff[idx].c

		(*tbl)[r][c] = val
	}
}

func main() {
	var row_cnt, col_cnt, rotate_cnt int
    reader := bufio.NewReader(os.Stdin)
    writer := bufio.NewWriter(os.Stdout)
	fmt.Fscan(reader, &row_cnt, &col_cnt, &rotate_cnt)

	table := make([][]int, row_cnt)
	for r := 0; r < row_cnt; r++ {
		table[r] = make([]int, col_cnt)
		for c := 0; c < col_cnt; c++ {
            fmt.Fscan(reader, &table[r][c])
		}
	}

	min := row_cnt
	if col_cnt < row_cnt {
		min = col_cnt
	}
	loop := min / 2
	for idx := 0; idx < loop; idx++ {
		rotate_table(idx, &table, rotate_cnt)
	}

	for r := 0; r < row_cnt; r++ {
		for c := 0; c < col_cnt; c++ {
			fmt.Fprint(writer, table[r][c], " ")
		}
		fmt.Fprintln(writer)
	}
	writer.Flush()
}
