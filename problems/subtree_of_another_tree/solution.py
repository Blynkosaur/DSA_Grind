# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p, q)->bool:
        pval = None if p is None else p.val
        qval = None if q is None else q.val
        if pval != qval:
            return False
        if pval is not None and qval is not None:
            return self.isSameTree(p.right,q.right) and self.isSameTree(p.left, q.left)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True 
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
        
        