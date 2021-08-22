#include <iostream>

using namespace std;

int main(void) {
	int num[5];

	for(int i = 0; i < 5; i++) 
		cin >> num[i];

	int crc = 0;
	for (int i = 0; i < 5; i++) {
		crc += num[i] * num[i];
	}

	cout << crc % 10;
}