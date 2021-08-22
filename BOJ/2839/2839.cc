#include <cstdio>

using namespace std;

int main(void) {

	int required, cnt_5, cnt_3, remaining;

	scanf("%d", &required);

	// TODO:: allocating algorithm goes here
	cnt_5 = required / 5;
	cnt_3 = 0;
	remaining = required % 5;

	for (cnt_5 = required / 5; cnt_5 >= 0; cnt_5--) {
		remaining = required - (cnt_5 * 5);
		if ((remaining % 3) == 0) {
			cnt_3 = remaining / 3;
			break;
		}
	}
	remaining = required - (cnt_5 * 5) - (cnt_3 * 3);

	if (remaining == 0)
		printf("%d", cnt_3 + cnt_5);
	else 
		printf("-1");

}