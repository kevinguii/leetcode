# 653. Two Sum IV - Input is a BST
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/

# my initial intuition is to just do BFS and store values in a set, if the difference is in the set return True
from collections import deque

#O(n) time and space
def findTarget(root,k):
	values = set()
	q = deque([root])
	while q:
		node = q.popleft()
		diff = k - node.val
		if diff in values:
			return True
		values.add(node.val)
		if node.left: q.append(node.left)
		if node.right: q.append(node.right)
	return False