#include <iostream>
using namespace std;

long long combination(int object, int sample) {
	long long result = 1;
	for (int i = 1; i <= sample; i++) {
		result *= (object - i + 1);
		result /= i;
	}
	return result;
}

int main(void) {
	int cases;

	cin >> cases;
	for (int i = 0; i < cases; i++) {
		int west, east;
		cin >> west >> east;
		cout << combination(east, west) << '\n';
	}
}