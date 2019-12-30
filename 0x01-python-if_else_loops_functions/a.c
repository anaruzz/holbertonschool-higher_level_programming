#include <stdlib.h>
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

  new->n = number ;

  if (*head == NULL)
  {
  new->next = NULL;
  *head = new;
  return (*head);
  }

  if (number < h->n)
  {
    new->next = h->next;
    *head = new;
    return(new);
  }
  while (h)
  {
    if (number > (h->next)->n)
    h = h->next;
    else
    break;
  }
  if (h->next == NULL && number > h->n)
  {
    h->next = new;
    new->next = NULL;
    h = new;
    return (h);
  }
  if (h->next != NULL)
  {
    new->next = h->next;
    h->next = new;
    h = new;
    return (h);
  }
return (NULL);
}
