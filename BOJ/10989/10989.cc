#include <iostream>
#include <cstring>

using namespace std;

int main(void) {
    cin.tie(NULL);
    ios::sync_with_stdio(false);
	int cases;
	cin >> cases;

	int count[10001];
	memset(count, 0, sizeof(int) * 10001);
	for (int i = 0; i < cases; i++) {
		int input;
		cin >> input;
		count[input]++;
	}

	for (int i = 0; i < 10001; i++) {
		for (int j = 0; j < count[i]; j++) {
			cout << i << '\n';
		}
	}
} 
