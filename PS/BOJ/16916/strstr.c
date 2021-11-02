#include <stdio.h>
#include <string.h>

char origin[1000001];
char substr[1000001];

int main(void) {
	scanf("%s", origin);
	scanf("%s", substr);

	char* substr_pos = strstr(origin, substr);
	int answer = (int)(substr_pos != NULL);
	printf("%d", answer);
}
