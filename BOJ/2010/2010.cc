#include <iostream>

using namespace std;

int main(void) {
	int n_taps;
	cin >> n_taps;

	int total_holes = 1;
	for (int i = 0; i < n_taps; i++) {
		int n_holes;
		cin >> n_holes;
		total_holes += n_holes - 1;
	}
	cout << total_holes;
}