#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int main(void) {
	string input;
	cin >> input;

	int location[26];
	memset(location, -1, sizeof(int) * 26);
	for (int i = 0; i < input.length(); i++) {
		if (location[input[i] - 'a'] == -1)
			location[input[i] - 'a'] = i;
	}

	for (int i = 0; i < 26; i++) {
		cout << location[i] << ' ';
	}
}