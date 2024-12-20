# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head = ListNode(0,head)
        dummy = head
        if not head:
            return head
        while head:
            while head.next and head.next.val == val:
                head.next = head.next.next
            head = head.next
            
        return dummy.next