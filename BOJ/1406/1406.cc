// Using stack for "after cursor area"

#include <iostream>
#include <string>
#include <stack>

using namespace std;

string before_cursor;
stack<char> after_cursor;

void move_left() {
	if (before_cursor.length() == 0)
		return;
	char c = before_cursor.back();
	before_cursor.pop_back();
	after_cursor.push(c);
}

void move_right() {
	if (after_cursor.empty() == true)
		return;
	char c = after_cursor.top();
	after_cursor.pop();
	before_cursor.push_back(c);
}

void back_space() {
	if (before_cursor.length() == 0)
		return;
	before_cursor.pop_back();
}

void write_char(char c) {
	before_cursor.push_back(c);
}

int main(void) {
	cin >> before_cursor;

	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		char command;
		cin >> command;

		switch(command) {
			case 'L':
				move_left();
				break;
			case 'D':
				move_right();
				break;
			case 'B':
				back_space();
				break;
			case 'P':
				char c;
				cin >> c;
				write_char(c);
		}
	}

	cout << before_cursor;
	while(after_cursor.empty() == false) {
		cout << after_cursor.top();
		after_cursor.pop();
	}
}