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
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int a, b;
		cin >> a >> b;

		int gcd_ = gcd(a, b);
		int lcm = a * b / gcd(a, b);

		cout << lcm << ' ' << gcd_ << '\n';
	}
}