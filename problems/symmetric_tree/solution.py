# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        leftnodes = []
        queue = deque([root.left])
        while queue:
            node = queue.popleft()
            
            if node:
                leftnodes.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                leftnodes.append(None)
        rightnodes = []
        queue = deque([root.right])
        while queue:
            node = queue.popleft()
            
            if node:
                rightnodes.append(node.val)
                queue.append(node.right)
                queue.append(node.left)
            else:
                rightnodes.append(None)
        return rightnodes == leftnodes
