# 543. Diameter of a Binary Tree
# https://leetcode.com/problems/diameter-of-binary-tree/description/

# isn't this just longest path left and right of root if they exist? no
# intuition: the length of a binary tree is sum of left and right children
# iterate that same process through all nodes, and keep track of the max
# using recursion is more efficient and at each level you add 1 to the value, stopping if it is equal to none

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        self.diameter = 0
        def depth(root):
            if not root: return 0

            left_tree = depth(root.left)
            right_tree = depth(root.right)

            self.diameter = max(self.diameter,left_tree + right_tree)
            return 1 + max(left_tree,right_tree)
        depth(root)
        return self.diameter