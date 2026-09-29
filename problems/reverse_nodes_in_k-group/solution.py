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
    def isReversible(self, k: int, head: Optional[Listnode])->bool:
        for i in range(k):
            if head is None:
                return False
            head = head. next
        return True
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        group_prev = dummy
        while head != None:
            if self.isReversible(k,head):
                post_end = head
                for i in range(k):
                    post_end = post_end.next
                reverse = self.reverseNGroup(k,post_end,head)
                group_prev.next = reverse
                group_prev = head # head here becomes the tail of the group that is reversed
                head = post_end 
            else:
                break
        return dummy.next
            
            
            
        