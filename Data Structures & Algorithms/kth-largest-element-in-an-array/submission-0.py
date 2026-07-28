class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = []
        i=0
        while i < len(nums):
            heapq.heappush(max_heap, -nums[i])
            i+=1

        i=1
        while i<k:
            heapq.heappop(max_heap)
            i+=1

        return -max_heap[0]