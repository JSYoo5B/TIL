#include <iostream>

using namespace std;

int main(void) {
	int input;
	cin >> input;

	int bit_found = 0;
	while (input > 0) {
		if ((input & 1) == 1)
			bit_found++;
		input = input >> 1;
	}

	if (bit_found == 1)
		cout << 1;
	else
		cout << 0;
}