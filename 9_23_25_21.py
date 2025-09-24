# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/

# intuition: given list 1 and list 2, use a dummy head to store, then check 
# while loops for both lists until they reach None and then append the other one

class ListNode:
	def __init__(self,val=0,next=None):
		self.val = val 
		self.next = next

# O(m+n) time, length of both lists, O(1) space
def mergeTwoLists(list1,list2):
	cur = dummy = ListNode()
	while list1 and list2:
		if list1.val < list2.val:
			dummy.next = list1
			list1 = list1.next
		else:
			dummy.next = list2
			list2 = list2.next
		dummy = dummy.next
	if list1 or list2:
		dummy.next = list1 if list1 else list2
	return cur.next