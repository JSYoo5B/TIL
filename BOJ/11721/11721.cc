#include <cstdio>
#include <cstring>
using namespace std;
int main(void) {
	char str[120];
	scanf("%s", &str);

	int length = strlen(str);
	for (int i = 0; i < length; i++) {
		printf("%c", str[i]);
		if (i % 10 == 9) {
			printf("\n");
		}
	}
}