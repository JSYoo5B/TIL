#include <iostream>

using namespace std;

int main(void) {
	int num[8];

	for (int i = 0; i < 8; i++) {
		cin >> num[i];
	}

	bool asc = false; 
	bool des = false;

	for (int i = 0; i < 7; i++) {
		if (num[i] < num[i + 1])
			asc = true;
		if (num[i] > num[i + 1])
			des = true;
	}

	if (asc && des) 
		cout << "mixed";
	else if (asc)
		cout << "ascending";
	else
		cout << "descending";
}