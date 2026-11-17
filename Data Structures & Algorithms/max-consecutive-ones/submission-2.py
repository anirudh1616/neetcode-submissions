class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
                if temp > max:
                    max = temp
            else:
                temp = 0
        return max