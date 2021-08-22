#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string input;
	while(getline(cin, input)) {
		int lower = 0, upper = 0, num = 0, space = 0;

		for (char& c : input) {
			if (c >= 'A' && c <= 'Z') 
				upper++;
			if (c >= 'a' && c <= 'z')
				lower++;
			if (c == ' ')
				space++;
			if (c >= '0' && c <= '9')
				num++;
		}

		cout << lower << ' ' << upper << ' '
			<< num << ' ' << space << '\n';
	}
}