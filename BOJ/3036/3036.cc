#include <iostream>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
	for (int i = min(a, b); i > 0; i--) {
		if (a % i == 0 && b % i == 0)
			return i;
	}
}

int main(void) {
	int n_number;
	cin >> n_number;

	int* numbers = new int[n_number];
	for (int i = 0; i < n_number; i++) {
		cin >> numbers[i];
	}

	for (int i = 1; i < n_number; i++) {
		int divisor = gcd(numbers[0], numbers[i]);

		cout << numbers[0] / divisor << '/' << numbers[i] / divisor << '\n';
	}
}