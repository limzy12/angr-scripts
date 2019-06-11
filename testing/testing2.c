#include <stdio.h>

void main(int argc, char** argv)
{
	int number;

	printf("Enter a number: ");
	scanf("%d", &number);

	if(number == 4)
	{
		printf("Success!\n");
	}
	else
	{
		printf("Fail\n");
	}
}
