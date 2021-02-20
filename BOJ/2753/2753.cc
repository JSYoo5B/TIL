#include <iostream>

using namespace std;

bool leap_year(int year) {
	if (year % 4 != 0)
		return 0;
	if (year % 400 == 0)
		return 1;
	if (year % 100 == 0)
		return 0;
	return 1;
}

int main(void) {
	int year;
	cin >> year;

	cout << leap_year(year);
}