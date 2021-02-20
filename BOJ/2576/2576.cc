#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(void) {
	vector<int> odds;
	int input;
	int odd_cnt = 0;

	for (int i = 0; i < 7; i++) {
		cin >> input;
		if (input % 2 == 1) {
			odds.push_back(input);
			odd_cnt++;
		}
	}

	if (odd_cnt == 0) {
		cout << -1 ;
		return 0;
	}

	sort(odds.begin(), odds.end());

	int sum = 0;
	for (int& i : odds) {
		sum += i;
	}

	cout << sum << '\n' << odds[0];
}