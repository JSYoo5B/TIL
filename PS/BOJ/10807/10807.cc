#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int numbers;
	cin >> numbers;

	int* num = new int[numbers];
	for (int i = 0; i < numbers; i++) {
		cin >> num[i];
	}
	sort(num, num+numbers);

	int target, count;
	cin >> target;
	count = 0;
	for (int i = 0; i < numbers; i++) {
		if (num[i] < target)
			continue;
		else if (num[i] > target)
			break;
		else if (num[i] == target) 
			count++;
	}

	cout << count;
}