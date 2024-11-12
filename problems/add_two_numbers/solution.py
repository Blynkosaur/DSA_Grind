# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        toreturn = ListNode(0)
        head = toreturn
    
        carry = 0
        totals = []
        while  l1 or l2:
            if l1 and l2:
                total = l1.val +l2.val + carry
                l1 = l1.next
                l2 = l2.next
                
            elif l2:
                total = l2.val + carry
                l2 = l2.next
            elif l1:
                total = l1.val + carry
                l1 = l1.next
            else:
                total = carry
            if total >= 10:
                carry = 1
                total = total - 10
            else:
                carry = 0
            print(total)
            totals.append(total)
        if carry ==1:
            totals.append(1)
        for el in totals:
            toreturn.next = ListNode(el)
            toreturn = toreturn.next
        head = head.next
        return head
            
        
            


