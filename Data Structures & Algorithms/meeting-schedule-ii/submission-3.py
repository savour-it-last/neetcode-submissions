"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_list = sorted([i.start for i in intervals])
        end_list = sorted([i.end for i in intervals])

        res, count = 0, 0
        start_ind, end_ind = 0, 0
        while start_ind < len(start_list):
            if start_list[start_ind]<end_list[end_ind]:
                count+=1
                start_ind+=1
            else:
                end_ind+=1
                count-=1
            res = max(res, count)
        return res


