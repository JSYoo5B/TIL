#include <iostream>
#include <algorithm>
#include <cstdlib>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	int* input = new int[n];
	for (int i = 0; i < n; i++) {
		cin >> input[i];
	}

	sort(input, input + n);

	int left = 1; 
	int right = n - 2;

	int last_min = input[0];
	int last_max = input[n-1];

	int sum = abs(last_min - last_max);

	while(left < right) {
		int min = input[left];
		int max = input[right];

		left++;
		right--;

		sum += abs(max - last_min);
		sum += abs(min - last_max);
		last_max = max;
		last_min = min;
	}

	if (left == right)
		sum += max(abs(last_min - input[left]),
					abs(last_max - input[left]));
	cout << sum;
}