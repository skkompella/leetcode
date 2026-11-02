class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        # make output intersection list (O(n))
        # start at 0, 0 -- if a[1] > b[1] then increase a idx else increase b idx, continue until end
        length_1 = len(firstList)
        length_2 = len(secondList)
        if not firstList or not secondList:
            return []
        i, j  = 0, 0
        res = []
        # lo, hi = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
        lo, hi = 0, 0
        while i < length_1 and j < length_2:
            lo, hi = max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                res.append([lo, hi])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return res
