class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        dist = [float('inf')]*n
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, 2*w))
        q = []
        q.append((0, 0))
        while q:
            distance, node = heapq.heappop(q)
            if node == n-1:
                return distance
            for nei, w in adj[node]:
                tmp = distance + w
                if dist[nei] > tmp:
                    dist[nei] = tmp
                    heapq.heappush(q, (tmp, nei))
        return -1
