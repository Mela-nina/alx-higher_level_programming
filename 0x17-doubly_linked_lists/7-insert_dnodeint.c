#include "lists.h"

/**
 * insert_dnodeint_at_index - This inserts a node in a given index in
 * a doubly linked list
 * @l: This is the double pointer to the list
 * @idx: This is the index of the node to insert
 * @m: This is the data to insert
 * Return: address of the new node, or if it failed NULL
 */

dlistint_t *insert_dnodeint_at_index(dlistint_t **l, unsigned int idx, int m)
{
	unsigned int i;
	dlistint_t *new;
	dlistint_t *temp = *l;

	new = malloc(sizeof(dlistint_t));
	if (!new || !h)
		return (NULL);

	new->m = m;
	new->next = NULL;

	if (idx == 0)
		return (add_dnodeint(l, m));

	for (i = 0; temp && i < idx; i++)
	{
		if (i == idx - 1)
		{
			if (temp->next == NULL)
				return (add_dnodeint_end(l, m));
			new->next = temp->next;
			new->prev = temp;
			temp->next->prev = new;
			temp->next = new;
			return (new);
		}
		else
			temp = temp->next;
	}

	return (NULL);
}
