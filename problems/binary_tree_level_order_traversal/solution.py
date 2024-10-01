# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.helper(root, 0)
        return self.output


    def helper(self, root, depth):
        if not root:
            return root

        if depth > (len(self.output) - 1):
            self.output.append([root.val])
        else:
            self.output[depth].append(root.val)

        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)