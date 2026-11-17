class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for i in range(len(nums)):
            n = nums[i]
            counts[n] += 1
        i = 0
        for c in range(len(counts)):
            for m in range(counts[c]):
                nums[i] = c
                i += 1
                