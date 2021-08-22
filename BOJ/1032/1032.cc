#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int files;
	cin >> files;

	string* filename = new string[files];
	for (int i = 0; i < files; i++) {
		cin >> filename[i];
	}

	int len = filename[0].length();
	string pattern(len, '?');
	for (int i = 0; i < len; i++) {
		char next_c = filename[0][i];
		for (int j = 1; j < files; j++) {
			if (filename[j-1][i] != filename[j][i]){
				next_c = '?';
				break;
			}
		}
		pattern[i] = next_c;
	}
	cout << pattern;
}