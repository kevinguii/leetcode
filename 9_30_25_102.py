# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# intuition
"""
store a res [] and a curr []
level by level = BFS, queue
create a queue start with root in it
res = []
q = deque([root])
while q:
	temp = []
	for _ in range(len(q)):
		node = q.popleft()
		temp.append(node)
		if node.left:
			q.append(node.left)
		if node.right:
			q.append(node.right)
	res.append(temp)
return res
"""
from collections import deque
# O(n) time and O(n) space
def levelOrder(root):
	if not root:
		return []
	res = []
	q = deque([root])
	while q:
		temp = []
		for _ in range(len(q)):
			node = q.popleft()
			temp.append(node.val)
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
		res.append(temp)
	return res