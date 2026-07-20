class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        weights = {}
        for f, t, p in flights:
            adj[f].append(t)
            weights[(f, t)] = p
        
        heap = []
        heapq.heappush(heap, (0, src, k+1)) # dist covered, src node, steps
        visited = {}
        while heap:
            dist, u, steps = heapq.heappop(heap)
            if u == dst:
                return dist
            # if u in visited:
            #     continue
            if steps <= 0:
                continue
            if u in visited and visited[u] >= steps:
                continue
            visited[u] = steps

            for v in adj[u]:
                heapq.heappush(heap, (dist + weights[(u, v)], v, steps - 1))
        # if dst in visited:
        #     return visited[dst]
        return -1
