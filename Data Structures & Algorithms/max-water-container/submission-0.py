class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_vertex = 0
        right_vertex = len(heights)-1
        max_water = 0
        while left_vertex < right_vertex:
            curr_breadth = abs(right_vertex - left_vertex)
            if heights[left_vertex] > heights[right_vertex]:
                curr_length = heights[right_vertex]
                right_vertex-=1
            else:
                curr_length = heights[left_vertex]
                left_vertex+=1
            area = curr_length*curr_breadth
            if max_water < area:
                max_water = area
        return max_water
            
            