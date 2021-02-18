#include <iostream>

using namespace std;

int main(void) {
	for (int i = 0; i < 3; i++) {
		int back = 0;
		for (int j = 0; j < 4; j++) {
			int n;
			cin >> n;
			if (n == 1)
				back++;
		}

		switch(back) {
			case 0:
			cout << 'D';
			break;

			case 1:
			cout << 'C';
			break;

			case 2:
			cout << 'B';
			break;

			case 3:
			cout << 'A';
			break;

			case 4:
			cout << 'E';
			break;
		}
		cout << '\n';
	}
}