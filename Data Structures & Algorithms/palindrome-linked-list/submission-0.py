# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp_list = []
        curr = head
        
        while curr:
            temp_list.append(curr.val)
            curr = curr.next
        
        left, right = 0, len(temp_list) - 1
        while left <= right:
            if temp_list[left] != temp_list[right]:
                return False
            
            left += 1
            right -= 1
        return True