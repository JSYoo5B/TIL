#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string line;
	getline(cin, line);

	for (char& c : line) {
		if ((c >= 'a' && c <= 'm') || (c >= 'A' && c <= 'M'))
			c += 13;
		else if ((c >= 'n' && c <= 'z') || (c >= 'N' && c <= 'Z'))
			c -= 13;
	}
	cout << line;
}