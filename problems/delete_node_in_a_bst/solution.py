# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delete(self,root, parent) -> None:
        #find smallest node in the right branch
        if root.right:
            right, tail = root.right, root
            while root.right:
                if right.left:
                    tail = right
                    right = right.left
                else:
                    break
            if root.val == tail.val:
                tail.right = right.right #tricky not tail.right = None cuz minimum of right subtree might not be last node so right.right is just bigger values, impossible to be right.left since by definition it is impossible since right is already smallest value of left subtree
            else:
                tail.left = right.right
            root.val = right.val
        elif root.left:
            left, tail = root.left, root
            while root.left:
                if left.right:
                    tail = left
                    left = left.right
                else:
                    break
            if root.val == tail.val:
                tail.left = left.left #tricky not tail.left = None cuz maximum of left subtree might not be last node so left.left is just smaller values, impossible to be left.right since by definition it is impossible

            else:
                tail.right = left.left #tricky 
            root.val = left.val
        else:
            if root.val > parent.val:
                parent.right = None
            else:
                parent.left = None
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        toDelete, parent = None, None
        stack = [(root, None)]
        if not root:
            return None
        while stack:
            node, parent = stack.pop()
            if node.val == key:
                toDelete = node
                break
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))
        #in case empty tree
        if not toDelete:
            return root
        #in case just one node
        if toDelete is root and not root.left and not root.right: 
            return None
        self.delete(toDelete, parent)
        return root

        
        