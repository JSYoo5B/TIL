// Bottom-Up approach

#include <iostream>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* count = new int[n+1];

	count[1] = 0;
	for (int i = 2; i <= n; i++) {
		count[i] = count[i-1] + 1;
		if (i % 2 == 0 && count[i] > count[i/2] + 1)
			count[i] = count[i / 2] + 1;
		if (i % 3 == 0 && count[i] > count[i/3] + 1)
			count[i] = count[i / 3] + 1;
	}

	cout << count[n];
}