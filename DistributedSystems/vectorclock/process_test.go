package vectorclock

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func TestProcess(t *testing.T) {
	middleware := *NewMiddleware(3)
	processes := []*Process{
		NewProcess(
			0,
			middleware,
			50*time.Millisecond,
			[]string{
				"send 1,2 hello",
				"wait",
			},
			1,
		),
		NewProcess(
			1,
			middleware,
			10*time.Millisecond,
			[]string{
				"wait",
				"send 0,2 world",
				"wait",
			},
			1,
		),
		NewProcess(
			2,
			middleware,
			200*time.Millisecond,
			[]string{
				"wait",
			},
			2,
		),
	}

	for _, process := range processes {
		go process.Run()
	}

	middleware.Wait()
}

func TestProcess_doTask_send(t *testing.T) {
	middleware := *NewMiddleware(3)
	process := NewProcess(0, middleware, time.Millisecond, []string{}, 0)

	wg := sync.WaitGroup{}
	wg.Add(2)
	receiveFunc := func(id int) {
		defer wg.Done()

		receiver := middleware.GetChannel(id)
		msg := <-receiver
		fmt.Println("Received message: ", msg)
	}

	go receiveFunc(1)
	go receiveFunc(2)
	process.doTask("send 1,2 hello")

	wg.Wait()
}
