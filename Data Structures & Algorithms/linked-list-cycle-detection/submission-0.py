# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a hashtable to associate each val with an index position
        # check what index, each node points to.
        # if there exists a node such that it calls an earlier node return true, else false

        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True
        return False
        
