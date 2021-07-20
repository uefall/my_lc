# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isLeaf(self,root):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return True
        return False
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        sum = 0
        if root is None:
            return 0
        if self.isLeaf(root.left):
            sum += root.left.val
        else:
            sum += self.sumOfLeftLeaves(root.left)
        if root.right is not None:
            sum += self.sumOfLeftLeaves(root.right)
        return sum