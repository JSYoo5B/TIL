#include <iostream>
#include <cstring>
#include <string>

using namespace std;

int main(void) {
	string word;
	cin >> word;


	int count[26];
	memset(count, 0, (sizeof(int) * 26));

	for (char& c : word) {
		count[c - 'a']++;
	}

	for (int i = 0; i < 26; i++) {
		cout << count[i] << ' ';
	}
}