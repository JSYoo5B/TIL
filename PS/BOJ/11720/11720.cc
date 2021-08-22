#include <cstdio>
using namespace std;
int main(void) {
	int count;
	int input, sum;

	sum = 0;
	scanf("%d", &count);
	for (int i = 0; i < count; i++) {
		scanf("%1d", &input);
		sum += input;
	}
	printf("%d\n", sum);
}