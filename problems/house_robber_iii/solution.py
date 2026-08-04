# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root): #robable we can either take or not take from current house
            if not root:
                return 0, 0
            maximum_without, maximum_with_robbing = 0,0
            left_no, left_rob = dfs(root.left)
            right_no, right_rob = dfs(root.right)
            #we rob
            maximum_with_robbing = root.val + left_no + right_no 
            #we don't rob
            maximum_without = max(left_no, left_rob) + max(right_no, right_rob) 
            return (maximum_without, maximum_with_robbing)
        return max(dfs(root))
            
            
        