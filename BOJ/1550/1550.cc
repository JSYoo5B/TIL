#include <iostream>
#include <string>

using namespace std;

int main(void) {
	string hex_num;
	cin >> hex_num;

	int dec_num = 0;
	for (char& c : hex_num) {
		dec_num *= 16;
		if (c >= '0' && c <= '9')
			dec_num += (c - '0');
		else if (c >= 'A' && c <= 'F')
			dec_num += (c - 'A' + 10);
		else if (c >= 'a' && c <= 'f')
			dec_num += (c - 'a' + 10);
	}
	cout << dec_num;
}
