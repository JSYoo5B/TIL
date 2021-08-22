#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int num[9];

	for (int i = 0; i < 9; i++) {
		cin >> num[i];
	}

	int max = *max_element(num, num+9);
	cout << max << '\n';
	for (int i = 0; i < 9; i++) {
		if (num[i] == max)
			cout << i + 1;
	}
}