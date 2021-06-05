package main

import "fmt"

type Data struct{
	value int
	data [10]int
}

func main() {
	var data1 Data
	var data2 Data = *new(Data)

	var pData1 *Data = &data1
	var pData2 *Data = &data2
	var pData3 *Data = new(Data)
	var pData4 *Data = newData()
	var pData5 *Data

	n := 10
	if n % 5 == 0 {
		// force variable allocation unpredictable
		pData5 = new(Data)
	}

	fmt.Printf("pData1: %p\n", pData1)
	fmt.Printf("pData2: %p\n", pData2)
	fmt.Printf("pData3: %p\n", pData3)
	fmt.Printf("pData4: %p\n", pData4)
	fmt.Printf("pData5: %p\n", pData5)

	for {
		// Force infinite loop to check in /proc/**/map
	}
}

func newData() *Data {
	var d Data = Data{}
	return &d
}

