#include <iostream>
#include <string>
#include <queue>

using namespace std;

int main(void) {
	queue<int> my_queue;

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		string operation;
		int temp;
		cin >> operation;

		if (operation.compare("push") == 0) {
			cin >> temp;
			my_queue.push(temp);
		}
		else if (operation.compare("pop") == 0) {
			if (my_queue.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << my_queue.front() << '\n';
				my_queue.pop();
			}
		}
		else if (operation.compare("size") == 0) {
			cout << my_queue.size() << '\n';
		}
		else if (operation.compare("empty") == 0) {
			cout << (my_queue.empty() ? 1 : 0) << '\n';
		}
		else if (operation.compare("front") == 0) {
			cout << (my_queue.empty() ? -1 : my_queue.front()) << '\n';
		}
		else if (operation.compare("back") == 0) {
			cout << (my_queue.empty() ? -1 : my_queue.back()) << '\n';
		}
	}
}