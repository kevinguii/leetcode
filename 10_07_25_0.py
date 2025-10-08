# traversals
# inorder: left, root, right
def inorder(root):
	if not root: return []
	return inorder(root.left) + [root.val] + inorder(root.right)

# preorder: root, left, right
def preorder(root):
	if not root: return []
	return [root.val] + preorder(root.left) + preorder(root.right)

# postorder: left, right, root
def postorder(root):
	if not root: return []
	return postorder(root.left) + postorder(root.right) + [root.val]

# balance tree in BST
# O(n) time and space
# get numbers into a sorted array, then recreate a balanced tree
def balanceTree(root):
	def inorder(root):
		if not root: return []
		return inorder(root.left) + [root.val] + inorder(root.right)
	
	nums = inorder(root)
	# create a balanced tree (iteratively and recursively)
	# recursively
	def createBalanced(left,right):
		if left > right: return None
		mid = (left+right)//2
		node = TreeNode(nums[mid])
		node.left = createBalanced(left,mid-1)
		node.right = createBalanced(mid+1, right)
		return node
	return createBalanced(0,len(nums)-1)

	# iteratively
	n = len(nums)
	mid = n //2
	root = TreeNode(nums[mid])
	q = deque()
	q.append((root,0,mid-1))
	q.append((root,mid+1,n-1))
	while q:
		node, l, r = q.popleft()
		if l<=r:
			mid = (l+r)//2
			child = TreeNode(nums[mid])
			if nums[mid] < node.val:
				node.left = child
			else:
				node.right = child
			q.append((child,l,mid-1))
			q.append((child,mid+1,r))
	return root

# delete node in BST
# O(n) time and space
def deleteNode(root,key):
	if not root: return None
	if key > root.val:
		root.right = deleteNode(root.right,key)
	elif key < root.val:
		root.left = deleteNode(root.left,key)
	else:
		# no children
		if not root.left and not root.right:
			return None
		# 1 child left or right
		if not root.right: return root.left
		if not root.left: return root.right

		# 2 children, find successor
		successor = root.right
		while successor.left:
			successor = successor.left
		root.val = successor.val
		root.right = deleteNode(root.right,successor.val)
	return root

# kth smallest element in BST
# do inorder traversal and store in a stack, instead of creating the whole thing, just pop off and subtract one from k index
# O(n) time and space
def kthSmallest(root,k):
	stack = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			node = stack.pop()
			k-=1
			if k == 0: return node.val
	return None
