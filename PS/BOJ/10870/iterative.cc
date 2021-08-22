#include <iostream>

using namespace std;

int main(void) {
	int number;

	cin >> number;

	int fibo_n1 = 1, fibo_n2 = 0;
	int fibo_n = 0;
	for (int i = 0; i < number; i++) {
		fibo_n2 = fibo_n1;
		fibo_n1 = fibo_n;
		fibo_n = fibo_n1 + fibo_n2;
		
	}
	cout << fibo_n << endl;
}