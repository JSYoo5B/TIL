CC=gcc
# Add static flag to prevent linking shared objects
CFLAGS=-static -g

all: fork exec exit open

fork: fork.c
	gcc -o $@ $< $(CFLAGS)

hello: hello.c
	gcc -o $@ $< $(CFLAGS)

exec: exec.c hello
	gcc -o exec exec.c $(CFLAGS)

exit: exit.c
	gcc -o $@ $< $(CFLAGS)

open: open.c
	gcc -o $@ $< $(CFLAGS)

clean:
	rm -f fork
	rm -f hello exec
	rm -f exit
	rm -f open
