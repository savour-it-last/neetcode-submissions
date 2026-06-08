class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        curr_ind = 0
        sorted_intervals = sorted(intervals)
        res = []
        new_interval = sorted_intervals[curr_ind]
        while curr_ind<len(sorted_intervals):
            if new_interval[1] < sorted_intervals[curr_ind][0]:
                res.append(new_interval)
                new_interval = sorted_intervals[curr_ind]
            # I dont think this scenario will ever playout ngl because its sorted
            # I added so the else has everything else ig
            elif new_interval[0] > sorted_intervals[curr_ind][1]:
                new_interval = sorted_intervals[curr_ind]
            else:
                new_interval = [min(new_interval[0], sorted_intervals[curr_ind][0]), max(new_interval[1], sorted_intervals[curr_ind][1])]
            curr_ind+=1
        if new_interval:
            res.append(new_interval)
        return res


