#include <iostream>
#include <cstring>

using namespace std;

int main(void) {
	int n;
	cin >> n;
	if (n == 0) {
		cout << 0;
		return 0;
	}
	else if (n == 1) {
		cout << 1;
		return 0;
	}

	long long* fibo = new long long[n];
	memset(fibo, -1, (sizeof(long long) * n));

	fibo[0] = 0;
	fibo[1] = 1;
	for (int i = 2; i < n; i++) {
		fibo[i] = fibo[i-1] + fibo[i-2];
	}

	cout << fibo[n-1] + fibo[n-2]; 
}