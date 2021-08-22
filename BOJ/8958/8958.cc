#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		string scores;
		cin >> scores;

		int max_correct = 0;
		int current_correct = 0;
		for (char& c : scores) {
			if (c == 'O') {
				current_correct++;
				max_correct += current_correct;
			}
			else {
				current_correct = 0;
			}
		}
		cout << max_correct << '\n';
	}
}