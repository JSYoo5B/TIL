#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	int not_group = 0;
	for (int i = 0; i < cases; i++) {
		string word;
		cin >> word;

		bool duplicate[26];
		memset(duplicate, 0, sizeof(bool) * 26);
		char last_c = '0';
		for (char c : word) {
			if (last_c != c) {
				last_c = c;
				if (duplicate[c - 'a'] == true) {
					not_group++;
					break;
				}
				duplicate[c - 'a'] = true;
			}

		}

	}
	cout << cases - not_group;
}