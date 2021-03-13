#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* A = new int[n];
	int* B = new int[n];

	for (int i = 0; i < n; i++) {
		cin >> A[i];
	}
	for (int i = 0; i < n; i++) {
		cin >> B[i];
	}

	sort(A, A+n);
	sort(B, B+n, greater<int>());

	int sum = 0;
	for (int i = 0; i < n; i++) {
		sum += A[i] * B[i];
	}

	cout << sum;
}