class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Set two pointers, one at each end of the array.
        # swap the two and decrement the end pointer, while incrementing the start pointer.
        # Stop when one of the pointers goes beyond.

        start = 0
        end = len(s) - 1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        