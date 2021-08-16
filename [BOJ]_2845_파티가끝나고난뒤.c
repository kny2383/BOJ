#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int L, P;
	int n[5];
	int k[5];
	scanf("%d %d\n", &L, &P);
	for (int i=0; i <5; i++)
	{
		scanf("%d", &n[i]);
		k[i] = L * P - n[i];
	}

	if (n < 0 || n >= 10 * 10 * 10 * 10 * 10 * 10)
	{
		printf("다시입력\n");
		exit();
	}
	
	for (int j = 0; j < 5; j++)
	{
		printf("%d ", k[j]);
	}
	return 0;
}