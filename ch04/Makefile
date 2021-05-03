all: go_intmax32 go_intmax64

go_intmax32:
	GOOS=linux GOARCH=386 GO386=softfloat go build -o go_intmax32

go_intmax64:
	GOOS=linux GOARCH=amd64 go build -o go_intmax64
