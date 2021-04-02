#include <iostream>
#include <climits>

using namespace std;

int last_room(int nth) {
	return (nth * (nth - 1) * 3) + 1;
}

int main(void) {
	int room_number;
	cin >> room_number;

	for (int i = 1; last_room(i) < INT_MAX; i++) {
		if (last_room(i) >= room_number) {
			cout << i << endl;
			break;
		}
	}
}