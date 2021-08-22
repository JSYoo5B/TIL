// an expedient soluiton
#include <iostream>
using namespace std;

#define MAX_NUMBER 2000003
#define MID_NUMBER 1000001

int main(void) {
	bool is_member[MAX_NUMBER] = { false };
	int numbers;
	cin >> numbers;

	int min_num = 2000000;
	int max_num = 0;
	for (int i = 0; i < numbers; i++) {
		int input;
		cin >> input;

		// to avoid negative index, 
		input += MID_NUMBER;
		is_member[input] = true;
		// to improve scope
		if (input > max_num)
			max_num = input;
		if (input < min_num)
			min_num = input;
	}

	for (int i = min_num; i <= max_num; i++) {
		if (is_member[i]) {
			cout << i - MID_NUMBER << "\n";
		}
	}
}