#include "lists.h"

/**
 * add_dnodeint - This adds new node at the beginning of dlistint_t list
 * @head: This a pointer to the head of dlistint_t list
 * @m: This is integer for new node to contain
 * Return: Null - If the function fails
 *         Otherwise, the address of the new node
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int m)
{
	dlistint_t *new;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);

	new->m = m;
	new->prev = NULL;
	new->next = *head;
	if (*head != NULL)
		(*head)->prev = new;
	*head = new;

	return (new);
}
