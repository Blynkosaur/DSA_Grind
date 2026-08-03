# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_map = {val : idx for idx, val in enumerate(inorder)}
        def dfs(left, right, pre):
            if left > right:
                return None
            root_val = preorder[pre]
            mid = index_map[root_val]
            root = TreeNode(root_val)
            root.left = dfs(left, mid - 1, pre + 1)
            root.right = dfs(mid + 1, right, pre - left + mid + 1)
            return root
        return dfs(0, len(inorder) - 1 , 0)
        