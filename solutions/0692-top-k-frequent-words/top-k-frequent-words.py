class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        counts = collections.Counter(words)
        heap = [(-j, i) for i, j in counts.items()]
        # print(heap)
        heapq.heapify(heap)
        # heap = []
        # for word, cnt in counts.items():
        #     heapq.heappush(heap, (-cnt, word))
        
        res = []
        for _ in range(k):
            _, word = heapq.heappop(heap)
            res.append(word)
        return res
