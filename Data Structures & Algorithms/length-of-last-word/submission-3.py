class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s) - 1
        count = 0
        while s[n] != " ":
            if len(s) > 1:
                count += 1
                n -= 1
            else:
                count = 1
                break
        
        return count