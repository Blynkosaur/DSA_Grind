# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, one: ListNode, two:ListNode)->ListNode:
        head = ListNode(0)
        dummy = head
        while one and two:
            if one.val < two.val:
                head.next = ListNode(one.val)
                one = one.next
            else:
                head.next = ListNode(two.val)
                two = two.next
            head = head.next
        if one:
            head.next = one
        if two:
            head.next = two
        return dummy.next


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists) > 1:
            first = lists.pop()
            second = lists.pop()
            lists.append(self.mergeTwoLists(first,second))
        return lists[0]
