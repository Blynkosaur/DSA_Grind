# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
#         hashmap = {}
#         while True:
            
#             if head != None:
                
#                 if head not in hashmap:
#                     hashmap[head]= 0
#                 hashmap[head]+=1
#                 if hashmap[head]>1:
#                     return True
#                 head = head.next
#             else:
                
#                 return False
        turtle = head
        rabbit = head
        if head == None:
            return False
        while rabbit and rabbit.next != None:
            turtle = turtle.next
            rabbit = rabbit.next.next
            if rabbit == turtle:
                return True
        return False
        