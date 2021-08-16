#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int a = 0;
	int b = 0;
	int c = 0;
	int sol;
	scanf("%d %d %d", &a, &b,&c);
	if ((a == b) && (b == c)&&(c==a))
		printf("%d", 10000 + a * 1000);
	else if ((a == b) || (c==a))
		printf("%d",1000 + a * 100);
	else if (b == c)
		printf("%d", 1000 + b * 100);
	if (a > b) 
	{
		int max = a;
		if (a < c)
			max = c;
		sol = max * 100;
	}
	else if (a < b)
	{
		int max = b;
		if (b < c)
			max = c;
		sol = max * 100;
	}
	printf("%d", sol);
	return 0;
}

