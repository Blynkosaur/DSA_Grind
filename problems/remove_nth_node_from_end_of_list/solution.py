# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pin = head
        if not head.next:
            return None
        while head:
            temp = head
            for i in range(n+1):
                if not temp:
                    return head.next
                temp = temp.next
            if not temp:
                head.next = head.next.next
                return pin
            head = head.next