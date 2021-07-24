# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, path, t):
        if not root.left and not root.right and sum(path) == t:
            self.re.append(path.copy())
            path = []
        if root.left:
            path.append(root.left.val)
            self.dfs(root.left,path,t)
            path.pop()
        if root.right:
            path.append(root.right.val)
            self.dfs(root.right,path,t)
            path.pop()

    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        self.re = []
        if not root:
            return self.re
        self.dfs(root,[root.val],targetSum)
        return self.re
