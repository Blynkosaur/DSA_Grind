# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root:TreeNode, min_range, max_range) -> bool:
            if not root:
                return True
            if not (min_range < root.val < max_range):
                return False
            return dfs(root.left, min_range, root.val) and dfs(root.right, root.val, max_range)
        return dfs(root, float('-inf'), float('inf'))
            
            
        
        