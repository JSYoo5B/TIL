#include <iostream>
#include <string>
#include <regex>
#include <vector>

using namespace std;
int main(void) {
	string input;
	regex reg("\\s+");

	getline(cin, input);
	int words = 0;
	bool counting_blank = true;
	for (int i = 0; i < input.length(); i++) {
		if (input[i] == ' ' && counting_blank == true) {
			continue;
		}
		else if (input[i] == ' ' && counting_blank != true) {
			counting_blank = true;
			continue;
		}
		else if (input[i] != ' ' && counting_blank == true) {
			words++;
			counting_blank = false;
		}
		else if (input[i] != ' ' && counting_blank != true) {
			continue;
		}
	}

	cout << words << endl;
}