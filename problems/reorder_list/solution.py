# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        length = 0
        prev, reverse = None, head
        header = ListNode()
        normal = header
        ret = ListNode()
        pin = ret
        while reverse:
            header.next = ListNode(reverse.val)
            header = header.next
            nxt = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = nxt
            length += 1
        normal = normal.next
        for i in range(length):
            if i%2 ==0:
                ret.next = ListNode(normal.val)
                normal = normal.next
            else:
                ret.next = ListNode(prev.val)
                prev = prev.next
            ret = ret.next
        pin = pin.next
        head.next = pin.next
        
        
        



        