class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            k = (left + right) // 2
            hours_used = 0
            for i in piles:
                hours_used += math.ceil(i / k)

            if hours_used <= h:
                result = min(result, k)
                right = k - 1
            else:
                left = k + 1
        
        return result