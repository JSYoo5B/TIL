#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string input;
	cin >> input;

	int numbers = 1;
	for (char& c : input) {
		if (c == ',')
			numbers++;
	}
	cout << numbers;
}