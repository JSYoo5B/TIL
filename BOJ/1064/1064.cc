#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

double dist(int x1, int y1, int x2, int y2) {
	double diffx = x1 - x2;
	double diffy = y1 - y2;

	return sqrt(diffx * diffx + diffy * diffy);
}

bool is_line(int x1, int y1, int x2, int y2, int x3, int y3) {
	// this works same as (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)
	return ((y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1));
}

int main(void) {
	int x1, y1, x2, y2, x3, y3;
	scanf("%d%d%d%d%d%d", &x1, &y1, &x2, &y2, &x3, &y3);

	if (is_line(x1, y1, x2, y2, x3, y3)) {
		printf("-1");
		return 0;
	}

	double line[3];
	line[0] = dist(x1, y1, x2, y2);
	line[1] = dist(x1, y1, x3, y3);
	line[2] = dist(x2, y2, x3, y3);
	sort(line, line+3);

	printf("%.10lf\n", 2.0 * (line[2] - line[0]));
}