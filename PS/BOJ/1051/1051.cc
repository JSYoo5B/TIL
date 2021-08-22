#include <cstdio>
#include <algorithm>

using namespace std;

int main(void) {

	int row, col;
	scanf("%d%d", &row, &col);

	int rect[50][50];
	for (int i = 0; i < row; i++) {
		for (int j = 0; j < col; j++)
			scanf("%1d", &rect[i][j]);
	}

	for (int x = min(row, col); x > 0; x--) {
		for (int i = 0; (i + x - 1) < row; i++) {
			for (int j = 0; (j + x - 1) < col; j++) {
				if (rect[i][j] == rect[i+x-1][j]
					&& rect[i][j] == rect[i][j+x-1]
					&& rect[i][j] == rect[i+x-1][j+x-1]) {
					printf("%d", x * x);
					return 0;
				}
			}
		}
	}
}