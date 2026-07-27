class Solution:
    def _euclidian_from_origin(self, point: list[int])->int:
        x, y = [0,0]

        x_, y_ = point

        return (((x-x_)**2)+((y-y_)**2))**0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        reference = {}
        for i in range(len(points)):
            #FIXME: issue is I need reference to the origin points
            distance = self._euclidian_from_origin(point= points[i])
            heapq.heappush(min_heap, distance)
            if distance not in reference:
                reference[distance] = []
            reference[distance].append(i)
        res = []
        for i in range(k):
            distance = heapq.heappop(min_heap)
            indices = reference[distance]
            res.append(points[indices.pop(-1)])
        return res

            
        