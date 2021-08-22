// Bottom-Up approach

#include <iostream>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* count = new int[n+1];
	int* last = new int[n+1];

	count[1] = 0;
	for (int i = 2; i <= n; i++) {
		count[i] = count[i-1] + 1;
		last[i] = i-1;
		if (i % 2 == 0 && count[i] > count[i/2] + 1) {
			count[i] = count[i / 2] + 1;
			last[i] = i / 2;
		}
		if (i % 3 == 0 && count[i] > count[i/3] + 1) {
			count[i] = count[i / 3] + 1;
			last[i] = i / 3;
		}
	}

	cout << count[n] << '\n';
	for (int i = n; i != 1; i = last[i])
		cout << i << ' ';
	cout << 1;
}