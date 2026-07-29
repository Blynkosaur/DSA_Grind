# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = root
        if root is None:
            return TreeNode(val)
        while root is not None:
            if val > root.val:
                if root.right:
                    root = root.right
                else:
                    root.right = TreeNode(val)
                    return dummy
            else:
                if root.left:
                    root = root.left
                else:
                    root.left = TreeNode(val)   
                    return dummy
        