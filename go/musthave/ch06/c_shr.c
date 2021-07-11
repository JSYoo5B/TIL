#include <stdio.h>
#include <sys/types.h>

int main(void) {
	u_int8_t num1 = 0xCC;

	printf("0x%X\n", num1 >> 2);
	printf("0x%X\n", (u_int8_t)((int8_t)num1 >> 2));
}
