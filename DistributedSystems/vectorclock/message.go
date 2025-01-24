package vectorclock

import (
	"fmt"
	"sync"
)

type Message struct {
	From    int
	To      int
	Clock   VectorClock
	Payload string
}

func (m Message) String() string {
	return fmt.Sprintf(`Clock%v | %d -> %d | "%s"`,
		m.Clock, m.From, m.To, m.Payload)
}

func NewMiddleware(processes int) *Middleware {
	channels := make([]chan Message, processes)
	wait := &sync.WaitGroup{}
	for i := range channels {
		channels[i] = make(chan Message)
		wait.Add(1)
	}
	return &Middleware{
		channels: channels,
		wg:       wait,
	}
}

type Middleware struct {
	channels []chan Message
	wg       *sync.WaitGroup
}

func (m Middleware) GetChannel(id int) chan Message {
	return m.channels[id]
}

func (m Middleware) Send(msg Message) {
	m.channels[msg.To] <- msg
}

func (m Middleware) Stop(id int) {
	close(m.channels[id])
	m.wg.Done()
}

func (m Middleware) Wait() {
	m.wg.Wait()
}

func (m Middleware) Length() int {
	return len(m.channels)
}
