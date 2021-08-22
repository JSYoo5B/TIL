#include <iostream>
#include <cmath>
using namespace std;

typedef struct _turret {
	int x;
	int y;
	int radius;
} turret;

int calculate(turret t1, turret t2) {
	int diffx = t1.x - t2.x;
	int diffy = t1.y - t2.y;
	float dist = sqrt(diffx * diffx + diffy * diffy);

	int max_r = (t1.radius > t2.radius) ? t1.radius : t2.radius;
	int min_r = (t1.radius < t2.radius) ? t1.radius : t2.radius;

	// when two turrets are in same position
	if (dist == 0) {
		if (t1.radius == t2.radius) {
			return -1;
		}
		else 
			return 0;
	}
	// when two turrets are tangent
	else if (dist == max_r + min_r || dist == max_r - min_r) {
		return 1;
	}
	// when two turrets are not meet
	else if (dist > max_r + min_r || max_r > dist + min_r) {
		return 0;
	}
	else
		return 2;
}

int main(void) {
	int cases;

	cin >> cases;
	for (int i = 0; i < cases; i++) {
		turret t1, t2;
		cin >> t1.x >> t1.y >> t1.radius
			>> t2.x >> t2.y >> t2.radius;
		cout << calculate(t1, t2) << '\n';
	}
}