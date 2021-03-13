#include <iostream>

using namespace std;

int main(void) {
	int input;

	cin >> input;

	if (input < 100) {
		cout << input;
		return 0;
	}

	int cnt = 99;
	for (int i = 111; i <= input; i++) {
		int diff1 = (i / 100) - ((i / 10) % 10);
		int diff2 = ((i / 10) % 10) - i % 10;
		if (diff1 == diff2)
			cnt++;
	}

	cout << cnt;
}