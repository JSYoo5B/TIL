#include <stdio.h>

enum {
	FLAG_ALPHA = 1 << 1,
	FLAG_BRABO = 1 << 2,
	FLAG_CHARLIE = 1 << 3
};

int main(void) {
	printf("%d %d %d\n", FLAG_ALPHA, FLAG_BRABO, FLAG_CHARLIE);
}

