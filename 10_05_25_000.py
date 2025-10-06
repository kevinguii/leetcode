# Two Sum - Input is BST
def findTarget(root,k):
	q = deque([root])
	values = set()
	while q:
		node = q.popleft()
		if (k - node.val) in values:
			return True
		values.add(node.val)
		if node.right: q.append(node.right)
		if node.left: q.append(node.left)
	return False

# LCA of BST
def LCA(root,p,q):
	small, large = sorted([p.val,q.val])
	while root:
		if root.val > large:
			root = root.left
		elif root.val < small:
			root = root.right
		else:
			return root

# 530. Minimum Absolute Difference in BST
# in order traversal
# keep track of a stack and the root
"""
while stack and root:
if root:
go left and append to stack
else:
pop off lsat stack val and assign as root
do your calculation, try to go right
"""
def minAbsDiff(root):
	min_diff = float('inf')
	prev_val = float('-inf')
	stack = []
	while root or stack:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			min_diff = min(min_diff,root.val-prev_val)
			prev_val = root.val
			root = root.right
	return min_diff

# recursive
def minAbsDiff(self,root):
	self.min_diff = float('inf')
	self.prev = None

	def inorder(node):
		if not node: return
		inorder(node.left)
		if self.prev is not None:
			self.min_diff = min(self.min_diff,node.val-self.prev)
		self.prev = node.val
		inorder(node.right)

	inorder(root)
	return self.min_diff

# Search in a Binary Search Tree 
# O(n) time and O(1) space
def searchBST(root,val):
	while root:
		if root.val > val:
			root = root.left
		elif root.val < val:
			root = root.right
		else:
			return root
	return None

# Insert into a Binary Search Tree
# keep track of root, and current_node, start at current node and go down the tree, if no left child and smaller, insert, if no right child an dlarger insert
# O(n) time and O(1) space
def insertIntoBST(root,val):
	current_node = root
	while current_node:
		if current_node.val < val:
			if current_node.right:
				current_node = current_node.right
			else:
				current_node.right = TreeNode(val)
				break
		elif current_node.val > val:
			if current_node.left:
				current_node = current_node.left
			else:
				current_node.left = TreeNode(val)
				break
	return root
def insertIntoBST(root,val):
	if not root:
		return TreeNode(val)
	if root.val > val:
		root.left = insertIntoBST(root.left,val)
	else:
		root.right = insertIntoBST(root.right,val)

# Convert Sorted Array into a BST (height-balanced)
# iterative approach
def sortedArrToBST(nums):
	n = len(nums)
	mid = n // 2
	root = TreeNode(nums[mid])
	q = deque()
	q.append((root,0,mid-1))
	q.append(root,mid+1,n-1)
	while q:
		node, left, right = q.popleft()
		if left <= right:
			middle = (left+right)//2
			if nums[middle] < node.val:
				node.left = TreeNode(nums[middle])
			else:
				node.right = TreeNode(nums[middle])
			q.append((node,left,mid-1))
			q.append((node,mid+1,right))
	return root

# recursive
def sortedArrToBST(nums):
	if not nums: return None
	n = len(nums)
	mid = n // 2
	root = TreeNode(nums[mid])
	root.left = sortedArrToBST(nums[:mid])
	root.right = sortedArrToBST(nums[mid+1:])
	return root

# diameter of a binary tree 
# recursion
def diameterBinaryTree(self,root):
	self.diameter = 0
	def depth(node):
		if not node: return 0
		left_depth = depth(node.left)
		right_depth = depth(node.right)
		self.diameter = max(self.diameter,left_depth+right_depth)
		return 1 + max(left_depth,right_depth)
	depth(root)
	return self.diameter

# invert binary tree
# bfs
def invertTree(root):
	if not root: return None
	q = deque([root])
	while q:
		node = q.popleft()
		node.left, node.right = node.right, node.left
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	return root

# dfs
def invertTree(root):
	if not root: return None
	stack = [root]
	while stack:
		node = stack.pop()
		node.left, node.right = node.right, node.left
		stack.extend([node.right,node.left])
	return root

# recursive DFS
def invertTree(root):
	if not root: return None
	root.left, root.right = invertTree(root.right), invertTree(root.left)
	return root

# lowest common ancestor
def lowestCommonAncestor(root,p,q_val):
	parent = {root: None}
	q = deque([root])
	while p not in parent and q not in parent:
		node = q.popleft()
		if node.left:
			parent[node.left] = node
			q.append(node.left)
		if node.right:
			parent[node.right] = node
			q.append(node.right)
	ancestors = set()
	while p:
		ancestors.add(parent[p])
		p = parent[p]
	while q_val not in ancestors:
		q_val = parent[q_val]
	return q

# recursive
def lowestCommonAncestor(root,p,q):
	if not root or root.val == p or root.val == q:
		return root
	left = lowestCommonAncestor(root.left,p,q)
	right = lowestCommonAncestor(root.right,p,q)
	if left and right: return root
	if left: return left
	return right

# Max Min Val of Tree
# bfs min max
def minValTree(root):
	q = deque([root])
	min_val = float('inf')
	while q:
		node = q.popleft()
		min_val = min(min_val,node.val)
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	return min_val
def MaxValTree(root):
	q = deque([root])
	max_val = float('-inf')
	while q:
		node = q.popleft()
		max_val = max(max_val,node.val)
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	return max_val
# dfs min max
def minValTree(root):
	stack = [root]
	min_val = float('inf')
	while stack:
		node = stack.pop()
		min_val = min(min_val,node.val)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)
	return min_val
def MaxValTree(root):
	stack = [root]
	max_val = float('-inf')
	while stack:
		node = stack.pop()
		max_val = max(max_val,node.val)
		if node.right: stack.append(node.right)
		if node.left: stack.append(node.left)
	return max_val

# Binary Tree Level Order Traversal
def binaryTraversal(root):
	res = []
	q = deque([root])
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
def sameTree(p,q):
	q = deque([(p,q)])
	while q:
		node1, node2 = q.popleft()
		if not node1 and not node2:
			continue
		elif not node1 or not node2 or node1.val != node2.val:
			return False
		q.append((node1.left,node2.left))
		q.append((node1.right,node2.right))
	return True

def sameTree(p,q):
	q = [(p,q)]
	while q:
		node1, node2 = q.pop()
		if not node1 and not node2:
			continue
		elif not node1 or not node2 or node1.val != node2.val:
			return False
		q.append((node1.right,node2.right))
		q.append((node1.left,node2.left))
	return True

# Path Sum
# O(n) time and O(n) space
def hasPathSum(root,targetSum):
	if not root: return False
	stack = [(root,root.val)]
	while stack:
		node, curr_sum = stack.pop()
		if not node.left and not node.right and curr_sum == targetSum:
			return True
		if node.right: stack.append((node.right,curr_sum+node.right.val))
		if node.left: stack.append((node.left,curr_sum+node.left.val))
	return False