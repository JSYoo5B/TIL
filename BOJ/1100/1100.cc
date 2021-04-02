#include <cstdio>
#define BLACK 0
#define WHITE 1

using namespace std;

bool is_white(int x, int y) {
	if ((x + y) % 2 == 0)
		return WHITE;
	else
		return BLACK;
}

int main(void) {
	int cnt = 0;

	for (int i = 0; i < 8; i++) {
		char c;
		for (int j = 0; j < 8; j++) {
			scanf("%c", &c);
			if (c == 'F' && is_white(i, j))
				cnt++;
		}
		scanf("%c", &c);
	}

	printf("%d", cnt);
}