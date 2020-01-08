#include <cstdio>
#include <cstring>

using namespace std;

int main(void)
{
	int test_cases;
	int text_len;
	char plain_text[101];

	scanf("%d", &test_cases);
	for (int test = 0; test < test_cases; test++)
	{
		scanf(" %s", plain_text);
		text_len = strlen(plain_text);
		for (int i = 0 ; i < text_len; i += 2)
		{
			printf("%c", plain_text[i]);
		}
		for (int i = 1 ; i < text_len; i += 2)
		{
			printf("%c", plain_text[i]);
		}
		printf("\n");
	}

	return 0;
}
