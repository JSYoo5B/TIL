#include <iostream>

using namespace std;
int main(void) {
	int req;
	cin >> req;

	for (int line = 1; line < req; line++) {
		for (int blank = req - line; blank > 0; blank--) {
			cout << ' ';
		}
		if (line == 1)
			cout << "*";
		else 
			cout << "* ";
		for (int star = 2; star < line; star++) {
			cout << "  ";
		}
		if (line != 1)
			cout << "*" << endl;
		else
			cout << endl;
	}
	for (int star = 1; star < req; star++) {
		cout << "**";
	}
	cout << "*" << endl;
}