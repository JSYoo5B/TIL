#include <iostream>

using namespace std;

typedef struct _fibo {
	int n;
	int zero;
	int one;
} fibo;

int main(void) {
	fibo memo[41] = {{0, 1, 0}, {1, 0, 1}};

	for (int i = 2; i < 41; i++) {
		memo[i].n = i;
		memo[i].zero = memo[i-1].zero + memo[i-2].zero;
		memo[i].one = memo[i-1].one + memo[i-2].one;
	}

	int cases;
	cin >> cases;
	for (int i = 0; i < cases; i++) {
		int n;
		cin >> n;
		cout << memo[n].zero << ' ' << memo[n].one << '\n';
	}
}