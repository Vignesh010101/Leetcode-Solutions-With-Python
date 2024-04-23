# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        
    def getRandom(self) -> int:
        # Initialize the reservoir with the value of the head node
        reservoir = self.head.val
        
        # Initialize the counter to 2 since we've already processed the head node
        i = 2
        
        # Loop through the linked list starting from the second node
        next = self.head.next
        while next:
            # With probability 1/i, replace the reservoir value with the value of the current node
            if random.random() < 1/i:
                reservoir = next.val
                
            # Increment the counter and move on to the next node
            i += 1
            next = next.next
            
        # Return the final reservoir value
        return reservoir
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()