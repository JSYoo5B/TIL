// Bottom-up approach

#include <iostream>

using namespace std;

int main(void) {
	int count[12];

	count[0] = 0;
	count[1] = 1; // 1
	count[2] = 2; // 1+1, 2
	count[3] = 4; // 1+1+1, 1+2, 2+1, 3
	for (int i = 4; i <= 11; i++) {
		count[i] = count[i-1];  // "count[i]" + 1
		count[i] += count[i-2]; // "count[i]" + 2
		count[i] += count[i-3]; // "count[i]" + 3
	}

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int n;
		cin >> n;

		cout << count[n] << '\n';
	}
}