#include <iostream>

using namespace std;
int main(void) {
	int req;
	cin >> req;

	for (int line = 1; line <= req; line++) {
		for (int star = 0; star < line; star++) {
			cout << '*';
		}
		cout << endl;
	}
}