#include <stdio.h>

int main(void) {
	int number;

	// %i automatically checks radix
	scanf("%i", &number);
	printf("%d", number);
}