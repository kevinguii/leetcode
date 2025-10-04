# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# for regular binary tree
# continuously add to a dict until you get p and q, storing as child: parent

# iterate through ancestors and check
# or do that parent1 parent2 thing comparison and switch

# BST is easier
# find the bigger and smaller terms between p and q
# if the root value is greater than the largest term, then iterate left because p and q are both in that subtree
# if the root value is less than the small term, iterate to the right
# otherwise its the LCA and return the root 
# O(H) time for height of tree, O(1) space
def lowestCommonAncestor(root,p,q):
	small, large = sorted([p.val,q.val])
	while root:
		if root.val > large:
			root = root.left
		elif root.val < small:
			root = root.right
		else:
			return root