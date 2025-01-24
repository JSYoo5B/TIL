package vectorclock

import (
	"fmt"
	"sync"
	"testing"
)

func TestMessage_String(t *testing.T) {
	testCases := map[string]Message{
		"Two process": {
			From:    0,
			To:      1,
			Payload: "hello",
			Clock:   []int{1, 0},
		},
		"Three process": {
			From:    1,
			To:      0,
			Payload: "hello",
			Clock:   []int{0, 1, 0},
		},
	}

	for name, message := range testCases {
		t.Run(name, func(t *testing.T) {
			fmt.Printf("%s\n", message)
		})
	}
}

func TestMiddleware(t *testing.T) {
	middleware := NewMiddleware(3)

	wg := sync.WaitGroup{}
	wg.Add(2)

	// Run sender
	go func() {
		defer wg.Done()

		middleware.Send(Message{From: 1, To: 0, Payload: "hello"})
	}()

	// Run receiver
	go func() {
		defer wg.Done()

		receiver := middleware.GetChannel(0)
		msg := <-receiver
		fmt.Println("Received message: ", msg)
	}()

	wg.Wait()
}
