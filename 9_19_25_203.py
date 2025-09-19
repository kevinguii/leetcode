# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/description/

# my intuition: when you want to remove a value, you need to connect the two around it, so you probably still need prev curr and next_node
# check the value for current and if its equal to value, prev.next = next_node
# however, what if the value is the first one?
# prev starts as None and curr = head and if curr.val = val and prev = None, then curr.next = head
# the end? it will still work as long as we check in the while loop for current
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# optimized, use a dummy node to check instead so you don't have to check if prev = none
# both O(n) time, O(1 space)
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

# first try, kinda slow but it works

def removeElements(head, val: int):
	prev, curr = None, head
	while curr:
		next_node = curr.next
		if curr.val == val:
			if prev is None:
				head = next_node
				curr = next_node
			else:
				prev.next = next_node
				curr = next_node
		else:
			prev = curr
			curr = next_node
	return head