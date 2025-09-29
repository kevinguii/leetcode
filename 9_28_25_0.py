# Reverse First K Elemenets of a Queue Using a Stack
# create a stack to store the first k elements
# pop off the top of the stack one by one into the queue
# pop off remaining elements in the queue to get new order
# O(n) time, O(k) space for the number of elements
def reverse(k,q):
	stack = []
	for _ in range(k):
		stack.append(q.popleft())
	
	while stack:
		q.append(stack.pop())

	for _ in range(len(q)-k):
		q.append(q.popleft())
	return q

# Average of Levels in Binary Tree: average value of all nodes in a level
# BFS, Queue, start at the root, create a queue, iterate through all levels by appending to queue, checking for left and right, computing average value and popping
# q = queue()
# res = []
# q.append(root)
# while q:
# res.append(sum(q)/len(q))
# for i in range(len(q)):
# val = q.popleft()
# if node.right: q.append(node.right), if node.left: q.append(node.left)
# return res
# O(n) for n = number of nodes, O(k) space for k levels
from collections import deque
def avererageOfLevels(root):
	q = deque([root])
	res = []
	while q:
		level_sum = 0
		q_len = len(q)
		for _ in range(q_len):
			val = q.popleft()
			level_sum += val
			if val.left:
				q.append(val.left)
			if val.right:
				q.append(val.right)
		res.append(level_sum/q_len)
	return res

# Minimum Depth of Binary Tree
# use BFS, queue, same thing as average of levels except return level where no children at all
# if not root: return 0
# q = deque([root])
# level = 0
# while q:
# level +=1
# for _ in range(len(q)):
# node = q.popleft()
# if not node.left and not node.right:
# return level
# if node.left: q.append(node.left), if node.right: q.append(node.right)
# return level
def minDepth(root):
	if not root: return 0
	level = 0
	q = deque([root])
	while q:
		level +=1
		for _ in range(len(q)):
			node = q.popleft()
			if not node.left and not node.right:
				return level
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
	return level

# Max Depth of Binary Tree, find max depth binary tree
# use BFS
def maxDepth(root):
	if not root: return 0
	level = 0
	q = deque([root])
	while q:
		level +=1
		for _ in range(len(q)):
			node = q.popleft()
			if node.left:
				q.append(node.left)
			if node.right:
				q.append(node.right)
	return level

# recursively
def maxDepth(root):
	if not root: return 0
	return 1 + max(maxDepth(root.left),maxDepth(root.right))