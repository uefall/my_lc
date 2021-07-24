# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def update_path(self,root,cur_path):
        if not root:
            return
        # print('root',root.val)
        if root.left is None and root.right is None:
            # print('left,update')
            self.paths.append(cur_path)
        if root.left is not None:
            cur_path_L = cur_path+'->{}'.format(root.left.val)
            # print('L',root.left.val,cur_path_L)
            self.update_path(root.left,cur_path_L)
        if root.right is not None:
            cur_path_R = cur_path + '->{}'.format(root.right.val)
            # print('R',root.right.val,cur_path_R)
            self.update_path(root.right,cur_path_R)
            
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        if root is None:
            return self.paths
        cur_path = str(root.val)
        self.update_path(root,cur_path)
        return self.paths
            