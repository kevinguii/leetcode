# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/

# this is bfs for sure
# search all nodes at the same level and compute average there
# use a queue as well because its FIFO, once we get all values on the level, we calculate sum and iterate to next level
# O(n) time for traversal, O(n) space to store in the queue
from collections import deque
def averageOfLevels(root):
	q = deque([root])
	res = []
	while q:
		level_sum = 0
		level_len = len(q)
		for i in range(level_len):
			node = q.popleft()
			level_sum+=node.val
			if node.left: q.append(node.right)
			if node.right: q.append(node.left)
		res.append(level_sum/level_len)
	return res
