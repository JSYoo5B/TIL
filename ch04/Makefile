all: blogging

blogging: go_intmax32 go_intmax64 go_multilingual

go_intmax32:
	# Build in 32-bit linux application
	GOOS=linux GOARCH=386 GO386=softfloat go build -o go_intmax32 go_intmax.go

go_intmax64:
	# Build in 64-bit linux application
	GOOS=linux GOARCH=amd64 go build -o go_intmax64 go_intmax.go

go_multilingual:
	go build -o go_multilingual go_multilingual.go

go_var:
	# This code is intended to fail build. just check the code
	go vet go_var.go
