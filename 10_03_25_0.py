# Search in a Binary Search Tree
# O(n) time and O(1) space
def searchBST(root,val):
	while root:
		if root.val == val:
			return root
		if val < root.val:
			root = root.left
		else:
			root = root.right
		
# Insert into a Binary Search Tree
# given root fo BST and a value to insert, return root node of BST after insertion
def insertIntoBST(root,val):
	if not root: return TreeNode(val)
	curr = root
	while True:
		if val < curr.val:
			if curr.left:
				curr = curr.left
			else:
				curr.left = TreeNode(val)
				break
		else:
			if curr.right:
				curr = curr.right
			else:
				curr.right = TreeNode(val)
				break
	return 

def insertIntoBST(root,val):
	if not root: return TreeNode(val)
	if  val < root.val: root.left = insertIntoBST(root.left,val)
	else: root.right = insertIntoBST(root.right,val)
	return root

# Convert Sorted Array into a BST (height-balanced)
# given nums, return BST height-balanced
# iterative: set root as the middle value then create a queue and append node, left, right, binary searc, get the middle
# add that hen do another two

# recursive
def sortedArrToBST(nums):
	if not nums: return None
	mid = len(nums)//2
	root = TreeNode(nums[mid])
	root.left = sortedArrToBST(nums[:mid])
	root.right = sortedArrToBST(nums[mid+1:])
	return root

# O(n) time and space
def sortedArrToBST(nums):
	n = len(nums)
	mid = n//2
	root = TreeNode(nums[mid])
	q = deque()
	q.append((root,0,mid-1))
	q.append((root,mid+1,n-1))
	while q:
		node, left, right = q.popleft()
		if left <= right:
			middle = (left+right)//2
			child = TreeNode(nums[middle])
			if nums[middle] < node.val:
				node.left = child
			else:
				node.right = child
			q.append((child,left,middle-1))
			q.append((child,middle+1,right))
	return root