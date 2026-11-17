class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {} # stores key [number] and val [# of occurences]
        result = []
        maxVal = 0
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        for i in range(k):
            maxVal = max(hashMap, key=hashMap.get)
            result.append(maxVal)
            del hashMap[maxVal]
        
        return result