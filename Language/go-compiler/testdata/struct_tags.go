package main

type User struct {
	ID   int    `json:"id" db:"user_id"`
	Name string `json:"name"`
	Age  int    `json:"age,omitempty"`

	internalField bool
}

type OtherType int
