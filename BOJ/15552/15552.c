#include <stdio.h>

int main(void)
{
	int cases;
	int a, b;
	
	int i;

	scanf("%d", &cases);
	for (i = 0; i < cases; i++)
	{
		scanf("%d %d", &a, &b);
		printf("%d\n", a+b);
	}
}
