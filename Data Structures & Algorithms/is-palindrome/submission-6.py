class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for c in s:
            if c.isalnum():
                newString += c.lower()
        start, end = 0, len(newString) - 1
        while start < end:
            if newString[start] != newString[end]:
                return False
            start += 1
            end -= 1
        return True
        
            