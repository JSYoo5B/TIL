#include <iostream>
#include <string>

using std::cin;
using std::cout;
using std::endl;
using std::string;

int main(void) {
	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		string name;
		cin >> name;
		cout << "Hello, " << name << "!" << endl;
	}
	return 0;
}
