#include <iostream>
using namespace std;

int main(void) {
	int hour, minute;
	int time_to_cook;

	cin >> hour >> minute;
	cin >> time_to_cook;

	minute += time_to_cook;
	hour += (minute / 60);
	hour %= 24;
	minute %= 60;

	cout << hour << " " << minute << endl;
}