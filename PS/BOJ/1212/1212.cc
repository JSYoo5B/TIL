#include <cstdio>

int main(void) {
	char c;
	bool first = true;

	while(1) {
		scanf("%c", &c);
		switch(c) {
			case '\n':
			return 0;

			case '0':
			printf("%s", (first ? "0" : "000"));
			break;

			case '1':
			printf("%s", (first ? "1" : "001"));
			break;

			case '2':
			printf("%s", (first ? "10" : "010"));
			break;

			case '3':
			printf("%s", (first ? "11" : "011"));
			break;

			case '4':
			printf("100");
			break;

			case '5':
			printf("101");
			break;

			case '6':
			printf("110");
			break;

			case '7':
			printf("111");
			break;
		}
		first = false;
	}
}