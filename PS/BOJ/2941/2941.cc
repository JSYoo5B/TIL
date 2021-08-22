#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string word;
	cin >> word;

	int croatian_char = 0;
	for (int i = 0; i < word.length(); i++) {
		if (word[i] == 'c' && word[i+1] == '=') {
			i++;
		}
		else if (word[i] == 'c' && word[i+1] == '-') {
			i++;
		}
		else if (word[i] == 'd' && word[i+1] == 'z' && word[i+2] == '=') {
			i += 2;
		}
		else if (word[i] == 'd' && word[i+1] == '-') {
			i++;
		}
		else if (word[i] == 'l' && word[i+1] == 'j') {
			i++;
		}
		else if (word[i] == 'n' && word[i+1] == 'j') {
			i++;
		}
		else if (word[i] == 's' && word[i+1] == '=') {
			i++;
		}
		else if (word[i] == 'z' && word[i+1] == '=') {
			i++;
		}
		croatian_char++;
	}
	cout << croatian_char;
}