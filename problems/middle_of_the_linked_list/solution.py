# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        lenght = 1
        while head.next != None:
            head = head.next
            lenght +=1
        for i in range(int(lenght/2)):
            dummy = dummy.next
        return dummy
        