#include <iostream>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
	for (int i = min(a, b); i > 0; i--) {
		if (a % i == 0 && b % i == 0)
			return i;
	}
}

int lcm(int a, int b) {
	return a * b / gcd(a, b);
}

int main(void) {
	int a, b;
	cin >> a >> b;

	cout << gcd(a, b) << '\n' << lcm(a, b);
}