#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	int numbers;
	vector<int> storage;

	cin >> numbers;
	for (int i = 0; i < numbers; i++) {
		int temp;
		cin >> temp;
		storage.push_back(temp);
	}

	sort(storage.begin(), storage.end());

	for (auto i : storage) {
		cout << i << "\n";
	}
}