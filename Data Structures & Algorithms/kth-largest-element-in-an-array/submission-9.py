class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums = [-num for num in nums]
        # heapq.heapify(nums)

        # for i in range(k):
        #     res = heapq.heappop(nums)
        
        # return -res

        minHeap = []
        for i in range(len(nums)):
            heapq.heappush(minHeap, nums[i])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        return minHeap[0]
            