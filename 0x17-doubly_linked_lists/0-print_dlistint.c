#include "lists.h"
#include <stdio.h>

/**
 * print_dlistint - This prints all elements of dlistint_t list
 * @s: This is the  pointer to the start of linked list
 * Return: The number of nodes
 */
size_t print_dlistint(const dlistint_t *s)
{
	size_t j;

	for (j = 0; s != NULL; j++)
	{
		printf("%d\n", s->n);
		s = s->next;
	}
	return (j);
}
