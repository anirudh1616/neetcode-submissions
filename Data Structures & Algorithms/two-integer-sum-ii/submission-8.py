class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # intution: [ 1 2 3 4 ] we want two numbers indexes, where index 1 < iindex 2. Cannot use the same element twice.

        # [ 1  2  3  4  ] Maybe we traverse the array with two pointers. 1 pointer will travel linearly in increasing icrements. The other points to the direction in which the target may be, typically splitting it by half.
        l = 0
        r = len(numbers) - 1
        curr = 0

        while l < r:
            curr = numbers[l] + numbers[r]
            if curr > target:
                r -= 1
            elif curr < target:
                l += 1
            
            else:
                return [l + 1, r + 1]
        
