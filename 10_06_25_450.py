# 450. Delete Node in a BST
# https://leetcode.com/problems/delete-node-in-a-bst/description/

# first you can do the same as balancing and just delete the node and rebalance, but that probably doesn't work
# next idea, get everyone's parents up until the key + the key's kids, if the key is not in our dict, return the root
# otherwise, you need to check 3 cases: the deleted node has no children, 1, or 2
# 2 children, find the successor (smallest node in the right subtree)

# O(n) time, O(1) space
def deleteNode(root,key):
	if not root:
		return None
	
	if key < root.val:
		root.left = deleteNode(root.left,key)
	elif key > root.val:
		root.right = deleteNode(root.right,key)
	else: # node to delete is found
		# case 1: no children
		if not root.left and not root.right:
			return None
		
		# case 2: 1 child
		if not root.right:
			return root.left
		if not root.left:
			return root.right
		
		# case 3: 2 children, find successor
		successor = root.right
		while successor.left:
			successor = successor.left
		root.val = successor.val
		root.right = deleteNode(root.right,successor.val)
	return root