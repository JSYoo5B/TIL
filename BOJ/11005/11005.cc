#include <iostream>
#include <stack>

using namespace std;

int main(void) {
	stack<char> base_nums;

	int number;
	cin >> number;

	int base;
	cin >> base;

	while(number > 0) {
		int new_num = number % base;
		char conv_num;
		if (new_num < 10)
			conv_num = new_num + '0';
		else 
			conv_num = new_num - 10 + 'A'; 
		base_nums.push(conv_num);
		number /= base;
	}

	while(base_nums.empty() == false) {
		cout << base_nums.top();
		base_nums.pop();
	}
}