#include "lists.h"

/**
 * dlistint_len - This will return number of elements
 * @s: This is the head pointer
 * Return: The number of elements
 */

size_t dlistint_len(const dlistint_t *s)
{
	size_t count = 0;

	while (s != NULL)
	{
		s = s->next;
		count += 1;
	}

	return (count);
}
