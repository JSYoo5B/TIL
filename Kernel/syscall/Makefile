CC=gcc
# Add static flag to prevent linking shared objects
CFLAGS=-static

all: fork 

fork: fork.c
	gcc -o $@ $< $(CFLAGS)

clean:
	rm -f fork
