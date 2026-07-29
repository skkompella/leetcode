class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.append(newInterval)
        # print(intervals)
        # intervals.sort(key=lambda x:x[0])
        # print(intervals)
        j=0
        l = len(intervals)
        while j < l and newInterval[0] > intervals[j][0]:
            j+=1
        intervals.insert(j, newInterval)

        i = max(1, j)
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
                intervals.pop(i)
            else:
                i+=1
        return intervals
