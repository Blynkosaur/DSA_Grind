# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pval = None if p is None else p.val
        qval = None if q is None else q.val
        print(pval, qval)
        if pval != qval:
            return False
        if pval is not None and qval is not None:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
        return True
        


        
            
        