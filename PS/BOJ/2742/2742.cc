#include <cstdio>

using namespace std;

int main(void) {
	int n;

	scanf("%d", &n);

	for (int i = 0; i < n; i++) {
		printf("%d\n", n - i);
	}
}