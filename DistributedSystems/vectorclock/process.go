package vectorclock

import (
	"fmt"
	"strconv"
	"strings"
	"time"
)

func NewProcess(id int, middleware Middleware, interval time.Duration, tasks []string, expectCount int) *Process {
	return &Process{
		id:          id,
		middleware:  middleware,
		receiver:    middleware.GetChannel(id),
		clock:       NewVectorClock(middleware.Length()),
		interval:    interval,
		tasks:       tasks,
		expectCount: expectCount,
	}
}

type Process struct {
	id          int
	middleware  Middleware
	receiver    chan Message
	clock       VectorClock
	interval    time.Duration
	tasks       []string
	expectCount int
}

func (p *Process) Run() {
	receiveCount := 0
	for i := 0; i < len(p.tasks); i++ {
		p.clock[p.id] += 1

		select {
		case msg := <-p.receiver:
			p.clock = MergeClock(p.id, p.clock, msg.Clock)
			fmt.Printf("Process %d received: %s, updated Clock%v\n", p.id, msg, p.clock)
			receiveCount++
		case <-time.After(p.interval):
			// In my interval, message not received
		}

		p.doTask(p.tasks[i])

		if i == len(p.tasks)-1 && p.tasks[i] == "wait" {
			if receiveCount == p.expectCount {
				break
			} else {
				i -= 1
				continue
			}
		}
	}

	fmt.Printf("Process %d finished job\n", p.id)
	p.middleware.Stop(p.id)
}

func (p *Process) doTask(task string) {
	switch {
	case task == "wait":
		fmt.Printf("Process %d waits... Clock%v\n", p.id, p.clock)
	case strings.HasPrefix(task, "send"):
		tokens := strings.SplitN(task, " ", 3)
		fmt.Printf("Process %d sends %s to %s... Clock%v\n", p.id, tokens[2], tokens[1], p.clock)
		for _, toStr := range strings.Split(tokens[1], ",") {
			to, _ := strconv.Atoi(toStr)
			msg := Message{
				From:    p.id,
				To:      to,
				Payload: tokens[2],
				Clock:   p.clock.Copy(),
			}
			p.middleware.Send(msg)
		}
	}
}
