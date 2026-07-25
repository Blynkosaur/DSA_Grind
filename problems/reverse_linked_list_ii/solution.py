# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNGroup(self, k: int, post_end: Optional[ListNode],head: Optional[ListNode])-> Optional[Listnode]:
        prev = post_end
        curr = head
        for i in range(k):
            temp_next = curr.next
            curr.next = prev
            prev = curr
            curr = temp_next
        return prev
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        k = right - left + 1
        dummy = ListNode(0, head)
        first = head
        tail = dummy
        for i in range(left-1):
            first = first.next
        post_end = first 
        for i in range(k):
            post_end = post_end.next
        reverse = self.reverseNGroup(k, post_end, first)
        for i in range(left-1):
            tail = tail.next
        tail.next = reverse
        return dummy.next
        
        
        
        