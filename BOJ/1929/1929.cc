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
	int m, n;

	cin >> m >> n;

	bool* prime = new bool[n+1];
	eratosthenes(prime, n);

	for(int i = m; i <= n; i++) {
		if (prime[i] == true) {
			cout << i << '\n';
		}
	}
}