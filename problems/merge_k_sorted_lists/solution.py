# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            ret = ListNode(0)
            head = ret
            l1 = lists.pop()
            l2 = lists.pop()
            while l1 and l2:
                if l1.val < l2.val:
                    head.next = l1
                    l1 = l1.next
                else:
                    head.next = l2
                    l2 = l2.next
                head = head.next  

            head.next = l1 if l1 else l2
            lists.append(ret.next)
        return lists[0]

                