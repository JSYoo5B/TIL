all: blogging

blogging: go_newline go_printf go_scan blank

go_newline:
	go build -o go_newline go_newline.go

go_printf:
	go build -o go_printf go_printf.go

go_scan:
	go build -o go_scan go_scan.go

blank:
	go build -o blank blank.go

unref:
	# This code is intended to fail build. just check the code
	go vet unref.go
