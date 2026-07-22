from _heapq import heappop
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        i = 0
        self.kth_max_heap = []
        while i<k and i<len(nums):
            heapq.heappush(self.kth_max_heap, nums[i])
            i+=1
        # We need the maximum value of the remaining, why?
        # if new value is less than or equal to this
        while i < len(nums):
            if nums[i] > self.kth_max_heap[0]:
                heapq.heappop(self.kth_max_heap)
                heapq.heappush(self.kth_max_heap, nums[i])
            i+=1

    def add(self, val: int) -> int:
        if len(self.kth_max_heap) < self.k:
            heapq.heappush(self.kth_max_heap,val)
        elif self.kth_max_heap[0] < val:
            heapq.heappop(self.kth_max_heap)
            heapq.heappush(self.kth_max_heap,val)
            
        return self.kth_max_heap[0]
        
