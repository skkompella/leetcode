class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        els = {}
        for i in nums:
            if i not in els:
                els[i] = 1
            else:
                els[i] += 1
        res = []
        for el, fr in els.items():
            heapq.heappush(res, (fr, el))
            if len(res) > k:
                heapq.heappop(res)
        return [i[1] for i in res]
