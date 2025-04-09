package main

import (
	"encoding/json"
	maelstrom "github.com/jepsen-io/maelstrom/demo/go"
)

type EchoNode struct {
	*maelstrom.Node
}

func NewEchoNode() *EchoNode {
	e := &EchoNode{Node: maelstrom.NewNode()}

	e.Handle("echo", e.handleEcho)

	return e
}

func (e *EchoNode) handleEcho(msg maelstrom.Message) error {
	// Unmarshal the message body as an loosely-typed map
	var body map[string]any
	if err := json.Unmarshal(msg.Body, &body); err != nil {
		return err
	}

	// Update the message type to return back.
	body["type"] = "echo_ok"

	// Echo the original message back with the updated message type.
	return e.Reply(msg, body)
}
