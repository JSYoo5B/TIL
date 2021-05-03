#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

typedef struct _coord {
	int x, y;
} Coord;

int main(void) {
	int cases;
	cin >> cases;

	vector<Coord> points;
	for (int i = 0; i < cases; i++) {
		Coord p;
		cin >> p.x >> p.y;
		points.push_back(p);
	}

	sort(points.begin(), points.end(), [](const Coord& a, const Coord& b) {
		if (a.y < b.y)
			return true;
		else if (a.y == b.y)
			return a.x < b.x;
		else
			return false;
	});

	for (auto& p : points) {
		cout << p.x << ' ' << p.y << '\n';
	}
}