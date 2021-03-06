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
	bool* prime = new bool[246912 + 1];
	eratosthenes(prime, 246912);

	while(1) {
		int n;
		cin >> n;

		if (n == 0)
			break;

		int n_prime = 0;
		for (int i = n + 1; i <= 2*n; i++) {
			if (prime[i] == true)
				n_prime++;
		}
		cout << n_prime << '\n';
	}
}