# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None and root.val == targetSum:
            return True
        re = False
        if root.left is not None:
            l_flg = self.hasPathSum(root.left, targetSum-root.val)
            re = re or l_flg
        if root.right is not None:
            r_flg = self.hasPathSum(root.right, targetSum-root.val)
            re = re or r_flg
        return re