#include <cstdio>
#include <vector>

using namespace std;

int main(void) {
	int cases;
	vector<int> scores;
	int max = 0;

	scanf("%d", &cases);
	for (int i = 0; i < cases; i++) {
		int temp;
		scanf("%d", &temp);
		if (max < temp) {
			max = temp;
		}
		scores.push_back(temp);
	}

	float sum = 0.0f;
	for (auto score : scores) {
		sum += (float) score / max;
	}
	sum *= 100;

	printf("%.2f", sum / (float) cases);
}