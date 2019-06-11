#include <stdio.h>

static char password[] = "passw0rd";
int main(void)
{
	char buf[20];
	printf("Password: ");
	scanf("%s", buf);
	
	int match = strcmp(buf, password);
	if(match)
	{
		printf("Access denied.\n");
		return 1;
	}
	else
	{
		printf("Access granted.\n");
		return 0;
	}
	return 0;
}
