"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def child(self,node,bottom,nexx):
        curr=bottom
        while curr.next:
            if curr.child:
                self.child(curr,curr.child,curr.next)
            curr=curr.next
        node.next=bottom
        bottom.prev=node
        node.child=None
        curr.next=nexx
        if nexx:
            nexx.prev=curr

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        tmp=head
        while tmp:
            if tmp.child:
                nexx=tmp.next
                self.child(tmp,tmp.child,nexx)
            tmp=tmp.next
        return head
        