#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

using namespace std;

int main(void) {
	string word;
	cin >> word;

	int alphabet_count[26];
	memset(alphabet_count, 0, sizeof(int) * 26);

	for (char c : word) {
		if (c >= 'a' && c <= 'z')
			c -= 32;
		alphabet_count[c - 'A']++;
	}

	int max_idx = 0;
	int max_count = 0;
	for (int i = 0; i < 26; i++) {
		if (alphabet_count[i] >= max_count){
			max_count = alphabet_count[i];
			max_idx = i;
		}
	}

	sort(alphabet_count, alphabet_count + 26);
	if (alphabet_count[25] == alphabet_count[24])
		cout << '?';
	else 
		cout << (char)(max_idx + 'A');

}