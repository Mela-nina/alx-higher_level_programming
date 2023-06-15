#include "lists.h"

/**
 * free_dlistint - This frees a doubly linked list
 * @head: This is the head pointer
 * Return: Nothing
 */

void free_dlistint(dlistint_t *head)
{
	if (head == NULL)/*An empty head return nothing*/
		return;

	while (head && head->next)
	{
		head = head->next;
		free(head->prev);
	}
	free(head);
}
