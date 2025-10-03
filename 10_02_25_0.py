# diameter of a binary tree
def diameterBinaryTree(self,root):
	self.diameter = 0
	def depth(root):
		if not root: return 0
		left = depth(root.left)
		right = depth(root.right)
		self.diameter = max(self.diameter,left+right)
		return 1 + max(left,right)
	depth(root)
	return self.diameter

# invert binary tree
def invertTree(root):
	stack = [root]
	while stack:
		node = stack.pop()
		if node:
			node.left, node.right = node.right, node.left
			stack.extend([node.right,node.left])
	return root

# recursive
def invertTree(root):
	if root:
		root.left, root.right = invertTree(root.right), invertTree(root.left)
		return root

# lowest common ancestor
# using stack
def LCA(root,p,q):
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
	
	"""
	parent1, parent2 = p,q
	while parent1!=parent2:
		parent1 = parent[parent1] if parent1 else q
		parent2 = parent[parent2] if parent2 else p
	return parent1
	"""

# recursion
def LCA(root,p,q):
	if not root or root.val == p or root.val == q:
		return root
	left = LCA(root.left,p,q)
	right = LCA(root.right,p,q)
	if left and right:
		return root
	if left: return left
	if right: return right