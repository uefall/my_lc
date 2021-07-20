# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.dfs_height(root) != -1
        
    def dfs_height(self, root):
        if not root: return 0
        
        # L
        left_height = self.dfs_height(root.left)
        if left_height == -1:
            return -1
        
        # R
        right_height = self.dfs_height(root.right)
        if right_height == -1:
            return -1
        
        # unb in this node
        if abs(left_height - right_height) > 1:
            return -1
        
        # b in this node
        # normal
        h = max(left_height, right_height) + 1
        return h
