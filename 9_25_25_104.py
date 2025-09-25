# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# recursive, faster run time, no overhead
# O(n) time nad O(h) space, with h being height of the tree, no queue operations
def maxDepth(root):
	if not root:
		return 0
	return 1+max(maxDepth(root.left),maxDepth(root.right))

# same intuition, except you keep going down until your queue is empty and no children left to look through
# O(n) time, O(m) space, where w is max width of tree
from collections import deque
def maxDepth(root):
	if not root:
		return 0
	level = 0
	q = deque([root])
	while q:
		level+=1
		for _ in range(len(q)):
			node = q.popleft()
			if node.left: q.append(node.left)
			if node.right: q.append(node.right)
	return level

