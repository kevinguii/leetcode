# 1382. Balance a Binary Search Tree
# https://leetcode.com/problems/balance-a-binary-search-tree/description/

# my thought: get all node values and store in an array, then create a new balanced BST
# O(n) time and space
def balanceBST(root):
	# get all values, inorder traversal
	arr = []
	stack = []
	while root or stack:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			arr.append(root.val)
			root = root.right

	# build BST recursively
	def buildBST(left,right):
		if left > right:
			return None
		mid = (left+right)//2
		node = TreeNode(arr[mid])
		node.left = buildBST(left,mid-1)
		node.right = buildBST(mid+1,right)
		return node
	return buildBST(0,len(arr)-1)
	
	n = len(arr)
	mid = n // 2
	root_new = TreeNode(arr[mid])
	q = deque()
	q.append((root_new,0,mid-1))
	q.append((root_new,mid+1,n-1))
	while q:
		node, left, right = q.popleft()
		if left <= right:
			mid = (left+right)//2
			child = TreeNode(arr[mid])
			if arr[mid] < node.val:
				node.left = child
			else:
				node.right = child
			q.append((child,left,mid-1))
			q.append((child,mid+1,right))
	return root_new