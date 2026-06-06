class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # find what the new range is and old range
        res = []
        for ind in range(len(intervals)):
            if newInterval[1]<intervals[ind][0]:
                res.append(newInterval)
                return res + intervals[ind:]
            elif newInterval[0] > intervals[ind][1]:
                res.append(intervals[ind])
            else:
                newInterval = [min(newInterval[0], intervals[ind][0]), max(newInterval[1], intervals[ind][1])]  
        res.append(newInterval)   
        return res
         


        