class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # need to create an array which is twice the length of nums named ans.
        # ans will store the values of nums, in the same order, but twice.
        n = len(nums)
        capacity = 2 * n
        ans = [None] * capacity
        i = 0
        j = 0
        while i < len(ans):
            if i < n:
                ans[i] = nums[i]
            else:
                ans[i] = nums[j]
                j += 1
            i += 1
        return ans