CC=gcc
# Add static flag to prevent linking shared objects
CFLAGS=-static -g

all: fork exec exit open read write close

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

read: read.c
	gcc -o $@ $< $(CFLAGS)

write: write.c
	gcc -o $@ $< $(CFLAGS)

close: close.c
	gcc -o $@ $< $(CFLAGS)

clean:
	rm -f fork
	rm -f hello exec
	rm -f exit
	rm -f open
	rm -f read
	rm -f write
	rm -f close
