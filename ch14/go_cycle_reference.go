package main

type List struct {
	value int
	next *List
}

func main() {
	var pLists [100]*List

	for i := 0; true; i++{
		var l1 List
		var l2 List
		var l3 List

		l1.next = &l2
		l2.next = &l3
		l3.next = &l1

		l1.value = 1
		l1.next.value = l1.value + 1
		l1.next.next.value = l1.next.value + 1

		pLists[i % 100] = &l1
	}
}