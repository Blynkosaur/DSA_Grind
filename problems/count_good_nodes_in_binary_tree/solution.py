# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    track = 0
    def goodNodes(self, root: TreeNode) -> int:
        self.count(root,root.val)
        return self.track
    def count(self, root, maximum):
        if not root:
            return root
        if root.val >= maximum:
            self.track += 1
        maximum = max(root.val, maximum)
        self.count(root.left, maximum)
        self.count(root.right, maximum)
