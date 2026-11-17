# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Find out what the tail is, and the reference to the value right before tail.
        # Convert the tail to the head and head to the tail.
        #prev = None
        #curr = head

        #while curr:
        #    nxt = curr.next
        #    curr.next = prev
        #    prev = curr
        #    curr = nxt
        #return prev

        # Recursive solution:
        # Write base case, and the recursive steps
        # base case:
        if not head:
            return None
        # Recursive step:

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        
        return newHead
