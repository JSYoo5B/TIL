package main

import "fmt"

type Data struct {
	value int
	data [10]int
}

func main() {
	var data1 Data
	var pData1 *Data = &data1
	var pData2 *Data = &Data{}	// Create instance with indirect addressing
	var pData3 *Data = new(Data) // Create with new()

	fmt.Printf("&data1: %p\n", &data1)
	fmt.Printf("pData1: %p,\t&pData1: %p\n", pData1, &pData1)
	fmt.Printf("pData2: %p,\t&pData2: %p\n", pData2, &pData2)
	fmt.Printf("pData3: %p,\t&pData3: %p\n", pData3, &pData3)

	CallByValue(data1, 10)
	fmt.Println(data1)
	CallByAddress(&data1, 10)
	fmt.Println(data1)

	CallByValue(*pData1, 20)
	fmt.Println(pData1)
	CallByAddress(pData1, 20)
	fmt.Println(pData1)

	var pData4 *Data = nil
	pData4.value = 40	// Trigger segfault
}

func CallByValue(data Data, n int) {
	data.value = n
	data.data[0] = n / 10
	fmt.Printf("Call-by-value &data: %p\n", &data)
}

func CallByAddress(data *Data, n int) {
	data.value = n
	data.data[0] = n / 10
	fmt.Printf("Call-by-address &data: %p\n", data)
}