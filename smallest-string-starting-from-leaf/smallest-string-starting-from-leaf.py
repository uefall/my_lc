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
            self.paths.append(cur_path[::-1])
        if root.left is not None:
            cur_path_L = cur_path+'{}'.format(chr(root.left.val+97))
            # print('L',root.left.val,cur_path_L)
            self.update_path(root.left,cur_path_L)
        if root.right is not None:
            cur_path_R = cur_path + '{}'.format(chr(root.right.val+97))
            # print('R',root.right.val,cur_path_R)
            self.update_path(root.right,cur_path_R)
            
    def smallestFromLeaf(self, root: TreeNode) -> str:
        self.paths = []
        if root is None:
            return self.paths
        cur_path = str(chr(root.val+97))
        self.update_path(root,cur_path)
        
        # print(self.paths)
        min_l = len(self.paths[0])
        min_str = self.paths[0]
        for path in self.paths:
            # print(path)
            l = len(path)
            m_flg = False
            min_l = l if l < min_l else min_l
            if path < min_str:
                min_str = path
#             for i in range(min_l):
#                 s = path[i]
#                 s_ = min_str[i]
#                 if s < s_:
#                     min_str = path
#                     # print('update min str',s,s_,min_str)
#                     m_flg = True
#                     break
                    
#             print(m_flg)
#             if not m_flg:
#                 min_str = path if l < min_l else min_str
        # print(min_str,min_l)
        return min_str
