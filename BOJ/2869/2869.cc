#include <iostream>

using namespace std;

int main(void) {
	int dist, up, down;

	cin >> up >> down >> dist;

	int current = 0;
	int day = 0;

	while(current < dist) {
		day++;
		current += up;
		if (current >= dist)
			break;
		current -= down;
	}

	cout << day;
}