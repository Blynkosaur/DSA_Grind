# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        my = []
        toreturn= head
        
        dummy = toreturn
        while head != None:
            my.append(head.val)
            head = head.next
        print(my)
        for i in range(len(my)):
            toreturn.val = my[-1]
            toreturn = toreturn.next
            my.pop(-1)
        return dummy