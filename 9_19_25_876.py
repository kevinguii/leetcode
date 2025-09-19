# 876. Middle of the Linked List
# http://leetcode.com/problems/middle-of-the-linked-list/description/

# my intuition: use slow and fast pointers?
# one slow that goes .next, the other that goes .next.next, need to make sure it's valid tho, so we need a next and a next.next before running that
# fast is for even list because .next.next will make it null, fast.next check is for odd length list where the one after it is null

# O(n) time and O(1) space
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow