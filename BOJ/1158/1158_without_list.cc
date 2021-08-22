#include <iostream>
#include <cstring>

using namespace std;

int main(void) {
	int n;
	cin >> n;

	bool* josephus = new bool[n];
	memset(josephus, 0, (sizeof(bool) * n));

	int m;
	cin >> m;
	josephus[m-1] = true;

	cout << "<" << m;

	int current = m - 1;
	for (int i = 1; i < n; i++) {
		int count = 0;
		while (count < m) {
			current = (current + 1) % n;
			if (josephus[current] == false)
				count++;
		}
		josephus[current] = true;
		cout << ", " << current + 1;
	}
	cout << ">";
}