#include <iostream>
#include <cstring>

using namespace std;

int main(void) {
	int a, b, c;
	cin >> a >> b >> c;

	int mul = a * b * c;
	int count[10];
	memset(count, 0, sizeof(int) * 10);

	while (mul > 0) {
		count[mul % 10] ++;
		mul /= 10;
	}

	for (int i = 0; i < 10; i++) {
		cout << count[i] << '\n';
	}
}