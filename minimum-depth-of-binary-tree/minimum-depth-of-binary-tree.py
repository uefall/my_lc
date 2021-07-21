# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        lr_min = 999999
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        else:
            if root.left:
                lr_min = min(self.minDepth(root.left)+1,lr_min)
            if root.right:
                lr_min = min(self.minDepth(root.right)+1,lr_min)
            return lr_min
        