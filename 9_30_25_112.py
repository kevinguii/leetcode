# 112. Path Sum
# https://leetcode.com/problems/path-sum/description/

# i know its DFS
# probably keep checking left from root
# sum has to end at a node with no children
# if a node reaches target sum and has children, stop looking
# intuition to solution: store the node and value in a tuple in the stack
# value will keep running sum as you append children
# check condition for True is if no children and equal to target
# otherwise add the right children first, with value including the new right value and same with left
def hasPathSum(root,targetSum):
	if not root: return False
	stack = [(root,root.val)]
	while stack:
		node, val = stack.pop()
		if not node.left and not node.right and val == targetSum:
			return True
		if node.right:
			stack.append((node.right,node.right.val+val))
		if node.left:
			stack.append((node.left,node.left.val+val))
	return False
