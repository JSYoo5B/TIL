#include <iostream>
#include <string>

using namespace std;

bool is_palindrome(string str) {
	int left = 0;
	int right = str.length() - 1;

	while(left <= right) {
		if (str[left] != str[right])
			return false;
		left++;
		right--;
	}
	return true;
}

int main(void) {
	string input;
	cin >> input;

	cout << is_palindrome(input);
}