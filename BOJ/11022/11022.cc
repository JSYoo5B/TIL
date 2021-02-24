#include <cstdio>

using namespace std;

int main(void) {
	int cases;
	int a, b;

	scanf("%d", &cases);

	for (int i = 1; i <= cases; i++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d ", i, a, b, a + b);
	}
}
