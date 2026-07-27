# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_depth = 0
        def checkDepth(root,depth):
            nonlocal max_depth
            if root:
                depth += 1
                max_depth = max(max_depth, depth)
                checkDepth(root.left, depth)
                checkDepth(root.right, depth)
        checkDepth(root,0)
        return max_depth
        