class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], (dst))
        # 100*ord(dst[0])+10*ord(dst[1])+ord(dst[2]), 
        res = []
        def recurse(airport):
            while adj[airport]:
                air = heapq.heappop(adj[airport])
                recurse(air)
            res.append(airport)
        recurse("JFK")
        res.reverse()
        return res
