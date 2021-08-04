#include <iostream>
using namespace std;

int main(void) {
	int cases, limit;

	cin >> cases >> limit;
	int lower[10000];
	int j = 0;
	for (int i = 0; i < cases; i++) {
		int number;
		cin >> number;
		if (number < limit) {
			lower[j] = number;
			j++;
		}
	}
	for (int i = 0; i < (j - 1); i++) {
		cout << lower[i] << " ";
	}
	if (j != 0)
		cout << lower[j-1] << endl;
}