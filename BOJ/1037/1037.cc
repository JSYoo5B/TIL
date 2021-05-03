#include <iostream>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	int min = 2000000;
	int max = -1;
	for (int i = 0; i < cases; i++) {
		int number;
		cin >> number;
		if (number > max)
			max = number;
		if (number < min)
			min = number;
	}
	cout << min * max;
}