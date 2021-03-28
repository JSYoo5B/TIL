#include <iostream>
#include <string>
using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	int cases;
	cin >> cases;

	for(int i = 0; i < cases; i++) {
		string number;
		cin >> number;

		if (((number.back() - '0') % 2) == 0)
			cout << "even\n";
		else
			cout << "odd\n";
	}
}