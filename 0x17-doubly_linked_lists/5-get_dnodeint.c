#include "lists.h"

/**
 * get_dnodeint_at_index - This locates a node in dlistint_t list
 * @head: This is the ead of the dlistint_t list
 * @index: This is the node to locate
 * Return: NULL - If the node does not exist
 *         Otherwise, the address of the located node
 */

dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	for (; index != 0; index--)
	{
		if (head == NULL)
			return (NULL);
		head = head->next;
	}

	return (head);
}
