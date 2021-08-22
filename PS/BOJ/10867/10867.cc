#include <iostream>

using namespace std;

int main(void) {
	int N;
	cin >> N;

	bool hasSeen[2001] = {false};
	for (int i = 0; i < N; i++) {
		int value;
		cin >> value;
		hasSeen[value + 1000] = true;
	}

	for (int i = 0; i < 2001; i++) {
		if (hasSeen[i] == true)
			cout << (i - 1000) << ' ';
	}
	return 0;
}