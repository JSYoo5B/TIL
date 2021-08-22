#include <stdio.h>

int main(void) {
	char str[100];
	// Get line including space char
	while(scanf("%[^\n]\n", str) == 1) {
		printf("%s\n", str);
	}
}