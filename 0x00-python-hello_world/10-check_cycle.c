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

while (f && s && f->next)
{
s = s->next;
f = (f->next)->next;
if (s == f)
return (1);
}
return (0);
}
