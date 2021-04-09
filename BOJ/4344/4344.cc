#include <cstdio>

using namespace std;

float overscore() {
	int students;
	scanf("%d", &students);
	int* score = new int[students];
	float average = 0.0f;

	for (int i = 0; i < students; i++) {
		scanf("%d", &score[i]);
		average = ((float)average * i / (i + 1)) 
				+ ((float)score[i] / (i + 1));
	}
	
	int overlings = 0;
	for (int i = 0; i < students; i++) {
		if ((float)(score[i]) > (float)average)
			overlings++;
	}

	return (float)100 * ((float)overlings / students);
}

int main(void) {
	int cases;

	scanf("%d", &cases);

	for (int i = 0; i < cases; i++) {
		printf("%.3f%%\n", overscore());
	}
}