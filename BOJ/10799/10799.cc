#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main(void) {
	string order;
	cin >> order;

	stack<char> sticks;
	int n_sticks = 0;
	char last_c = ')';
	for (char& c : order) {
		if (c == '(')
			sticks.push(c);
		else if (c == ')') {
			sticks.pop();
			if (last_c == '(')
				n_sticks += sticks.size();
			else 
				n_sticks++;
		}
		last_c = c;
	}
	cout << n_sticks;
}