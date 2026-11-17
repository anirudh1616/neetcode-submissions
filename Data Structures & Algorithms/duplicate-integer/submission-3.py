class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums.sort()

        # if len(nums) > 1:
        #     for i in range(len(nums)):
        #         if nums[i] == nums[i - 1]:
        #             return True
        # else:
        #     return False
        
        # return False

        # create a hashMap, with the num in nums as the key, and their occurences
        # as vals. If any key exists such that its val is 2, then we return true.
        # otherwise, we return false.

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        