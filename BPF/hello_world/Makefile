all: bpf.o

clean:
	rm -f bpf.ll bpf.o

bpf.ll: bpf.c
	clang -O2 -emit-llvm -c bpf.c -o bpf.ll

bpf.o: bpf.ll
	llc -march=bpf -filetype=obj bpf.ll -o bpf.o
