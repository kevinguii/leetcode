# 92. Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/description/

# left and right are 1-indexed
# my intuition: iterate, maybe for loop, to get to left, once you do, store prev
# iterate through that until you get to right, continuously doing next_node = curr.next, curr.next = prev, prev = current, current = next_node
# then when you get to the end, store the next value, and change pointing
# that last value should now be .next of the prv we stored before reversing and the first value in the loop .next should poitn to the value after the loop ends.

#pseudo code
# dummy = ListNode(0,head)
# prev, curr = dummy, head
# count = 1
# while count < left:
# keep it moving 
# count + 1
# store prev before loop starts and first element
# while count <= right:
# iterate through switching look
# make the switch, return head

# more optimized
def reverseBetween(head,left,right):
	if not head or left == right:
		return head
	dummy = ListNode(0,head)
	prev = dummy
	# iterate to item before start of 
	for _ in range(left-1):
		prev = prev.next
	start = prev.next
	then = start.next
	for _ in range(right-left):
		start.next = then.next
		then.next = prev.next
		prev.next = then
		then = start.next
	return dummy.next

def reverseBetween(head,left,right):
	dummy = ListNode(0,head)
	left_prev, curr = dummy, head
	# to get to the left pointer
	for i in range(1,left-1): # current node will stand at the first left node
		left_prev = curr
		curr = curr.next
	prev = None
	for i in range(right-left+1):
		next_pointer = curr.next
		curr.next = prev
		prev, current_node = current_node, next_pointer
	left_prev.next.next = current_node
	left_prev.next = prev
	return dummy.next
	
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next