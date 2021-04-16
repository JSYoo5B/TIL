#include <iostream>

using namespace std;

int main(void) {
	int dist, up, down;

	cin >> up >> down >> dist;

	int current = 0;
	int day = 0;

	// change dist to last day
	dist -= up;
	day ++;

	// divide by daily movement
	day += (dist / (up - down));
	// if rest distance exists, add 1 more day
	day += (dist % (up - down)) > 0 ? 1 : 0;
	cout << day;
}