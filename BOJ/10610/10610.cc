#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int main(void) {
	char c;

	vector<int> num;
	bool zero_found = false;
	int div_3 = 0;
	do {
		scanf("%c", &c);
		if (c >= '0' && c <= '9') {
			num.push_back(c - '0');
			div_3 += (c - '0');
			div_3 %= 3;
		}
		if (c == '0')
			zero_found = true;
	} while (c != '\n');

	if (div_3 == 0 && zero_found) {
		sort(num.begin(), num.end(), greater<int>());
		for (int n : num) {
			printf("%d", n);
		}
	}
	else {
		printf("-1");
	}
}