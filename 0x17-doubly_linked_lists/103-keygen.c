#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * main - This generates a key depending on a username for crackme5
 * @argv: This arguments passed to main
 * @argc: This is the number of arguments passed
 * Return: On success 0, on error 1
 */

int main(int argc, char *argv[])
{
	unsigned int i, c;
	size_t len, add;
	char *k = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";
	char q[7] = "      ";

	if (argc != 2)
	{
		printf("Correct usage: ./keygen5 username\n");
		return (1);
	}
	len = strlen(argv[1]);
	q[0] = k[(len ^ 59) & 63];
	for (i = 0, add = 0; i < len; i++)
		add += argv[1][i];
	q[1] = k[(add ^ 79) & 63];
	for (i = 0, c = 1; i < len; i++)
		c *= argv[1][i];
	q[2] = k[(c ^ 85) & 63];
	for (c = argv[1][0], i = 0; i < len; i++)
		if ((char)c <= argv[1][i])
			c = argv[1][i];
	srand(c ^ 14);
	q[3] = k[rand() & 63];
	for (c = 0, i = 0; i < len; i++)
		c += argv[1][i] * argv[1][i];
	q[4] = k[(c ^ 239) & 63];
	for (c = 0, i = 0; (char)i < argv[1][0]; i++)
		c = rand();
	q[5] = k[(c ^ 229) & 63];
	printf("%s\n", q);
	return (0);
}
