# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/

# DFS, use a stack
# iterate through both trees, starting with root node
# while stack, do checks, append rights and then lefts after
# therefore, you can pop the left off first and check left trees before right
# conditions are: if both are empty, you can keep going, but if at least one is a #, if other is none return False
# or if values don't match return False, otherwise append to stack and LIFO check

# O(n) time and O(n) space
def isSameTree(p,q):
	stack = [(p,q)]

	while stack:
		node1, node2 = stack.pop()
		# both don't exist
		if not node1 and not node2:
			continue
		# if one doesn't exist or values not equal
		elif None in [node1,node2] or node1.val != node2.val:
			return False
		stack.append((node1.right,node2.right))
		stack.append((node1.left,node2.left))
	return True

print(isSameTree(1,2))