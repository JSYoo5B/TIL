#include <iostream>
#include <string>
#include <deque>

using namespace std;

int main(void) {
	deque<int> my_deque;

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		string operation;
		int temp;
		cin >> operation;

		if (operation.compare("push_front") == 0) {
			cin >> temp;
			my_deque.push_front(temp);
		}
		else if (operation.compare("push_back") == 0) {
			cin >> temp;
			my_deque.push_back(temp);
		}
		else if (operation.compare("pop_front") == 0) {
			if (my_deque.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << my_deque.front() << '\n';
				my_deque.pop_front();
			}
		}
		else if (operation.compare("pop_back") == 0) {
			if (my_deque.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << my_deque.back() << '\n';
				my_deque.pop_back();
			}
		}
		else if (operation.compare("size") == 0) {
			cout << my_deque.size() << '\n';
		}
		else if (operation.compare("empty") == 0) {
			cout << (my_deque.empty() ? 1 : 0) << '\n';
		}
		else if (operation.compare("front") == 0) {

			cout << (my_deque.empty() ? -1 : my_deque.front()) << '\n';
		}
		else if (operation.compare("back") == 0) {
			cout << (my_deque.empty() ? -1 : my_deque.back()) << '\n';
		}
	}
}