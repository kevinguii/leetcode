# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# my thoughts: use BFS, keep track of level, if all nodes in the queue have left and right, append, else if both are null, return level
from collections import deque
# O(n) time and space
def minDepth(root):
	if not root:
		return 0
	q = deque([root])
	level = 1
	while q:
		for _ in range(len(q)):
			node = q.popleft()

			if not node.left and not node.right:
				return level
			
			if node.left: q.append(node.left)
			if node.right: q.append(node.right)
		level +=1
	return level