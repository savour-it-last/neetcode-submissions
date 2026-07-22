class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap)>1:
            max1 = -(heapq.heappop(max_heap))
            max2 = -(heapq.heappop(max_heap))
            if max1 == max2:
                continue
            else:
                diff = abs(max2-max1)
                heapq.heappush(max_heap, -diff)
        
        if max_heap:
            return -max_heap[0]
        return 0