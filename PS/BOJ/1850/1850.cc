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
	long long a, b;
	cin >> a >> b;

	long long gcd_count = gcd(a, b);
	for (long long i = 0; i < gcd_count; i++) {
		cout << 1;
	}
	cout << endl;
}