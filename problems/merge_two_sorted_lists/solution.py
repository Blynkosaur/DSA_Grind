# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
#         temp = ListNode()
#         dummy = temp
#         dummy.next = list1
#         print("temp1: ", temp)
#         dummy = dummy.next
#         print(dummy)
#         print("temp2: ",temp)
#         dummy.next = list2
#         print(dummy)
#         print(temp)
        
        
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next= list1
                list1 = list1.next
                
                
            else:
                tail.next = list2
                list2 = list2.next
                
                
            
            tail = tail.next
            
            
        if list1:
            tail.next = list1
            print("list1: ",list1)
        elif list2:
            tail.next = list2
            print("list2: ",list2)
        return dummy.next
        
                
        
                
            
            