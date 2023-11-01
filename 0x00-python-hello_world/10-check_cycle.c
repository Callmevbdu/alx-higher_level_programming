#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a function that checks if the linked list is cyclical
 * @list: a pointer to the list to be checked
 * Return: If cyclical(1), 0 otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
			return (1);
	}

	return (0);
}
