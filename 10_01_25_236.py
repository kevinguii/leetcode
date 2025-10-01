# 236. Lowest Common Ancestor of a Binary Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# if both children nodes are p and q, then LCA is just the parent
# if one is parent and other is child, LCA is parent

# iteartive approach: keep track of node and its parent until we find p and q, store them in a dict
# create a set to store all parents of p all the way up to the root
# then another loop for q to check if its parent is in p's parents, otherwise go up another level and check that parent
# BFS
# O(n) time, O(n) space with set, O(1) space for second half with pointers
def lowestCommonAncestor(root,p,q):
	stack = [root]
	parent = {root: None}
	while stack:
		node = stack.pop()
		if node.left:
			stack.append(node.left)
			parent[node.left] = node
		if node.right:
			stack.append(node.right)
			parent[node.right] = node
		if p in parent and q in parent:
			break
	
	ancestors = set()
	while p:
		ancestors.add(p)
		p = parent[p]
	
	while q:
		if q in ancestors:
			return q
		q = parent[q]

	# second half constant space approach, both will traverse the same distance and reach the same node in two iterations max
	# pointer1, pointer2 = p,q
	# while pointer1 != pointer2:
	# 	pointer1 = parent[pointer1] if pointer1 else q
	# 	pointer2 = parent[pointer2] if pointer2 else p
	# return pointer1
	
# using recurison
# check through entire thing, if root is None or equal to p and q return the value
# run recursion on left and right sides
# if left side and right side are both none, you found the LCA and return the root
# if only one side: then either both p and q are under that subtree or its bubbling up the value from lower so return left or right
# O(n) time and O(h) space for height of tree
def lowestCommonAncestor(self, root, p, q):
    if root == None or root == p or root == q:
        return root

    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left != None and right != None:
        return root

    if left != None:
        return left

    return right
