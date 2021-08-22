#include <iostream>

using namespace std;

typedef struct _point {
	int x, y;
} Point;
typedef struct _circle {
	int x, y, radius;
} Circle;

bool point_in_circle(Point p, Circle c) {
	int diff_x = c.x - p.x;
	int diff_y = c.y - p.y;
	int dist2 = diff_x * diff_x + diff_y * diff_y;
	int rad2 = c.radius * c.radius;

	return rad2 > dist2;
}

int main(void) {
	Point src, dst;
	int cases;

	cin >> cases;
	

	for (int i = 0; i < cases; i++) {
		cin >> src.x >> src.y >> dst.x >> dst.y;
		int n_circle;
		int count_boundary = 0;

		cin >> n_circle;
		for (int j = 0; j < n_circle; j++) {
			Circle c;
			cin >> c.x >> c.y >> c.radius;

			// circle should exclusively include one point
			bool src_in_circle = point_in_circle(src, c);
			bool dst_in_circle = point_in_circle(dst, c);
			if ((src_in_circle && !dst_in_circle) ||
				(!src_in_circle && dst_in_circle)) {
				count_boundary++;
			}
		}
		cout << count_boundary << endl;
	}
}