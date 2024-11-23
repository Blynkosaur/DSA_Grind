# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        answer = ListNode()
        pin = answer
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        nodes.sort()
        for el in nodes:
            answer.next = ListNode(el)
            answer = answer.next
        return pin.next
