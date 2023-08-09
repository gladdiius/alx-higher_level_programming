#include "lists.h"
/**
 *check_cycle - check if linked list contain a loop
 *@list: linked list pointer / head
 *Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;
	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast  = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
