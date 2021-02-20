#include <iostream>

using namespace std;

int main(void) {
	int hour, minute, second;
	cin >> hour >> minute >> second;

	int time_elapsed;
	cin >> time_elapsed;

	second += (time_elapsed % 60);
	time_elapsed /= 60;
	time_elapsed += second / 60;
	second %= 60;

	minute += (time_elapsed % 60);
	time_elapsed /= 60;
	time_elapsed += minute / 60;
	minute %= 60;

	hour += (time_elapsed % 24);
	time_elapsed /= 24;
	time_elapsed += hour / 24;
	hour %= 24;

	cout << hour << ' ' << minute << ' ' << second;
}