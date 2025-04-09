package main

import (
	"bytes"
	"github.com/stretchr/testify/assert"
	"strings"
	"testing"
)

func TestEcho(t *testing.T) {
	e := NewEchoNode()
	output := bytes.NewBuffer(nil)
	e.Stdout = output

	input := `{"src":"c1","dest":"n1","body":{"type":"echo","msg_id":1,"echo":"Please echo 35"}}`
	e.Stdin = strings.NewReader(input)
	err := e.Run()
	if err != nil {
		return
	}
	expected := `{"dest":"c1","body":{"echo":"Please echo 35","in_reply_to":1,"msg_id":1,"type":"echo_ok"}}`
	assert.JSONEq(t, expected, output.String())
}
