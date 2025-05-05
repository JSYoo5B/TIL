package main

import (
	"bytes"
	"encoding/json"
	maelstrom "github.com/jepsen-io/maelstrom/demo/go"
	"github.com/stretchr/testify/assert"
	"testing"
)

func TestEcho(t *testing.T) {
	body := map[string]any{
		"type":   "echo",
		"msg_id": 1,
		"echo":   "Please echo 35",
	}
	marshalBody, _ := json.Marshal(body)
	inputMsg := maelstrom.Message{
		Src:  "c1",
		Dest: "n1",
		Body: json.RawMessage(marshalBody),
	}

	e := NewEchoNode()
	output := bytes.NewBuffer(nil)
	e.Stdout = output

	input, _ := json.Marshal(inputMsg)
	e.Stdin = bytes.NewReader(input)
	err := e.Run()
	if err != nil {
		return
	}
	expected := `{"dest":"c1","body":{"echo":"Please echo 35","in_reply_to":1,"msg_id":1,"type":"echo_ok"}}`
	assert.JSONEq(t, expected, output.String())
}
