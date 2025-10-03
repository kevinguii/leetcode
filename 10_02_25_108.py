# 108. Convert Sorted Array to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# intuition: using binary search essentially to add the nodes in
# start with middle node, break up into left and right sides, pop from a queue using BFS, add to tree, append children + positioning
from collections import deque
class TreeNode:
	def __init__(self,val,left = None,right = None):
		self.val = val
		self.left = left
		self.right = right

# O(n) time and space
def sortedArrayToBST(nums):
	if not nums: return None
	mid = len(nums)//2
	root = TreeNode(val = nums[mid])
	l, r = 0, len(nums)
	q = deque()
	q.append((root,l, mid-1))
	q.append((root,mid+1,r))
	while q:
		node, left, right = q.popleft()
		if left <= right:
			mid = (left+right)//2
			child = TreeNode(nums[mid])
			if nums[mid] < node.val:
				node.left = child
			else:
				node.right = child
			q.append((child,left,mid-1))
			q.append((child,mid+1,right))
	return root

## recursive
def sortedArrToBST(nums):
	if not nums:
		return None
	mid = len(nums)//2
	root = TreeNode(nums[mid])
	root.left = sortedArrToBST(nums[:mid])
	root.right = sortedArrToBST(nums[mid+1:])
	return root
	
