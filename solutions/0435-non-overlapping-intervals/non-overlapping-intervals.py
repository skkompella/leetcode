class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        i = 1
        prev_end = intervals[0][1]
        while i < len(intervals):
            if intervals[i][0] < prev_end:
                # prev_end = min(prev_end, intervals[i-1][1])
                res += 1
            else:
                prev_end=intervals[i][1]
            i+=1
        return res
