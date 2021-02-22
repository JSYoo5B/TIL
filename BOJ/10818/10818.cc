#include <cstdio>

using namespace std;

int main(void) {
	int numbers;
	int min, max;
	int input;
	// set min and max as reversal  
	min = 1000000;
	max = -1000000;

	scanf("%d", &numbers);
	for (int i = 0; i < numbers; i++) {
		scanf("%d", &input);
		if (input < min) {
			min = input;
		}
		if (input > max) {
			max = input;
		}
	}
	printf("%d %d\n", min, max);
}