class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap_s = {}
        hashMap_t = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in hashMap_s:
                hashMap_s[s[i]] += 1
            else:
                hashMap_s[s[i]] = 1
        for j in range(len(t)):
            if t[j] in hashMap_t:
                hashMap_t[t[j]] += 1
            else:
                hashMap_t[t[j]] = 1
        
        return hashMap_s == hashMap_t
