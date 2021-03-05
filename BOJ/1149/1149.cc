#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int houses;
	cin >> houses;

	int price[1001][3];
	for (int i = 1; i <= houses; i++) {
		cin >> price[i][0] >> price[i][1] >> price[i][2];
	}

	long long total[1001][3];
	total[1][0] = price[1][0];
	total[1][1] = price[1][1];
	total[1][2] = price[1][2];
	for (int i = 2; i <= houses; i++) {
		total[i][0] = min(total[i-1][1], total[i-1][2]) + price[i][0];
		total[i][1] = min(total[i-1][2], total[i-1][0]) + price[i][1];
		total[i][2] = min(total[i-1][0], total[i-1][1]) + price[i][2];
	}
	long long min_price = min(total[houses][0], min(total[houses][1], total[houses][2]));
	cout << min_price;
}