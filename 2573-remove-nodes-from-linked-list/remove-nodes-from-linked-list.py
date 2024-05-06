# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        stacks=[]
        while curr:
            while stacks and stacks[-1].val<curr.val:
                stacks.pop()
            stacks.append(curr)
            curr=curr.next

        nxt=None
        while stacks:
            curr=stacks.pop()
            curr.next=nxt
            nxt=curr

        return curr