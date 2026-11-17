class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            leftOver = target - n
            if leftOver in hashMap:
                return [hashMap[leftOver], i]
            hashMap[n] = i