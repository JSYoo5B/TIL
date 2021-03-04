#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int start, end;
		cin >> start >> end;

		int diff = end - start;
		int max_speed = (int)sqrt(diff);
		int warp_count = 2 * max_speed - 1;

		diff -= max_speed * max_speed;

		warp_count += diff / max_speed;
		if (diff % max_speed != 0)
			warp_count++;

		cout << warp_count << '\n';
	}
}