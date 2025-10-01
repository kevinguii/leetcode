# find max and min of a binary tree

# breadth first search, use a queue, pop values
# min/max = float('inf') or float('-inf')
# deque()
# while q:
# val = q.popleft()
# min/max = min/max(min/max,val)
# if node.left: q.append(node.left), if node.right: q.append(node.right)
from collections import deque
# O(n) time, O(n) space for storing all nodes in the deque
def return_largest_node(root):
	q = deque([root])
	max_val = 0
	while q:
		curr_val = q.popleft()
		if curr_val.val > max_val:
			max_val = curr_val.val
		if curr_val.left:
			q.append(curr_val.left)
		if curr_val.right:
			q.append(curr_val.right)
	return max_val

def return_smallest_node(root):
	q = deque([root])
	min_node = float('inf')
	while q:
		curr_val = q.popleft()
		if curr_val.val < min_node:
			min_node = curr_val.val
		if curr_val.left:
			q.append(curr_val.left)
		if curr_val.right:
			q.append(curr_val.right)
	return min_node