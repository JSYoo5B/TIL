#include <cstdio>
#include <cstring>

using namespace std;

int main(void) {
	int cases;

	scanf("%d ", &cases);

	for (int i = 0; i < cases; i++) {
		bool exist[10];
		memset(exist, 0, (sizeof(bool) * 10));
		char c;
		do {
			scanf("%c", &c);
			if (c >= '0' && c <= '9') {
				exist[c - '0'] = true;
			}
		} while (c != '\n');

		int beauty = 0;
		for (int i = 0; i < 10; i++) {
			if (exist[i])
				beauty++;
		}
		printf("%d\n", beauty);
	}
}