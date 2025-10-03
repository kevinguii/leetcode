# 701. Insert into a Binary Search Tree
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
class TreeNode:
	def __init__(self,val,left,right):
		self.val = val
		self.left = left
		self.right = right

# recursion
def insertIntoBSTR(root,val):
	if not root: return TreeNode(val)
	if root.val > val:
		root.left = insertIntoBSTR(root.left,val)
	else:
		root.right = insertIntoBSTR(root.right,val)
	return root

# O(n) time and O(1) space
# O(logn) time if a balanced BST
def insertIntoBST(root,val):
	if not root:
		return TreeNode(val)
	
	current = root
	while True:
		if val < current.val:
			if current.left:
				current = current.left
			else:
				current.left = TreeNode(val)
				break
		else:
			if current.right:
				current = current.right
			else:
				current.right = TreeNode(val)
				break
	return root