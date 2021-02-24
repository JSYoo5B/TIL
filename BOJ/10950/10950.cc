#include <cstdio>
using namespace std;

int main(void) {
	int cases;
	int a, b;

	scanf("%d", &cases);

	for (int i = 0; i < cases; i++) {
		scanf("%d %d", &a, &b);
		printf("%d ", a + b);
	}
}