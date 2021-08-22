#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int n_people;
	cin >> n_people;

	int* wait = new int[n_people];
	for (int i = 0; i < n_people; i++) {
		cin >> wait[i];
	}
	sort(wait, wait+n_people);

	int total_wait = 0;
	for (int i = 0; i < n_people; i++) {
		for (int j = 0; j <= i; j++) {
			total_wait += wait[j];
		}
	}
	cout << total_wait;
}