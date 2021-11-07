CC=gcc
# Add static flag to prevent linking shared objects
CFLAGS=-static -g

all: fork exec

fork: fork.c
	gcc -o $@ $< $(CFLAGS)

hello: hello.c
	gcc -o $@ $< $(CFLAGS)

exec: exec.c hello
	gcc -o exec exec.c $(CFLAGS)

clean:
	rm -f fork
