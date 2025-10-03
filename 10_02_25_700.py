# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# O(n) time, O(1) space
def searchBST(root,val):
	while root:
		if root.val == val:
			return root
		elif root.val > val:
			root = root.left
		elif root.val < val:
			root = root.right
	return None