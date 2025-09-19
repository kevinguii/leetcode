# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/description/

# my intuition: as you iterate through the linked list, starting at the beginning, set next to null, but store the node, then for next one, store what that has as next
# then change it to first node, etc, etc until you reach the end, if next is null, that is the head

# O(n) time and O(1) space
def reverseList(head):
	if not head.next:
		return head
	prev = None
	current = head
	while current:
		next_node = current.next
		current.next = prev
		prev = current
		current = next_node
	head = prev
	return head