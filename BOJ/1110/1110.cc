#include <iostream>

using namespace std;

int main(void) {
	int origin;

	cin >> origin;
	int count = 0;
	int next = origin;

	do {
		next = (next % 10) * 10 
				+ ((next / 10) + (next % 10)) % 10;
		count++;
	} while (next != origin);

	cout << count;
}