"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None
        copy_ref = {}
        dummy = head
        prev = None
        while head:
            new_copy_node = Node(head.val)
            copy_ref[head] = new_copy_node
            if prev is not None:
                copy_ref[prev].next = new_copy_node
            prev = head
            head = head.next
        # for node in copy_ref:
            # print(f"original:{node.val}->{node.next} - copy: {copy_ref[node].val}->{copy_ref[node].next}")
        for node in copy_ref:
            original_random = node.random
            if original_random is not None:
                copy_ref[node].random = copy_ref[original_random]
        return copy_ref[dummy]