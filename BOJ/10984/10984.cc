#include <cstdio>

using namespace std;

int main(void) {
	int cases;
	scanf("%d", &cases);

	for (int t = 0; t < cases; t++) {
		int subjects;
		scanf("%d", &subjects);
		int full = 0;
		float gpa = 0.0f;
		for (int i = 0; i < subjects; i++) {
			int credit;
			float grade;
			scanf("%d %f", &credit, &grade);

			gpa = (gpa * full) / (full + credit)
					+ (grade * credit) / (full + credit);
			full += credit;
		}
		printf("%d %.1f\n", full, gpa);
	}
}
