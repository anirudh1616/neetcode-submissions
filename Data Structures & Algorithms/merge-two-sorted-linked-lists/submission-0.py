# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create an output list which contains a dummy node to satisfy edge case of null output list.
        # Traverse both lists and compare the values of each in order to fill up the dummy list.
        # in the chance that one of the lists are longer than the other, we need to adjust accordingly. Since
        # the lists are sorted already, once the new value is set, the remainder of the non null list, is bound to
        # be larger than the previous set value, so we can just add the rest of the nodes to the output list.

        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        return dummy.next