#include <iostream>

using namespace std;

int main(void) {
	int row, col;
	cin >> row >> col;

	int height, width;
	cin >> height >> width;

	for (int r = 0; r < row; r++) {
		for (int h = 0; h < height; h++){
			for (int c = 0; c < col; c++) {
				for (int w = 0; w < width; w++) {
					if ((r + c) % 2 == 0)
						cout << 'X';
					else
						cout << '.';
				}
			}
			cout << '\n';
		}
	}
}