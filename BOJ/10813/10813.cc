#include <iostream>
#include <algorithm>

using namespace std;

int main(void) {
	int n_bucket, trials;
	cin >> n_bucket >> trials;

	int* bucket = new int[n_bucket];
	for(int i = 0; i < n_bucket; i++) {
		bucket[i] = i + 1;
	}
	for(int i = 0; i < trials; i++) {
		int src, dst;
		cin >> src >> dst;
		if (src == dst)
			continue;

		src--; dst--;
		swap(bucket[src], bucket[dst]); 
	}

	cout << bucket[0];
	for (int i = 1; i < n_bucket; i++)
		cout << ' ' << bucket[i];
}