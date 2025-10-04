# 530. Minimum Absolute Difference in BST
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/
# min difference is always between consecutive nodes
# ascending order traversal will give us the best result (inorder)

# brute force: do BFS and store min value and do BFS to compare all parent children pairs, return min

# using inorder traversal, go all the way to the left then iterate in ascending order
# O(n) time, O(n) space
def getMinimumDifference(root):
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

# recursion
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev is not None:
                self.min_diff = min(self.min_diff, node.val - self.prev)
            self.prev = node.val
            inorder(node.right)

        inorder(root)
        return self.min_diff
