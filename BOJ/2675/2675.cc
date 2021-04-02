#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		int repeat;
		string str;
		cin >> repeat >> str;

		for (char& c : str) {
			for (int j = 0; j < repeat; j++) {
				cout << c;
			}
		}
		cout << '\n';
	}
}