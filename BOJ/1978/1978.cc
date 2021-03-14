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
	bool is_prime[1001];
	eratosthenes(is_prime, 1000);

	int cases;
	int count = 0;

	cin >> cases;

	for (int i  = 0; i < cases; i++) {
		int input;
		cin >> input;
		if (is_prime[input])
			count++;
	}
	
	cout << count;
}