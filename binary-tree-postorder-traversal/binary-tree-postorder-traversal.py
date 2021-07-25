# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postfs(self,root):
        if not root:
            return
        self.postfs(root.left)
        self.postfs(root.right)
        self.path.append(root.val)

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        self.path = []
        self.postfs(root)
        return self.path
