#include "lists.h"
#include <stdlib.h>
/**
 * insert_node -  inserts a number into a sorted singly linked list.
 * @head: pointer to the first node.
 * @number: number to be inserted.
 * Return: the address of the new node, or NULL if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp = *head;
	listint_t *temp2 = malloc(sizeof(listint_t));

	if (!temp2)
		return (NULL);

	temp2->n = number;
	temp2->next = NULL;
	if (!(*head))
		*head = temp2;

	if (temp->n > number)
	{
		temp2->next = temp;
		*head = temp2;
	}

	else
	{
		temp2->n = number;
		temp2->next = NULL;
		while (temp->next && temp->next->n < number)
			temp = temp->next;
		temp2->next = temp->next;
		temp->next = temp2;
	}

	return (temp2);
}
