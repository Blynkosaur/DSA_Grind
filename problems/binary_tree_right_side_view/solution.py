# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        tree = defaultdict(list)
        queue = deque([(root,0)])
        if not root:
            return []
        while queue:
            node, layer= queue.popleft()
            tree[layer].append(node.val)
            if node.left:
                queue.append((node.left, layer + 1))
            if node.right:
                queue.append((node.right, layer + 1))
        return [tree[layer][-1] for layer in sorted(tree.keys())]
        