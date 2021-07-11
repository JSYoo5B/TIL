package main

import "fmt"

func main() {
    var uint8Max uint8 = ^uint8(0)

    fmt.Printf("%b\n", uint8Max)
}
