#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string s;
	cin >> s;

	int start = 0;
	if (s.length() % 3 == 2) {
		cout << ((s[0] - '0') * 2 + (s[1] - '0'));
		start = 2;
	}
	else if (s.length() % 3 == 1) {
		cout << (s[0] - '0');
		start = 1;
	}
	int len = s.length();
	for (int i = start; i < len; i += 3) {
		cout << (((s[i] - '0') * 4) 
				+ ((s[i+1] - '0') * 2) 
				+ (s[i+2] - '0'));
	}
}