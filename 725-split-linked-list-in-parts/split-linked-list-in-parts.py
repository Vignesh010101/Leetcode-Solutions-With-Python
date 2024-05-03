# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, root, k):
        # Create a list of ListNode pointers to store the k parts.
        parts = [None] * k

        # Calculate the length of the linked list.
        len = 0
        node = root
        while node:
            len += 1
            node = node.next

        # Calculate the minimum guaranteed part size (n) and the number of extra nodes (r).
        n, r = divmod(len, k)

        # Reset the pointer to the beginning of the linked list.
        node = root
        prev = None

        # Loop through each part.
        for i in range(k):
            # Store the current node as the start of the current part.
            parts[i] = node

            # Traverse n + 1 nodes if there are remaining extra nodes (r > 0).
            # Otherwise, traverse only n nodes.
            for j in range(n + (1 if r > 0 else 0)):
                prev = node
                node = node.next

            # Disconnect the current part from the rest of the list by setting prev.next to None.
            if prev:
                prev.next = None

            # Decrement the count of extra nodes (r) if applicable.
            if r > 0:
                r -= 1

        # Return the list of k parts.
        return parts