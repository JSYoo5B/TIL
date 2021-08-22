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
	bool is_prime[10001];
	eratosthenes(is_prime, 10000);

	int min, max;
	cin >> min >> max;

	int min_prime = 10001;
	int prime_sum = 0;
	for (int i = min; i <= max; i++) {
		if (is_prime[i] == false)
			continue;

		prime_sum += i;
		if (min_prime > i)
			min_prime = i;
	}
	if (prime_sum == 0)
		cout << -1;
	else 
		cout << prime_sum << '\n' << min_prime;
}
