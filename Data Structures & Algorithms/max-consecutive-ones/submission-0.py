class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # 1. traverse through the array.
        # 2. Increment a counter if current index is 1.
        # 3. If the current index isn't 1, reset the counter. If before this, the counter had max values, set this to a return variable.
        # 4. At the end of the array, return the counter counting max number of ones.
        max_ones = 0
        temp_counter = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp_counter += 1
                if temp_counter > max_ones:
                    max_ones = temp_counter
            if nums[i] != 1:
                temp_counter = 0

        return max_ones
