#include <iostream>
#include <cstring>

using namespace std;

void eratosthenes(bool* is_prime, int limit) {
	memset(is_prime, 1, sizeof(bool) * (limit + 1));

	is_prime[0] = false;
	is_prime[1] = false;

	for (int i = 2; i * i <= limit; i++) {
		for (int j = i * 2; j <= limit; j += i)
			is_prime[j] = false;
	}
}

int main(void) {
	bool* prime = new bool[10001];
	eratosthenes(prime, 10000);

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int number;
		cin >> number;

		bool partition_found = false;
		for (int left = number / 2; left > 1; left--) {
			if (prime[left] == false)
				continue;

			for (int right = number / 2; right <= number; right++) {
				if (prime[right] == false)
					continue;

				if ((left + right) == number) {
					cout << left << ' ' << right << '\n';
					partition_found = true;
					break;
				}
			}

			if (partition_found == true)
				break;
		}
	}
}