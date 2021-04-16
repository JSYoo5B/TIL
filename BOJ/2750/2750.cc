#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* numbers = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> numbers[i];
	}
	sort(numbers, numbers+n);
	for (int i = 0; i < n; i++) {
		cout << numbers[i] << '\n';
	}
}