#include <iostream>

using namespace std;

int main(void) {
	int remainder[10][4] = {{10},
							{1},
							{2, 4, 8, 6},
 							{3, 9, 7, 1},
							{4, 6},
							{5},
							{6},
							{7, 9, 3, 1},
							{8, 4, 2, 6},
							{9, 1}};
	int rem_len[10] = {1, 1, 4, 4, 2, 1, 1, 4, 4, 2};
	int a, b;
	int cases;

	cin >> cases;

	for (int i = 0; i < cases; i++) {
		cin >> a >> b;
		b--;
		b %= rem_len[a % 10];
		int result = remainder[a % 10][b];
		cout << result << endl;
	}
}