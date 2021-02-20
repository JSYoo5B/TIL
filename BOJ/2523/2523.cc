#include <iostream>

using namespace std;

int main(void) {
	int input;
	cin >> input;

	for (int i = 0; i < input; i++) {
		for (int j = 0; j < i+1; j++) {
			cout << '*';
		}
		cout << '\n';
	}
	for (int i = input - 1; i > 0; i--) {
		for (int j = 0; j < i; j++) {
			cout << '*';
		}
		cout << '\n';
	}
}