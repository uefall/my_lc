# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def prefs(self,root):
        if not root:
            return
        self.path.append(root.val)
        self.prefs(root.left)
        self.prefs(root.right)
        
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.path = []
        self.prefs(root)
        return self.path
        