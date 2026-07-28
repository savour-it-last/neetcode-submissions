class Solution:
    def distance_from_origin(self, point: list[int])->int:
        x_, y_ = point
        return (x_*x_)+(y_*y_)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        reference = {}
        i = 0
        while i < k:
            #FIXME: issue is I need reference to the origin points
            distance = self.distance_from_origin(point= points[i])
            heapq.heappush(max_heap, (-distance, points[i]))
            i+=1

        while i< len(points):
            distance = self.distance_from_origin(point=points[i])
            if max_heap[0][0]< -distance:
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, (-distance, points[i]))
            i+=1

        res = []

        while max_heap:
            res.append(heapq.heappop(max_heap)[1])
        
        return res