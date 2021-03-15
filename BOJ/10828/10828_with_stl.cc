#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main(void) {
	stack<int> my_stack;

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		string operation;
		int temp;
		cin >> operation;

		if (operation.compare("push") == 0) {
			cin >> temp;
			my_stack.push(temp);
		}
		else if (operation.compare("pop") == 0) {
			if (my_stack.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << my_stack.top() << '\n';
				my_stack.pop();
			}
		}
		else if (operation.compare("size") == 0) {
			cout << my_stack.size() << '\n';
		}
		else if (operation.compare("empty") == 0) {
			cout << (my_stack.empty() ? 1 : 0) << '\n';
		}
		else if (operation.compare("top") == 0) {
			cout << (my_stack.empty() ? -1 : my_stack.top()) << '\n';
		}
	}
}