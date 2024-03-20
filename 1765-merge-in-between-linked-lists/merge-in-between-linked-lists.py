# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        nodefora=list1
        for i in range(a-1):
            nodefora=nodefora.next
        
        nodeb=nodefora.next
        for i in range(b-a):
            nodeb=nodeb.next

        nodefora.next=list2
        lastlistnode=list2

        while lastlistnode.next:
            lastlistnode=lastlistnode.next

        lastlistnode.next=nodeb.next
        nodeb.next=None
        return list1