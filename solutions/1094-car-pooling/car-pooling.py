class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        events = []
        for num, f, t in trips:
            events.append([f, num])
            events.append([t, -num])
        # events.sort(key=lambda x:x[0])
        events.sort()

        # [1, 2], [3, 3], [5, -2], [7, -3]
        # print(events)
        tot = 0
        for _, cap in events:
            tot += cap
            # print(tot, cap)
            if tot > capacity:
                return False
        return True
