#include <iostream>

using namespace std;

int main(void) {
	int gandalf_score[] = {1, 2, 3, 3, 4, 10};
	int sauron_score[] = {1, 2, 2, 2, 3, 5, 10};

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int gandalf_army[6];
		for (int j = 0; j < 6; j++) 
			cin >> gandalf_army[j];
		int sauron_army[7];
		for (int j = 0; j < 7; j++) 
			cin >> sauron_army[j];

		int gandalf_battle = 0;
		for (int j = 0; j < 6; j++) 
			gandalf_battle += gandalf_army[j] * gandalf_score[j];
		int sauron_battle = 0;
		for (int j = 0; j < 7; j++) 
			sauron_battle += sauron_army[j] * sauron_score[j];

		cout << "Battle " << i+1 << ": ";
		if (gandalf_battle > sauron_battle)
			cout << "Good triumphs over Evil\n";
		else if (gandalf_battle < sauron_battle)
			cout << "Evil eradicates all trace of Good\n";
		else
			cout << "No victor on this battle field\n";
	}
}