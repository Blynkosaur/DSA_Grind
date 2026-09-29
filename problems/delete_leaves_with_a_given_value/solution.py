# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        stack = [root]
        dummy = TreeNode(0, root)
        if not root or (root.val == target and (not root.left and not root.right)):
            return None
        parents = {root:dummy}
        while stack:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
            while not node.right and not node.left and node.val == target:
                parent = parents[node]
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None
                node = parent
        return dummy.left

                



        