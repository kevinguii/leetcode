# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

# even simpler, instead of storing in an array, just pop off and subtract one from the k index
# O(n) time, O(n) space
def kthSmallest(root,k):
	stack = []
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			k-=1
			if k == 0: return root.val
			root = root.right

# can do in order then index
# O(n) time and O(n) space
def kthSmallest(root,k):
	nums = []
	stack = []
	current = root
	while current or stack:
		if current:
			stack.append(current)
			current = current.left
		else:
			current = stack.pop()
			nums.append(current.val)
			current = current.right
	
	return nums[k-1]