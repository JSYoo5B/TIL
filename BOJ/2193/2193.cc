#include <iostream>

using namespace std;

int main(void) {
	int n_digit;
	cin >> n_digit;

	long long pinary[91][2];
	pinary[1][0] = 0;
	pinary[1][1] = 1;

	for (int i = 2; i <= n_digit; i++) {
		pinary[i][0] = pinary[i-1][0] + pinary[i-1][1];
		pinary[i][1] = pinary[i-1][0];
	}

	cout << pinary[n_digit][0] + pinary[n_digit][1];
}