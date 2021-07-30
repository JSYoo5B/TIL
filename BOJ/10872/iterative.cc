#include <iostream>
using namespace std;

int main(void) {
	int number;
	int factorial = 1;

	cin >> number;
	for (int i = 1; i <= number; i++) {
		factorial *= i;
	}
	cout << factorial << endl;
}