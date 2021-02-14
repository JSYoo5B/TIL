#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int x, y, w, h;

	cin >> x >> y >> w >> h;

	int diff[4];
	diff[0] = w - x;
	diff[1] = x;
	diff[2] = h - y;
	diff[3] = y;

	sort(diff, diff+4);

	cout << diff[0];
}