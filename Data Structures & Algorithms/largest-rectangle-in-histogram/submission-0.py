class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # solution can be the max of heights
        # otherwise solution is between two points horizontally
        # horizontal parts diagnosis requires algorithmic thinking.
        #
        ind = 1
        res = heights[0]
        stack = [(0, heights[0])]
        start = 0
        while ind<len(heights):
            start = ind
            while stack and stack[-1][1] > heights[ind]:
                index, height = stack.pop()
                res = max(res, height*(ind - index))
                start = index
            stack.append((start, heights[ind]))
            ind+=1
            
        while stack:
            res = max(res, (len(heights) - stack[-1][0])*stack[-1][1])
            stack.pop()
        return res
                
            
