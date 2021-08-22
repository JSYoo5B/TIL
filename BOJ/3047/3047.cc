#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int num[3];
	cin >> num[0] >> num[1] >> num[2];

	sort(num, num+3);
	for (int i = 0 ; i < 3; i++) {
		char c;
		cin >> c;
		switch(c) {
			case 'A':
				cout << num[0] << ' ';
				break;
			case 'B':
				cout << num[1] << ' ';
				break;
			case 'C':
				cout << num[2] << ' ';
				break;
		}
	}

}