# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque([(root,0)])
        hashmap = {}
        ret = []
        while queue:
            node, layer = queue.popleft()
            if layer not in hashmap:
                hashmap[layer] = [node.val]
            else:
                hashmap[layer].append(node.val)
            if node.left:
                queue.append((node.left,layer+1))
            if node.right:
                queue.append((node.right,layer+1))
        
        for node in hashmap:
            ret.append(max(hashmap[node]))  
        return ret