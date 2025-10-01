from collections import deque
# Max Min Val of Tree
def maxValTree(root):
	q = deque([root])
	max_val = 0
	while q:
		node = q.popleft()
		if node.val > max_val:
			max_val = node.val
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	return max_val

# Binary Tree Level Order Traversal
# O(n) time and space
def traversal(root):
	if not root: return []
	q = deque([root])
	res = []
	while q:
		temp = []
		for _ in range(len(q)):
			node = q.popleft()
			temp.append(node.val)
			if node.left: q.append(node.left)
			if node.right: q.append(node.right)
		res.append(temp)
	return res

# Same Tree
# O(n) time and space
def sameTree(p,q):
	stack = [(p,q)]
	while stack:
		node1, node2 = stack.pop()
		if not node1 and not node2:
			continue
		elif None in [node1,node2] or node1.val != node2.val:
			return False
		stack.append((node1.right,node2.right))
		stack.append((node1.left,node2.left))
	return True

# Path Sum
# O(n) time and space
def pathSum(root,targetSum):
	if not root:
		return False
	stack = [(root,root.val)]
	while stack:
		node,val = stack.pop()
		if not node.left and not node.right and val == targetSum:
			return True
		if node.right: stack.append((node.right,node.right.val+val))
		if node.left: stack.append((node.left,node.left.val+val))
	return False