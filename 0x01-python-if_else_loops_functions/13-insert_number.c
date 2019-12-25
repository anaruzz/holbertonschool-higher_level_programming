#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node- insert node in a sorted list
 * @head: head of node
 * @number: value of node to be inserted
 * Return: node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new, *h = *head;

new = malloc(sizeof(listint_t));
if (!new)
return (NULL);

if (!*head)
{
(*head)->n = number;
(*head)->next = NULL;
}
new->n = number;
while(h)
{
h = h->next;
if ((h->next)->n > number)
break;
}

if (h->next != NULL)
{
new->next = h->next;
h->next = new;
}
else
{
  h->next = new;
  new->next = NULL;
}
h = new;
return (h);
}
