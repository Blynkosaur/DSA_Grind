# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q= deque()
        q.append((root,0))
        nodes = []
        answer = []
        
        while len(q) != 0:
            node = q.popleft()
            value = node[0]
            
            level = node[1]
            if value != None:
                q.append((value.left,level+1))
                q.append((value.right,level+1))
                nodes.append((value.val,level))
        print(nodes)
        level = 0
        new = []
        for i in nodes:
            if i[1] != level:
                level += 1
                answer.append(new)
                new = []
                new.append(i[0])
            else:
                new.append(i[0])
        if new != []:
            
            answer.append(new)
        return answer
        
                
            