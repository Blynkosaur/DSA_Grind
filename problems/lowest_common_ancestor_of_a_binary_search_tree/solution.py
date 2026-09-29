# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_val = p.val
        q_val = q.val
        stack = deque([root])
        if not root: 
            return None
        ret = None
        while stack:
            node = stack.popleft()
            if node.val >= p_val and node.val <= q_val or node.val <= p_val and node.val >= q_val:
                return node
            if node.val > p_val and node.val > q_val:
                stack.append(node.left)
            else :
                stack.append(node.right)
        return ret

        
        