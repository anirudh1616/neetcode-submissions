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

        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap:
                hashMap[nums[i]] += 1
            else:
                hashMap[nums[i]] = 1
        for key, val in hashMap.items():
            if val > 1:
                return True
        return False
        