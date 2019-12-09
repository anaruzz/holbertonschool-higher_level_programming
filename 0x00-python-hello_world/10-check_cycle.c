#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
* check_cycle - check for cycle in a linked list
* @list: the list
* Return: has cycle or not
*/
int check_cycle(listint_t *list)
{
listint_t *f = list;
listint_t *s = list;
if (list == NULL || list->next == NULL)
return (0);
while (f && f->next && f->next->next)
{
s = s->next;
if (s->n == f->n)
f = f->next->next;
return (1);
}
return (0);
}
