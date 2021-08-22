#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	int n, idx;

	cin >> n >> idx;

	int* num = new int[n];
	for(int i = 0; i < n; i++) {
		cin >> num[i];
	}

	nth_element(num, num + idx - 1, num + n);
	cout << num[idx-1];
}