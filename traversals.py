# inorder: left, root, right
# recursive
def inorder(root):
	if not root: return []
	return inorder(root.left) + [root.val] + inorder(root.right)

# want nodes in a sorted order
def inorder(root):
	res = []
	stack = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			res.append(root.val)
			root = root.right
	return res

######################################################################
# preorder: root, left, right
# recursive
def preorder(root):
	if not root: return []
	return [root.val] + preorder(root.left) + preorder(root.right)

# need to copy or serialize a tree (convert to a string)
def preorder(root):
	if not root: return []
	res = []
	stack = [root]
	while stack:
		node = stack.pop()
		res.append(node.val)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left) # processes left node first

######################################################################
# postorder: left, right, root
# recursive
def postorder(root):
	if not root: return []
	return postorder(root.left) + postorder(root.right) + [root.val]

# need to delete/free a tree (child before parent), for evaluating expression trees
# process child before parent
def postorder(root):
	if not root: return []
	res = []
	stack = [root]
	while stack:
		node = stack.pop()
		stack.append(node.val)
		if node.left: stack.append(node.left)
		if node.right: stack.append(node.right)
	return res[::-1]