package main

import (
	"log"
)

func main() {
	e := NewEchoNode()

	if err := e.Run(); err != nil {
		log.Fatal(err)
	}
}
