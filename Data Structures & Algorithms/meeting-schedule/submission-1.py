"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda interval: interval.start)
        curr_meet = 1
        while curr_meet < len(intervals):
            prev_meet = curr_meet - 1
            if intervals[prev_meet].end > intervals[curr_meet].start:
                return False
            curr_meet+=1
        return True
