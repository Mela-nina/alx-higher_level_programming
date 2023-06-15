#include "lists.h"

/**
 * sum_dlistint - This is the sums all of the data of a dlistint_t linked list
 * @head: This is the pointer to the beginning of the linked list
 * Return: sum of all data, or if the list is empty 0
 */

int sum_dlistint(dlistint_t *head)
{
	int sum = 0;

	while (head != NULL)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}
