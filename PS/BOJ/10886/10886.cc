#include <iostream>

using namespace std;

int main(void) {
	int people;
	cin >> people;

	int cute = 0;
	int not_cute = 0;

	for (int i = 0; i < people; i++) {
		int input;
		cin >> input;

		if (input == 0)
			not_cute++;
		else if (input == 1)
			cute++;
	}

	cout << "Junhee is " << ((cute > not_cute) ? "cute!" : "not cute!");
}