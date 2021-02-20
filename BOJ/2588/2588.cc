#include <iostream>

using namespace std;

int main(void) {
	int a, b;
	cin >> a >> b;

	int result = a * b;

	while(b > 0) {
		cout << a * (b % 10) << '\n';
		b /= 10;
	}
	cout << result;
}