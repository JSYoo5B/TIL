#include <iostream>
#include <algorithm>

using namespace std;

long long gcd(long long a, long long b) {
	long long big, small;
	big = max(a, b);
	small = min(a, b);

	long long remains = big % small;
	while(remains != 0) {
		big = small;
		small = remains;
		remains = big % small;
	}
	return small;
}

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int n_number;
		cin >> n_number;

		long long* numbers = new long long[n_number];
		for (int j = 0; j < n_number; j++) {
			cin >> numbers[j];
		}

		long long gcd_sum = 0;
		for (int j = 0; j < n_number - 1; j++) {
			for (int k = j + 1; k < n_number; k++) {
				gcd_sum += gcd(numbers[j], numbers[k]);
			}
		}
		cout << gcd_sum << '\n';

		delete[] numbers;
	}
}