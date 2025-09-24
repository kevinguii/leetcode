# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/description/

# my intuition: store values in a set, iterate through, if in set, remove it, it set is empty by end of iteration, return True
# else return False

# other approach, find the middle of the linked list with the slow and fast pointers, then iterate beginning and end
# towards the middle to check values if they are the same up to the middle

# O(n) time and O(1) space
def isPalindrome(head):
	# find middle node
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	
	# reverse the second half
	prev = None
	curr = slow
	while curr:
		next_n = curr.next
		curr.next = prev
		prev = curr
		curr = next_n

	# compare the values up to the middle
	right = prev
	left = head
	while right:
		if left.val != right.val:
			return False
		left = left.next
		right = right.next
	return True