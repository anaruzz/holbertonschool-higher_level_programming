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
f = f->next->next;
while (f->n != s->n)
{
s = s->next;
f = f->next->next;
}
if (s->n == f->n)
return (1);

return (0);
}
