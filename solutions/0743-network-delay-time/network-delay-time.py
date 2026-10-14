class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # min path with weighted graph => dijkstra

        adj = defaultdict(list)
        dist = {}
        visited = {}
        visited[k]=0
        for u, v, w in times:
            adj[u].append(v)
            dist[(u, v)] = w
        # print(adj.keys(), k)
        q = []
        for nei in adj[k]:
            heapq.heappush(q, (dist[(k, nei)], nei))
        # print(q)
        while len(q) != 0:
            d, node = heapq.heappop(q)
            if node in visited and visited[node] < d:
                continue
            visited[node] = d
            for nei in adj[node]:
                if nei in visited:
                    if visited[nei] > d + dist[(node, nei)]:
                        heapq.heappush(q, (d + dist[(node, nei)], nei))
                else:
                    heapq.heappush(q, (d + dist[(node, nei)], nei))
        # print(visited)
        if len(visited)!=n:
            return -1
        return max(visited.values())
