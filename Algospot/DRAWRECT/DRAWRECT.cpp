#include <cstdio>

using namespace std;

int main(void)
{
	int test_cases;
	int x, y;
	int ans_x, ans_y;

	scanf("%d", &test_cases);

	for (int test = 0 ; test < test_cases; test++)
	{
		ans_x = 0;
		ans_y = 0;
		for (int point = 0; point < 3; point++)
		{
			scanf(" %d %d", &x, &y);
			if (point == 1 && x == ans_x)
			{
				ans_x = 0;
			}
			else if (point == 2 && ans_x != 0)
			{
				ans_x -= x;
			}
			else
			{
				ans_x += x;
			}
			if (point == 1 && y == ans_y)
			{
				ans_y = 0;
			}
			else if (point == 2 && ans_y != 0)
			{
				ans_y -= y;
			}
			else
			{
				ans_y += y;
			}
		}

		printf("%d %d\n", ans_x, ans_y);
	}
	return 0;
}
