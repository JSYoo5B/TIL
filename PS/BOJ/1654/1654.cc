#include <iostream>
#include <vector>

using namespace std;

int cut_lines(const vector<int>& lines, long long length) {
	int n_lines = 0;
	for (auto i : lines) {
		n_lines += (i / length);
	}
	return n_lines;
} 

int main(void) {
	long long given, to_make;
	long long min = 1, max = 0;
	vector<int> lines;

	cin >> given >> to_make;
	for (int i = 0; i < given; i++) {
		int temp;
		cin >> temp;
		if (max < temp) {
			max = temp;
		}
		lines.push_back(temp);
	}

	long long answer = 0;
	while (min <= max) {
		long long target = (max + min) / 2;

		if (cut_lines(lines, target) < to_make) {
			max = target - 1;
		}
		else {
			if (answer < target) {
				answer = target;
			}
			min = target + 1;
		}
	}
	cout << answer;
}