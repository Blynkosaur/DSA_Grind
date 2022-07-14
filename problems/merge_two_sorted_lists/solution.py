# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        # hashmap = {}
        # def algorithm(mylist):
        #     if mylist.val not in hashmap:
        #         hashmap[mylist.val] = 0
        #     hashmap[mylist.val]+= 1
        #     if mylist.next != None:
        #         algorithm(mylist.next)
        # algorithm(list1)
        # algorithm(list2)
        # final = ListNode()
        # def next():
        #     for i in hashmap:
        #         toset = final
        #         for j in range(hashmap[i]):
        #             toset.val = j
        #             toset = toset.next
        # return final
        tail = ListNode()
        
        dummy= tail
        while list1 and list2:
            if list1.val < list2.val:
                dummy.next= list1
                list1 = list1.next
                
            else:
                dummy.next = list2
                list2 = list2.next
            
            dummy = dummy.next
            print(dummy)
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        return tail.next
                
        
                
            
            