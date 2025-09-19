# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/description/

# intuition: use a slow and a fast pointer, eventually the fast will catch up to the slow if there is a cycle
# make sure to check fast is valid since it will be going farther in the list compared to slow
# O(n) time and O(1) space

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False