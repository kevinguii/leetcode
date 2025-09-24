# Palindrome Linked List
def isPalindrome(head):
	# find middle
	fast = slow = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	prev = None
	curr = slow
	#reverse second half
	while curr:
		next_n = curr.next
		curr.next = prev
		prev = curr
		curr = next_n
	#checks
	l,r = head, prev
	while r:
		if l.val != r.val:
			return False
		l = l.next
		r = r.next
	return True

# Merge Two Sorted Lists
def mergeTwoLists(list1,list2):
	# create dummy
	# append the lower value between two lists until one is empty
	# append the other list and return
	curr = dummy = ListNode()
	while list1 or list2:
		if list1.val < list2.val:
			curr.next = list1
			list1 = list1.next
		else:
			curr.next = list2
			list2 = list2.next
		curr = curr.next
	if list1 or list2:
		curr.next = list1 if list1 else list2
	return dummy.next

# Min Stack
#O(n) initialization and O(1) getting min
class MinStack:
	def __init__(self):
		stack = []
	def push(self,val):
		if not self.stack:
			current_min = val
		else:
			current_min = min(self.stack[-1][1],val)
		self.stack.append((val,current_min))
	def pop(self):
		self.stack.pop()
	def top(self):
		return self.stack[-1][0]
	def getMin(self):
		return self.stack[-1][1]

# Valid Parentheses
# O(n) time and O(n) space
def isValid(s):
	closeToOpen = {"}":"{","]":"[",")":"("}
	stack = []
	for c in s:
		if c in closeToOpen:
			if stack and stack[-1] != closeToOpen[c]:
				return False
			stack.pop()
		else:
			stack.append(c)
	return False if stack else True