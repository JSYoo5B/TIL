#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		string ps;
		cin >> ps;

		int pair = 0;
		for (char& c : ps) {
			if (c == '(')
				pair++;
			else if (c == ')')
				pair--;
			if (pair < 0)
				break;
		}

		if (pair == 0)
			cout << "YES\n";
		else
			cout << "NO\n";
	}
}