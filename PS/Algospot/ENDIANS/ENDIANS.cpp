#include <cstdio>

using namespace std;

int main(int argc, char* argv[])
{
	int cnt;
	unsigned int value;
	unsigned int swapped;

	scanf("%d", &cnt);
	for (int i = 0; i < cnt; i++)
	{
		scanf("%d", &value);
		swapped = 0x00000000;
		swapped |= (value & 0x000000FF) << 24;
		swapped |= (value & 0x0000FF00) << 8;
		swapped |= (value & 0x00FF0000) >> 8;
		swapped |= (value & 0xFF000000) >> 24;
		printf("%u\n", swapped);
	}
}
