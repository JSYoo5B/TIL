#include <iostream>
#include <string>
using namespace std;

int main(void) {
	string s;
	int base;

	cin >> s >> base;

	int total = 0;
	for (char& c : s) {
		total *= base;

		int current;
		if (c >= '0' && c <= '9')
			current = c - '0';
		else if (c >= 'A' && c <= 'Z')
			current = c - 'A' + 10;

		total += current;
	}

	cout << total;
}