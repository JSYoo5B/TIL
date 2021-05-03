#include <cstdio>
#include <algorithm>

using namespace std;

int main(void) {
	char c = '\0';
	int idx = 0;
	int num[20];

	while(1) {
		scanf("%c", &c);
		if (c == '\n')
			break;
		else {
			num[idx] = c - '0';
			idx++;
		}
	}

	sort(num, num+idx);
	for (int i = idx - 1; i > -1; i--) {
		printf("%d", num[i]);
	}
}