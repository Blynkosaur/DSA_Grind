# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        ls = []
        def dfs(tree,sums):
            if tree:
                sums += tree.val
                dfs(tree.right,sums)
                dfs(tree.left,sums)
                if not tree.left and not tree.right:
                    
                    if sums == targetSum:
                        ls.append(sums)

                        
        dfs(root,0)
        if ls:
            return True
        return False
        
        
        
        