#include <iostream>
using namespace std;

int main(void) {
	int score;
	int sum = 0;
	for (int i = 0; i < 5; i++) {
		cin >> score;
		if (score < 40)
			score = 40;
		sum += score;
	}
	cout << (sum / 5) << endl;
}