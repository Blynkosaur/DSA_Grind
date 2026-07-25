# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        def traverse(root:Optional[TreeNode])->None:
            if not root:
                return
            if root.left is not None:
                traverse(root.left)
            if root.right is not None:
                traverse(root.right)
            ret.append(root.val)
        traverse(root)
        return ret
        