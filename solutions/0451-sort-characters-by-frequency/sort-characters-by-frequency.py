class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        minh = []
        for l in counts.keys():
            heapq.heappush(minh, (-counts[l], l))

        res = ''
        while minh:
            count, l = heapq.heappop(minh)
            res += l*(-count)
        return res
