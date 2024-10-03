# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.globalMax = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.globalMax = root.val
        self.helper(root, root.val)
        return self.globalMax

    def helper(self, root, localMax):
        if not root:
            return 0
        
        leftMax = self.helper(root.left, localMax)
        rightMax = self.helper(root.right, localMax)

        # localMax = leftMax + rightMax + root.val

        localMax = max(leftMax + rightMax + root.val, rightMax + root.val, leftMax + root.val, root.val)
        
        if localMax > self.globalMax:
            self.globalMax = localMax
        if leftMax < 0 and rightMax < 0:
            localMax = root.val
        else:
            localMax = max(leftMax, rightMax) + root.val
        
        return localMax
        