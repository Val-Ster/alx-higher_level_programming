#include "lists.h"
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: pointer to the head of the linked list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head;
	listint_t *fast_ptr = *head;
	listint_t *second_half = NULL;
	listint_t *prev_of_slow_ptr = *head;
	listint_t *mid_node = NULL;
	int is_palindrome = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		prev_of_slow_ptr = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	if (fast_ptr != NULL)
	{
		mid_node = slow_ptr;
		slow_ptr = slow_ptr->next;
	}
	second_half = slow_ptr;
	prev_of_slow_ptr->next = NULL;
	reverse_list(&second_half);
	is_palindrome = compare_lists(*head, second_half);
	reverse_list(&second_half);
	if (mid_node != NULL)
	{
		prev_of_slow_ptr->next = mid_node;
		mid_node->next = second_half;
	}
	else
	{
		prev_of_slow_ptr->next = second_half;
	}
	return (is_palindrome);
}
/**
 * reverse_list - reverses a linked list
 * @head_ref: pointer to the head of the linked list
 */
void reverse_list(listint_t **head_ref)
{
	listint_t *prev = NULL;
	listint_t *current = *head_ref;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head_ref = prev;
}
/**
 * compare_lists - compares two linked lists for equality
 * @head1: pointer to the head of the first linked list
 * @head2: pointer to the head of the second linked list
 * Return: 1 if the lists are equal, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 != NULL && head2 != NULL)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}
	return (head1 == NULL && head2 == NULL);
}
