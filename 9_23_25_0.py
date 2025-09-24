# Middle of Linked List
def middleNode(head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow

# Linked List Cycle
def hasCycle(head):
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if fast == slow:
			return True
	return False

# Reverse Linked List
def reverseList(head):
	prev = None
	curr = head
	while curr:
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	head = prev
	return head
# Remove LL Elements
def removeElements(head,val):
	dummy = ListNode(0,head)
	prev, curr = dummy, head
	while curr:
		if curr.val == val:
			prev.next = curr.next
		else:
			prev = curr
		curr = curr.next
	return dummy.next

# Remove LL II
def reverseBetween(head,left,right):
	dummy = ListNode(0,head)
	left_prev, curr = dummy, head

	for _ in range(1,left-1):
		left_prev = left_prev.next
		curr = curr.next
	
	prev = None
	for _ in range(right-left+1):
		next_node = curr.next
		curr.next = prev
		prev = curr
		curr = next_node
	
	left_prev.next.next = curr
	left_prev.next = prev
	return dummy.next
