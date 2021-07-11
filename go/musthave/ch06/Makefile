all: blogging

blogging: go_xor_not go_bit_clear shr go_next_after

go_xor_not:
	go build -o go_xor_not go_xor_not.go

go_bit_clear:
	go build -o go_bit_clear go_bit_clear.go

shr:
	go build -o go_shr go_shr.go
	gcc -o c_shr c_shr.c
	javac java_shr.java

go_next_after:
	go build -o go_next_after go_next_after.go
