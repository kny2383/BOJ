#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
	int A = 0;
	int I = 0;
	scanf("%d %d", &A, &I);
	printf("%d", A * (I - 1) + 1);
	return 0;
}

