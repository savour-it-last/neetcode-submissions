class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals)
        count = 0
        prev_end = sorted_intervals[0][1]
        for start, end in sorted_intervals[1:]:
            if start >= prev_end:
                prev_end = end
            else:
                # When we have overlapping times, we just remove the one whose end is biggest
                count += 1
                prev_end = min(prev_end, end)
        return count
                  


