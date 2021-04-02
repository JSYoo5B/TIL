#include <iostream>
#include <string>

using namespace std;

int main(void) {
	int cases;
	cin >> cases;

	for (int i = 0; i < cases; i++) {
		string s1;
		string s2;
		cin >> s1 >> s2;

		int dist = 0;
		for (int i = 0; i < s1.length(); i++) {
			if (s1[i] != s2[i])
				dist++;
		}

		cout << "Hamming distance is " << dist << ".\n";
	}
}