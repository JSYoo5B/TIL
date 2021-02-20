#include <iostream>

using namespace std;
int main(void) {
	int req;
	cin >> req;

	for (int line = 1; line <= req; line++) {
		for (int blank = req - line; blank > 0; blank--) {
			cout << ' ';
		}
		for (int star = 0; star < line; star++) {
			cout << '*';
		}
		cout << endl;
	}
}