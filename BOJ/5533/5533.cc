#include <iostream>
#include <cstring>

using namespace std;

int main(void) {
	int scores[200][3];

	int n_people;
	cin >> n_people;

	for (int i = 0; i < n_people; i++) {
		cin >> scores[i][0] >> scores[i][1] >> scores[i][2];
	}

	int total_score[200];
	memset(total_score, 0, sizeof(int) * 200);
	for (int j = 0; j < 3; j++) {
		int score_count[101];
		memset(score_count, 0, sizeof(int) * 101);
		for (int i = 0; i < n_people; i++) {
			score_count[scores[i][j]]++;
		}

		for (int i = 0; i < n_people; i++) {
			if (score_count[scores[i][j]] == 1) 
				total_score[i] += scores[i][j];
		}
	}

	for (int i = 0; i < n_people; i++) {
		cout << total_score[i] << '\n';
	}
}