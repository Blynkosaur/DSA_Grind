# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return 0, True
            left_height, left_valid = dfs(root.left)
            right_height, right_valid = dfs(root.right)
            is_valid = abs(left_height - right_height) <= 1 and left_valid and right_valid
            return 1+max(left_height,right_height), is_valid
        _ , isValid = dfs(root)
        return isValid

         
            

