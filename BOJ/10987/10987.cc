#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string word;
	cin >> word;

	int vowel = 0;
	for (char& c: word) {
		if (c == 'a' || c == 'e' || c == 'i' 
				|| c == 'o' || c == 'u') {
			vowel++;
		}
	}
	cout << vowel;
}