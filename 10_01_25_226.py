# 226. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/

# intuition: DFS, recursive down to when a node has at least one child, then node.left = node.right and vice versa, then recurse back up
def invertTreeRecursive(root):
	if root:
		root.left,root.right = invertTreeRecursive(root.right), invertTreeRecursive(root.left)
		return root
# you can also do it with a stack
def invertTree(root):
	stack = [root]
	while stack:
		node = stack.pop()
		if node:
			node.left,node.right = node.right, node.left
			stack.extend([node.right,node.left])
	return root
