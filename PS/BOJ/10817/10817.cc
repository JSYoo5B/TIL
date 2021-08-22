#include <iostream>
#include <algorithm>
using namespace std;

int main(void) {
	int numbers[3];
	for (int i  = 0; i < 3; i++) {
		cin >> numbers[i];
	}
	sort(numbers, numbers + 3);
	cout << numbers[1] << endl;
}